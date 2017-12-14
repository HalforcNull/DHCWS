from os import listdir
from os.path import isfile, join
from FlaskTestProject import (DesignPattern, app)

import numpy as np
import pickle

GTEX_NORMALIZEDDATAFOLDER = app.config['ENV_FILE_GTEX_NORMALIZED_DATA_FOLDER']
TCGA_NORMALIZEDDATAFOLDER = app.config['ENV_FILE_TCGA_NORMALIZED_DATA_FOLDER']
HUMANCELLLINE_NORMALIZEDDATAFOLDER = app.config['ENV_FILE_HUMAN_CELL_LINE_NORMALIZED_DATA_FOLDER']



class CorrelationManager:
    GtexData = {}
    TcgaData = {}
    HumanCellLineData = {}

    def __init__(self):
        for f in listdir(GTEX_NORMALIZEDDATAFOLDER):
            fullf = join(GTEX_NORMALIZEDDATAFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.GtexData[f] = newPkl
        for f in listdir(TCGA_NORMALIZEDDATAFOLDER):
            fullf = join(TCGA_NORMALIZEDDATAFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.TcgaData[f] = newPkl
        for f in listdir(HUMANCELLLINE_NORMALIZEDDATAFOLDER):
            fullf = join(HUMANCELLLINE_NORMALIZEDDATAFOLDER,f)
            if isfile(fullf) and f.rsplit('.', 1)[1].lower() == 'pkl':
                newPkl = pickle.load(open(fullf, 'rb'))
                self.HumanCellLineData[f] = newPkl
        app.logger.info('Data loaded. Includes GTEX: ' + str(len(self.GtexData.keys())) + ' TCGA:' + str(len(self.TcgaData.keys())) + ' CellLine: ' + str(len(self.HumanCellLineData.keys())))

    def __correlation(self, s1, s2):
        return np.corrcoef(s1,s2)[0][1]

    def calcCorrelation(self, DataSource, Label, userdata):
        DataSource = DataSource.toUpper()
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
            result.append(self.__correlation(s, userdata))
        return result
    
    def calcCorrelationForAllDataSource(self, Label, userdata):
        result = {}
        result['GTEX'] = self.calcCorrelation('GTEX', Label['GTEX'], userdata)
        result['TCGA'] = self.calcCorrelation('TCGA', Label['TCGA'], userdata)
        result['CELLLINE'] = self.calcCorrelation('CELLLINE', Label['CELLLINE'], userdata)
        return result
