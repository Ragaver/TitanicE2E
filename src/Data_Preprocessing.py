from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder,OneHotEncoder
from sklearn.impute import SimpleImputer
import yaml
from utils.outlier_treatment import OutlierCapper
from logger.custom_logger import AppLogger
from src.Data_Ingestion import DataIngestion

logger = AppLogger().get_logger(__name__)

with open(r'F:\TitanicE2E\config\feature_store.yml',"r") as f:
    features = yaml.safe_load(f)

class Preprocessing:
    def __init__(self,data):
        self.data = data

    def remove_duplicates(self):
        try:
            logger.info(f"Success removed duplicates duplicate count {self.data.duplicated().sum()}")
            self.data = self.data.drop_duplicates()
            
        except Exception as e:
            logger.error(f"Failed to remove duplicates Error: {str(e)}")

    def remove_null(self):
        try:
            to_remove = []
            for col in self.data.columns:
                if self.data[col].isnull().mean()>.70:
                    to_remove.append(col)
            self.data.drop(to_remove,axis = 1,inplace = True)
            logger.info(f"Removed columns whose null percent is greater than 70% {to_remove}")

        except Exception as e:
            logger.error(f"Failed to remove duplicates Error: {str(e)}")
            raise
    def transform_features(self):
        continuous_pipeline = Pipeline(
            [
                ('imputer',SimpleImputer(strategy = "median")),
                ('capper',OutlierCapper()),
                 ('scaler',StandardScaler())
                 ]
        )

        discrete_pipeline = Pipeline(
            [
                ('imputer',SimpleImputer(strategy = "most_frequent")),
                 ('scaler',StandardScaler())
                 ]
        )
        ordinal_pipeline = Pipeline(
         [
                ('imputer',SimpleImputer(strategy = "most_frequent")),
                 ('encoder',OrdinalEncoder(categories = [features['order']]))
                 ]
        )
        nominal_pipeline = Pipeline(
         [
                ('imputer',SimpleImputer(strategy = "most_frequent")),
                 ('encoder',OneHotEncoder(handle_unknown = "ignore"))
                 ]
        )
        preprocessor = ColumnTransformer(
            [
                ('continuous',continuous_pipeline,features['continuous']),
                ('discrete',discrete_pipeline,features['discrete']),
                ('ordinal',ordinal_pipeline,features['ordinal']),
                ('nominal',nominal_pipeline,features['nominal'])
            ]
        )
        return preprocessor
        
    def run(self):
        self.remove_duplicates()
        self.remove_null()
        preprocessor = self.transform_features()
        return preprocessor
    

        

    