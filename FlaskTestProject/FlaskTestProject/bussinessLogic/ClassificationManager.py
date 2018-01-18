from os import listdir
from os.path import isfile, join
from sklearn.naive_bayes import GaussianNB
from FlaskTestProject import (DesignPattern, app)

import os
import errno
import datetime
import json
import numpy as np
import pickle

PICKLEFOLDER = app.config['ENV_FILE_PICKLE_FOLDER']
GTEXMODULEFOLDER = app.config['ENV_FILE_GTEX_MODEL_FOLDER']
TCGAMODULEFOLDER = app.config['ENV_FILE_TCGA_MODEL_FOLDER']
CELLLINEMODULEFOLDER = app.config['ENV_FILE_HUMANCELLLINE_MODEL_FOLDER']
GTEXGENE = app.config['ENV_FILE_GTEX_GENE']
CELLLINEGENE = app.config['ENV_FILE_CELLLINE_GENE']

class ClassificationManager(DesignPattern.Singleton):
    GtexFullDataModel = ''
    GtexGeneLabel = []
    CellLineGeneLabel = []
    GtexClassificationModules = []
    TcgaClassificationModules = []
    CellLineClassificationModules = []
    
    def __init__(self):
        self.GtexFullDataModel = pickle.load( open( PICKLEFOLDER + 'gtex_TrainingNormalizedResult.pkl', 'rb' ) )
        if isfile(GTEXGENE):
            with open (GTEXGENE, "r") as myfile:
                self.GtexGeneLabel=myfile.read().split('\r\n')
        else:
            app.logger.info('GTEXGENE file is not found')

        if isfile(CELLLINEGENE):
            with open (CELLLINEGENE, "r") as myfile:
                self.CellLineGeneLabel=myfile.read().split('\r\n')
        else:
            app.logger.info('CELL Line is not found')
            
        for f in listdir(GTEXMODULEFOLDER):
            fullf = join(GTEXMODULEFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.GtexClassificationModules.append(newPkl)

        for f in listdir(TCGAMODULEFOLDER):
            fullf = join(TCGAMODULEFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.TcgaClassificationModules.append(newPkl)
        
        app.logger.info( datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': cell line classification start loading.')
        a = datetime.datetime.now()
        for f in listdir(CELLLINEMODULEFOLDER):
            fullf = join(CELLLINEMODULEFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.CellLineClassificationModules.append(newPkl)
        app.logger.info( datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': cell line classification loaded.')
        app.logger.info( 'cell line data load time use: ' + str(datetime.datetime.now() - a) )

    """ Data normalization will normalize data following :
        sum(Data) = 2^20
        then return Log2(Data)        """
    def __DataNormalization(self, sample):
        """one sample pass in"""
        sample = sample + 100
        # 2^20 = 1048576
        return np.log2(sample * 1048576/np.sum(sample))
        
    def __matchData(self, unmatchedData, matchMode):
        unmatched = json.loads(unmatchedData)
        matchedData = []
        matchLabel = []
        if matchMode == 'GTEX': #TCGA and GTEX using the same gene
            matchLabel = self.GtexGeneLabel
        elif matchMode == 'CELLLINE': # this is the second gene match mode 
            # we do not have any other labels again
            matchLabel = self.CellLineGeneLabel
        else:
            matchLabel = self.GtexGeneLabel # Gtex still the default match mode
        for gene in matchLabel:
            matchedData.append(unmatched.get(gene, 0))
        return matchedData
    
    def GtexFullDataPredict(self, datalist):
        matchedData = self.__matchData(datalist, 'GTEX')
      #  raise Exception(len(matchedData))
        npmatchedData = np.array([matchedData]).astype(np.float)    
        normalizedData = self.__DataNormalization(npmatchedData)
        return self.GtexFullDataModel.predict(normalizedData)[0]


    """ predictWithFeq will also do normalization """
    def predictWithFeq(self, datalist, predictMode):
        dataPred = np.apply_along_axis(self.__DataNormalization, 1, datalist)
        PdctRslt = []
        PdctModel = None
        if predictMode == 'TCGA':
            PdctModel = self.TcgaClassificationModules
        elif predictMode == 'GTEX':
            PdctModel = self.GtexClassificationModules
        elif predictMode == 'CELLLINE':
            PdctModel = self.CellLineClassificationModules
        else:
            raise KeyError('Unknown Mode: '+predictMode)

        for m in PdctModel:
            PdctRslt.append(m.predict(dataPred)[0])
        result = {}
        for r in PdctRslt:
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

    def calcProbExcludeOne(self, result):    
        mysum = 0
        keys = result.keys()
        for key in keys:
            if result[key] == 1:
                result.pop(key)
            else:
                mysum += result[key]
        keys = result.keys()
        for key in keys:
            result[key] = float(result[key]) * 100 / mysum
        return result

    def matchedDataToProb(self, raw):
        app.logger.info('New matchedDataToProb request come in. Timer Start.')
        a = datetime.datetime.now()
        matchedData = self.__matchData(raw, 'GTEX')
        if not isinstance( matchedData, np.ndarray ):
            matchedData = np.array(matchedData).astype(np.float)
        if matchedData.ndim <= 1:
            matchedData = [matchedData]
        results = {}
        results['GTEX'] = self.predictWithFeq(matchedData, 'GTEX')
        results['TCGA'] = self.predictWithFeq(matchedData, 'TCGA')

        matchedData = self.__matchData(raw, 'CELLLINE')
        if not isinstance( matchedData, np.ndarray ):
            matchedData = np.array(matchedData).astype(np.float)
        if matchedData.ndim <= 1:
            matchedData = [matchedData]
        results['CELLLINE'] = self.predictWithFeq(matchedData, 'CELLLINE')
        for k in results.keys():
            results[k] = self.calcProbExcludeOne(results[k])
        app.logger.info('Request done. Time consume is: ' + str(datetime.datetime.now()-a))
        return results
    
    
        
        

    




    
