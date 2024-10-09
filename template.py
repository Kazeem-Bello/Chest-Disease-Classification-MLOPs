import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = "[%(asctime)]: %(message)s:")

project_name = "chest_disease_classification"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    "dvc.yaml",
    "params.yaml",
    "research/trials.ipynb",
    "templates/index.html",
    "requirements.txt",
    "setup.py",
    "config/config.yaml"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
    else:
        print(f"File {file_path} already exists")
