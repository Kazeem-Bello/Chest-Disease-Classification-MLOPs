from chest_disease_classification import logger
from chest_disease_classification.config_manager import ConfigurationManager
from chest_disease_classification.components.data_ingestion import DataIngestion
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
        


