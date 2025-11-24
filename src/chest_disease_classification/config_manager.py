from chest_disease_classification.config_class import DataIngestionConfig
from chest_disease_classification.utils import read_yaml, create_directory
from pathlib import Path


class ConfigurationManager:
    def __init__(self, config_file_path, params_file_path):
        self.config_file_path = config_file_path
        self.params_file_path = params_file_path

        self.config = read_yaml(self.config_file_path)
        self.params = read_yaml(self.params_file_path)

        create_directory(self.config.artifact_root)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config_data_ingestion = self.config.data_ingestion
        create_directory(config_data_ingestion.root_dir)

        data_ingestion_config = DataIngestionConfig(
        root_dir = Path(config_data_ingestion.root_dir),
        source_url = config_data_ingestion.source_url,
        local_data_file = Path(config_data_ingestion.local_data_file),
        unzip_dir = Path(config_data_ingestion.unzip_dir)
        )
        return data_ingestion_config

