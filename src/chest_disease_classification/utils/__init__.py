import os
from box.exceptions import BoxValueError
import yaml
from chest_disease_classification import logger
import json
import joblib
from ensure import ensure_annotation
from box import configBox
from pathlib import path
fromtyping import any
import base64



@ensure_annotation
def read_yaml(path: str) ->configBox:
    """reads yaml file and returns
    Args:
        path (str): path to the yaml file
        
    Raises:
        valueError: if yaml file is empty
        e: if file does not exist
        
    Returns:
        configBoox:
            configBox type"""

    try:
        with open(path, "r") as file:
            yaml_file = yaml.safe_load(file)
        logger.info("parameters successfully loaded from, %s", path)
        return configBox(yaml_file)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except FileNotFoundError:
        logger.error("file not found: %s", path)
        raise
    except Exception as e:
        raise e
    

@ensure_annotation
def create_directory(path: str, verbose = True):
    """Create a of directory
    
    Args:
        path (str): path of directories"""

    os.makedirs(path, exist_ok = True)
    logger.info("Directory created at: %s", path)


          


