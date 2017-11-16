from sklearn.naive_bayes import GaussianNB
from FlaskTestProject import (DesignPattern, app)
from os import listdir
from os.path import isfile, join

import numpy as np
import pickle

PICKLEFOLDER = app.config['ENV_FILE_PICKLE_FOLDER']
BIMODULEFOLDER = app.config['ENV_BIOMODULE_FOLDER']

class ClassificationManager(DesignPattern.Singleton):
    #GtexFullDataModel = ''
    #GtexGenData  = ''
    BiClassificationModules = []

    def __init__(self):
     #   newPkl = pickle.load(open('C:/Pickle/BioModule/_adipose_colon.pkl', 'rb'))
     #   self.BiClassificationModules.append(newPkl)
    #    self.GtexFullDataModel  = pickle.load( open( PICKLEFOLDER + 'gtex_TrainingResult.pkl', 'rb' ) )
        for f in listdir(BIMODULEFOLDER):
            fullf = join(BIMODULEFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.BiClassificationModules.append(newPkl)
    
    def __GenDataMatch__(self, datalist):
        raise(NotImplementedError)

    """ Data normalization will normalize data following :
        sum(Data) = 2^20
        then return Log2(Data)
        """
    def __DataNormalization(self, sample):
        """one sample pass in"""
        sample = sample + 100
        # 2^20 = 1048576
        return np.log2(sample * 1048576/np.sum(sample))

    def __RunForBiPerdiction(self, normalizedData):
        result = []
        for m in self.BiClassificationModules:
            result.append(m.predict(normalizedData)[0])
        return result
    """
    def GtexFullDataPredict(self, datalist):
        return GtexFullDataModel.predict(datalist)
    """
    """ predictWithFeq will also do normalization """
    def predictWithFeq(self, datalist):
        dataPred = np.apply_along_axis(self.__DataNormalization, 1, datalist)
        prdrslt = self.__RunForBiPerdiction(dataPred)
        result = {}
        for r in prdrslt:
            if r in result.keys():
                result[r] += 1
            else:
                result[r] = 1
        return result
    
    def convertFeqToProb(self, rlist):
        fsum = 0
        for k in rlist.keys():
            fsum += rlist[k]
        for k in rlist.keys():
            rlist[k] = rlist[k] * 100 /fsum
        return rlist
    
    def convertStrToList(self, raw):
        lst = []
        for n in raw.replace('[', '').replace(']', '').split(','):
            if n == '[' or n == ']':
                continue
            lst.append(n)
        return [lst]

    def matchedDataToProb(self, matchedData):
        matchedData = self.convertStrToList(matchedData)
        if not isinstance( matchedData, np.ndarray ):
            matchedData = np.array(matchedData).astype(np.float)
        if matchedData.ndim <= 1:
            matchedData = [matchedData]
        
        return self.predictWithFeq(matchedData)
    

    
