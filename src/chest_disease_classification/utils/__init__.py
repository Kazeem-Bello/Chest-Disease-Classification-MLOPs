import os
from box.exceptions import BoxValueError
import yaml
from chest_disease_classification import logger
import json
import joblib
from ensure import ensure_annotation
from box import configBox
from pathlib import path
from typing import any
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

@ensure_annotation
def save_json(path: str, data: dict):
    """ save json data
    Args:
        path (str): path to json file
        data (dict: data to be saved)"""
    try:
        with open(path, "w") as file:
            json.dump(data, file, input = 1)
        logger.info("json file saved at. %s", path)
    except Exception as e:
        raise e


@ensure_annotation
def load_json(path: str) -> configBox:
   """load json data
   Args:
        path(str): path to the file to be loaded
   """
    try:
        with open(path, "r") as file:
            content = json.load(file)
        logger.info("json file loaded successfully from %s", path)
        return configBox(content)
    except BoxValueError:
        raise ValueError("file content empty at %s", path)
    except FileNotFoundError:
        logger.error("file not found: %s", path)
        raise
    except Exception as e:
        raise e
   


@ensure_annotation
def save_bin(path: str, data: any):
    """save a binary file
    Args:
        path (str): path the bin file to be saved
        data (aby): the bin data
        """
    try:
        with open(path, "wb") as file:
            joblib.dump(data, file, index = 1)
        logger.info("binary file saved at: %s", path)
    except Exception as e:
        raise e


@ensure_annotation
def load_bin(path: str):
    """load binary data
    Args:
        path (str): the path to the binary files"""

    try:
        with open(path, "rb") as file:
            bin = joblib.load(file)
        logger.info("binary file loaded fomr %s", path)
        return bin
    except Exception as e:
        raise e
    
@ensure_annotation
def get_size(path: str) -> str:
    """get size in KB
    Args:
        path (str): path of the file
    Returns:
        str:size in KB"""
    size_in_kb = round(os.path.getsize(path)/ 1024)
    return f"~{size_in_kb} KB"


def decode_image(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open (fileName, "wb") as f:
        f.write(imgdata)
        f.close()

def encode_image_into_base64(croppedImagePath):
    with open(croppedImagePath, "wb") as f:
        return base64.b64encode(f.read())



          


