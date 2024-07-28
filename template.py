from pathlib import Path
import os

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

project="objectdetection"

list_of_files = [
    ".github/workflow/.gitkeep/",
    f"src/{project}/__init__.py",
    f"src/{project}/components/__init__.py",
    f"src/{project}/components/data_ingestion.py",
    f"src/{project}/components/data_validation.py",
    f"src/{project}/components/model_trainer.py",
    f"src/{project}/components/model_pusher.py",
    f"src/{project}/configuraion/__init__.py",
    f"src/{project}/configuraion/s3_operation.py",
    f"src/{project}/constants/__init__.py",
    f"src/{project}/constants/training_pipeline/__init__.py",
    f"src/{project}/constants/application.py",
    f"src/{project}/entity/__init__.py",
    f"src/{project}/entity/artifact_entity.py",
    f"src/{project}/entity/config_entity.py",
    f"src/{project}/exception/__init__.py",
    f"src/{project}/logger/__init__.py",
    f"src/{project}/pipeline/__init__.py",
    f"src/{project}/pipeline/training_pipeline.py",
    f"src/{project}/main/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
    "app.py",
    "Dockerfile",
    'requirements.txt',
    "setup"
    
  
]

for file_path in list_of_files:
    file_path= Path(file_path)
    file_dir,file_name=os.path.split(file_path)
    
    
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} and creating file name{file_name}")
        
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Created file: {file_path}")
        
    else:
        logging.info(f"File {file_path} already exists.")
    
        