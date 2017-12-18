from os import listdir
from os.path import isfile, join
from FlaskTestProject import (DesignPattern, app)

import numpy as np
import pickle
import json

GTEX_NORMALIZEDDATAFOLDER = app.config['ENV_FILE_GTEX_NORMALIZED_DATA_FOLDER']
TCGA_NORMALIZEDDATAFOLDER = app.config['ENV_FILE_TCGA_NORMALIZED_DATA_FOLDER']
HUMANCELLLINE_NORMALIZEDDATAFOLDER = app.config['ENV_FILE_HUMAN_CELL_LINE_NORMALIZED_DATA_FOLDER']
GTEXGENE = app.config['ENV_FILE_GTEX_GENE']
CELLLINEGENE = app.config['ENV_FILE_CELLLINE_GENE']



class CorrelationManager:
    GtexData = {}
    TcgaData = {}
    HumanCellLineData = {}
    GtexGeneLabel = []
    CellLineGeneLabel = []

    def __init__(self):
        if isfile(GTEXGENE):
            with open (GTEXGENE, "r") as myfile:
                self.GtexGeneLabel=myfile.read().splitlines()
        else:
            app.logger.info('GTEXGENE file is not found')
        if isfile(CELLLINEGENE):
            with open (CELLLINEGENE, "r") as myfile:
                self.CellLineGeneLabel=myfile.read().splitlines()
        else:
            app.logger.info('CELL Line is not found')
        app.logger.info('Correlation Manager - Gene Loaded:')
        app.logger.info('GTEX Gene Count:' + str(len(self.GtexGeneLabel)))
        #app.logger.info(self.GtexGeneLabel)
        app.logger.info('Cell Line Gene Count:' + str(len(self.CellLineGeneLabel)))

        for f in listdir(GTEX_NORMALIZEDDATAFOLDER):
            fullf = join(GTEX_NORMALIZEDDATAFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.GtexData[f.replace('.pkl', '')] = newPkl
        for f in listdir(TCGA_NORMALIZEDDATAFOLDER):
            fullf = join(TCGA_NORMALIZEDDATAFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.TcgaData[f.replace('.pkl', '')] = newPkl
        for f in listdir(HUMANCELLLINE_NORMALIZEDDATAFOLDER):
            fullf = join(HUMANCELLLINE_NORMALIZEDDATAFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.HumanCellLineData[f.replace('.pkl', '')] = newPkl
        app.logger.info('Data loaded. Includes GTEX: ' + str(len(self.GtexData.keys())) + ' TCGA:' + str(len(self.TcgaData.keys())) + ' CellLine: ' + str(len(self.HumanCellLineData.keys())))

    def __correlation(self, s1, s2):
        if s1.size != s2.size:
            app.logger.info('s1 and s2 has different len. s1:' + str(s1.size) + ' s2:' + str(s2.size) )
        return np.corrcoef(s1,s2)[0][1]

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

    """ Data normalization will normalize data following :
        sum(Data) = 2^20
        then return Log2(Data)        """
    def __DataNormalization(self, sample):
        """one sample pass in"""
        sample = sample + 100
        # 2^20 = 1048576
        return np.log2(sample * 1048576/np.sum(sample))

    def calcCorrelation(self, DataSource, Label, userdata):
        DataSource = DataSource.upper()
        sourceData = None
        if DataSource == 'GTEX':
            sourceData = self.GtexData[Label]
        elif DataSource == 'TCGA':
            sourceData = self.TcgaData[Label]
        elif DataSource == 'CELLLINE':
            sourceData = self.HumanCellLineData[Label]
        else:
            raise NotImplementedError()
        result = []
        for s in sourceData:
            matchedData = self.__matchData(userdata, DataSource) 
            if not isinstance( matchedData, np.ndarray ):
                matchedData = np.array(matchedData).astype(np.float)
            normalizedData = self.__DataNormalization(matchedData)
            result.append(self.__correlation(s, normalizedData))
        return result
    
    def calcCorrelationForAllDataSource(self, Label, userdata):
        result = {}
        result['GTEX'] = self.calcCorrelation('GTEX', Label['GTEX'], userdata)
        result['TCGA'] = self.calcCorrelation('TCGA', Label['TCGA'], userdata)
        result['GTEX'] = sorted(result['GTEX'], reverse=True)
        result['TCGA'] = sorted(result['TCGA'], reverse=True)
        #result['CELLLINE'] = self.calcCorrelation('CELLLINE', Label['CELLLINE'], userdata)
        return result
