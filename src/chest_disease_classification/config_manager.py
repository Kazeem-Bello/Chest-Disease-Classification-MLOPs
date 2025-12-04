from chest_disease_classification.config_class import DataIngestionConfig, BaseModelConfig, ModelTrainingConfig
from chest_disease_classification.utils import read_yaml, create_directory
from pathlib import Path
import os


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
    
    def get_base_model_config(self) -> BaseModelConfig:
        config_base_model = self.config.base_model
        create_directory(config_base_model.root_dir)

        base_model_config = BaseModelConfig(
            root_dir = Path(config_base_model.root_dir),
            base_model_dir = Path(config_base_model.base_model_dir),
            updated_base_model_dir = Path(config_base_model.updated_base_model_dir),
            include_top = self.params.include_top,
            image_size = self.params.image_size,
            classes = self.params.classes,
            weights = self.params.weights,
            learning_rate = self.params.learning_rate
        )
        return base_model_config
    
    def get_training_config(self) -> ModelTrainingConfig:
        config_training = self.config.model_training
        config_base_model = self.config.base_model
        config_data_ingestion = self.config.data_ingestion
        training_data = os.path.join(config_data_ingestion.unzip_dir, "Chest-CT-Scan-data")
        
        create_directory(config_training.root_dir)
        model_training_config = ModelTrainingConfig(
            root_dir = Path(config_training.root_dir),
            model_dir = Path(config_training.model_dir),
            updated_base_model_dir = Path(config_base_model.updated_base_model_dir),
            training_data = Path(training_data),
            epoch = self.params.epoch,
            batch_size = self.params.batch_size,
            augmentation = self.params.augmentation,
            image_size = self.params.image_size,
            learning_rate = self.params.learning_rate
        )
        return model_training_config
        


