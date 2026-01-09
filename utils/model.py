from logger.custom_logger import AppLogger
from sklearn.svm import SVC
import yaml

logger = AppLogger().get_logger(__name__)

with open(r'F:\TitanicE2E\config\config.yml','r') as f:
    parameters = yaml.safe_load(f)



def load_model():
    model = SVC(C =parameters['svm']['C'],
                gamma =parameters['svm']['gamma'],
                 kernel =parameters['svm']['kernel'])
    
    logger.info("Success SVM model loaded successfully")
    
    return model