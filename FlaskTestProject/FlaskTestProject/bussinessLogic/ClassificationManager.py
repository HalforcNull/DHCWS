from sklearn.naive_bayes import GaussianNB
from FlaskTeskProject import DesignPattern.Singleton 
import numpy as np
import pickle

PICKLEFOLDER = app.config['ENV_FILE_PICKLE_FOLDER']

class ClassificationManager(Singleton):
    GtexFullDataModel = ''
    GtexGenData  = ''
    def __init__(self):
        self.GtexFullDataModel  = pickle.load( open( PICKLEFOLDER + 'gtex_TrainingResult.pkl', 'rb' ) )

    def __GenDataMatch__(self, datalist):
        raise(NotImplementedError)

    def __DataNormalization__(self, datalist):
        raise(NotImplementedError)

    def GtexFullDataPredict(self, datalist):
        inputData = array(datalist).astype(np.float)
        return GtexFullDataModel.predict(inputData)



