import os
import sys
from src.end_to_end_data_science_project.exception import CustomException
from src.end_to_end_data_science_project.logger import logging
import pandas as pd
import pickle


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)