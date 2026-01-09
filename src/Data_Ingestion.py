from logger.custom_logger import AppLogger
import pandas as pd

logger = AppLogger().get_logger(__name__)

def DataIngestion(path):
    """
    use case: Loading the data
    Arguments: path of the file
    Return: DataFrame of the file in path
    """
    try:
        data = pd.read_csv(path)
        logger.info(f"Success File from path {path} is successfully loaded")
        return data
    except FileNotFoundError as e:
        logger.error(f"Failed to load file from path {path} | Error: {str(e)}")
        raise