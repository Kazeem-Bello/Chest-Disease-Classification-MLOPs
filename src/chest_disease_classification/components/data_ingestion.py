from chest_disease_classification import logger
from chest_disease_classification.config_class import DataIngestionConfig
import os
import gdown
import zipfile



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        try:
            data_url = self.config.source_url
            unzip_url = self.config.unzip_dir
            local_data_file = self.config.local_data_file

            os.makedirs(unzip_url, exist_ok = True)
            file_id = data_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            logger.info(f"Downloading data from {data_url} to {unzip_url}")
            gdown.download(prefix+file_id, local_data_file)
            logger.info("file downloaded successfully")
        except Exception as e:
            raise e

    def unzip_file(self):

        try:
            unzip_file_path = self.config.unzip_dir
            data_path = self.config.local_data_file
            os.makedirs(unzip_file_path, exist_ok = True)
            logger.info(f"Unzipping the project data into {unzip_file_path}")
            with zipfile.ZipFile(data_path, "r") as file:
                file.extractall(unzip_file_path)
            logger.info(f"Project data successfully unzip at {unzip_file_path}")
        except Exception as e:
            raise e

        
        
