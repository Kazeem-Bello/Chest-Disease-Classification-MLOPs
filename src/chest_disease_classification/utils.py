import os
from box.exceptions import BoxValueError
import yaml
from chest_disease_classification import logger
import json
import joblib
# from ensure import ensure_annotations
from pydantic import validate_call
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@validate_call
def read_yaml(path: Path) ->ConfigBox:
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
        return ConfigBox(yaml_file)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except FileNotFoundError:
        logger.error("file not found: %s", path)
        raise
    except Exception as e:
        raise e
    

@validate_call
def create_directory(path: Path, verbose = True):
    """Create a of directory
    
    Args:
        path (str): path of directories"""

    os.makedirs(Path(path), exist_ok = True)
    logger.info("Directory created at: %s", path)

@validate_call
def save_json(path: Path, data: dict):
    """ save json data
    Args:
        path (str): path to json file
        data (dict: data to be saved)"""
    try:
        os.makedirs(os.path.dirname(path), exist_ok= True)
        with open(path, "w") as file:
            json.dump(data, file, input = 1)
        logger.info("json file saved at. %s", path)
    except Exception as e:
        raise e


@validate_call
def load_json(path: Path) -> ConfigBox:
    """load json data
    Args:
    path(str): path to the file to be loaded
    """
    try:
        # Create directory using Path methods
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "r") as file:
            content = json.load(file)
        logger.info("json file loaded successfully from %s", path)
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("file content empty at %s", path)
    except FileNotFoundError:
        logger.error("file not found: %s", path)
        raise
    except Exception as e:
        raise e
   

@validate_call
def save_bin(path: Path, data: Any):
    """save a binary file
    Args:
        path (Path): path the bin file to be saved
        data (Any): the bin data
        """
    try:
        os.makedirs(os.path.dirname(path), exist_ok= True)
        with open(path, "wb") as file:
            joblib.dump(data, file)
        logger.info("binary file saved at: %s", path)
    except Exception as e:
        raise e


@validate_call
def load_bin(path: Path):
    """load binary data
    Args:
        path (str): the path to the binary files"""

    try:
         # Create directory using Path methods
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "rb") as file:
            bin = joblib.load(file)
        logger.info("binary file loaded fomr %s", path)
        return bin
    except Exception as e:
        raise e
    
# @ensure_annotations
@validate_call
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (str): path of the file
    Returns:
        str:size in KB"""
    
    # Create directory using Path methods
    path.parent.mkdir(parents=True, exist_ok=True)
    size_in_kb = round(os.path.getsize(path)/ 1024)
    return f"~{size_in_kb} KB"


def decode_image(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open (fileName, "wb") as f:
        f.write(imgdata)
        f.close()

def encode_image_into_base64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())



          


