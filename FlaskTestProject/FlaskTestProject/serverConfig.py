
class Config(object):
    DEBUG = True
    WEB_HOSTIP = 'localhost'
    WEB_PORT = '5555'
    WEB_BACKUPPORT = '5555'
    DB_HOSTNAME = 'localhost'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE = 'dbo'
    ENV_RSCRIPT_RUNNING_ENV_PATH = 'C:/Program Files/R/R-3.4.1/bin/RScript.exe'
    ENV_REXE_ENV_PATH = 'C:/Program Files/R/R-3.4.1/bin/R.exe'
    ENV_SCRIPTFOLDER = 'C:/DemoScriptFolder/'
    ENV_INPUT_FILE_PATH = 'C:/DemoWorkingFolder/Inputs/'
    ENV_OUTPUT_FILE_PATH = 'C:/DemoWorkingFolder/Outputs/'
    CONFIG_ALLOWED_EXTENSIONS = set(['csv'])
    ENV_FILE_UPLOAD_FOLDER = 'C:/DemoWorkingFolder/Inputs/'
    ENV_FILE_PICKLE_FOLDER = 'C:/WebsiteData/Pickle/'
    ENV_FILE_GTEX_MODEL_FOLDER = '/home/yaor/website/WebsiteData/Pickle/Model/gtex/'
    ENV_FILE_TCGA_MODEL_FOLDER = '/home/yaor/website/WebsiteData/Pickle/Model/tcga/'
    ENV_FILE_HUMANCELLLINE_MODEL_FOLDER = '' # add your own
    ENV_FILE_GTEX_GENE = 'C:/WebsiteData/Gene/GtexGene.txt'
    ENV_FILE_CELLLINE_GENE = '' # add you own 



class ConfigDevServer(object):
    DEBUG = True
    WEB_HOSTIP = '137.216.157.99'
    WEB_PORT = '80'
    WEB_BACKUPPORT = '5555'
    DB_HOSTNAME = 'localhost'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE = 'dbo'
    ENV_RSCRIPT_RUNNING_ENV_PATH = '/usr/bin/Rscript'
    ENV_REXE_ENV_PATH = '/usr/bin/R'
    ENV_SCRIPTFOLDER = ''
    ENV_INPUT_FILE_PATH = '/home/yaor/website/WebsiteData/UploadFile/'
    ENV_OUTPUT_FILE_PATH = '/home/yaor/website/WebsiteData/DownloadFile/'
    CONFIG_ALLOWED_EXTENSIONS = set(['csv'])
    ENV_FILE_UPLOAD_FOLDER = '/home/yaor/website/WebsiteData/UploadFile/'
    ENV_FILE_PICKLE_FOLDER = '/home/yaor/website/WebsiteData/Pickle/'
    ENV_FILE_GTEX_MODEL_FOLDER = '/home/yaor/website/WebsiteData/Pickle/Model/gtex/'
    ENV_FILE_TCGA_MODEL_FOLDER = '/home/yaor/website/WebsiteData/Pickle/Model/tcga/'
    ENV_FILE_HUMANCELLLINE_MODEL_FOLDER = '/home/yaor/website/WebsiteData/Pickle/Model/human_cell_line/'
    ENV_FILE_GTEX_GENE = '/home/yaor/website/WebsiteData/Gene/GtexGene.txt'
    ENV_FILE_CELLLINE_GENE = '/home/yaor/website/WebsiteData/Gene/CellLineGene.txt'
