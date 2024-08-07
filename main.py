import os
import sys
import torch
import subprocess

from processor import (change_modalities, 
                       rename_files_to_mednext, 
                       copy_brats_files, 
                       rename_files_to_brats)

input_path = "C:/Users/OWNER/Desktop/SPARK-DOCKER/BraTS2024-SSA-Challenge-ValidationData"

root_dir = os.path.dirname(__file__)
os.makedirs(f"{root_dir}/imagesTs", exist_ok = True)
os.makedirs(f"{root_dir}/MedNext_Predictions", exist_ok = True)

imagesTs = f"{root_dir}/imagesTs"
MedNext_Predictions = f"{root_dir}/MedNext_Predictions"


def run_inference(input_path: str, model_path: str):
    if len(os.listdir(imagesTs)) <= 0:
        change_modalities(input_path, imagesTs)
        rename_files_to_mednext(imagesTs)
    else:
        print("There are images in imagesTs already")

    os.system(f"python predict.py -i imagesTs -o MedNext_Predictions -m {model_path} -f 4")

    os.makedirs(f"{root_dir}/Predictions", exist_ok = True)
    Predictions = f"{root_dir}/Predictions"

    if len(os.listdir(MedNext_Predictions)) > 1:
        copy_brats_files(Predictions)
        rename_files_to_brats(Predictions)

run_inference(input_path, "C:/Users/OWNER/Desktop/spark7-docker/3d_full/")