from chest_disease_classification import logger
from chest_disease_classification.config_manager import ConfigurationManager
from chest_disease_classification.components.data_ingestion import DataIngestion
from chest_disease_classification.components.base_model import BaseModel
from chest_disease_classification.components.model_training import Model
from pathlib import Path


class DataIngestionTraining:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("Initializing Data Ingestion Component")
            config = ConfigurationManager(config_file_path = Path("config/config.yaml"), params_file_path = Path("params.yaml"))
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.unzip_file()
            logger.info("Data Ingestion Completed Successfully")
        except Exception as e:
            raise e
        
class BaseModelTraining:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("Getting the base model (VGG16) from Kera")
            config = ConfigurationManager(config_file_path = Path("config/config.yaml"), params_file_path = Path("params.yaml"))
            base_model_config = config.get_base_model_config()
            base_model = BaseModel(config = base_model_config)
            base_model.get_base_model()
            base_model.update_base_model()
            logger.info("Base model architecture successfully downloaded and updated")
        except Exception as e:
            raise e

class ModelTraining:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("Starting model training")
            config = ConfigurationManager(config_file_path = Path("config/config.yaml"), params_file_path = Path("params.yaml"))
            model_config = config.get_training_config()
            model_training = Model(config = model_config)
            model_training.get_base_model()
            model_training.train_valid_generator()
            model_training.train()
            logger.info("Model successfully trained")
        except Exception as e:
            raise e
