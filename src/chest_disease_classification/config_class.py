from dataclasses import dataclass
from pathlib import Path

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

