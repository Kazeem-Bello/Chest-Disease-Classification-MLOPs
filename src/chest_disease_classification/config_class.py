from dataclasses import dataclass
from pathlib import Path
from pydantic import BaseModel

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class BaseModelConfig:
    root_dir: Path
    base_model_dir: Path
    updated_base_model_dir: Path
    include_top: bool
    image_size: list
    classes: int
    weights: str
    learning_rate: float

@dataclass
class TrainingConfig:
    root_dir: Path
    model_dir: Path
    updated_base_dir: Path
    training_data: Path
    epoch: int
    bathsize: int
    augmentation: bool
    image_size: list

class ModelTrainingConfig(BaseModel):
    root_dir: Path
    model_dir: Path
    updated_base_model_dir: Path
    training_data: Path
    epoch: int
    batch_size: int
    augmentation: bool
    image_size: list
    learning_rate: float
