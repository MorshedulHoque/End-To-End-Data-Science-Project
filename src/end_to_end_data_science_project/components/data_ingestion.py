import os
import sys
from src.end_to_end_data_science_project.exception import CustomException
from src.end_to_end_data_science_project.logger import logging
import pandas as pd

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.end_to_end_data_science_project.components.data_transformation import DataTransformation
from src.end_to_end_data_science_project.components.data_transformation import DataTransformationConfig


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def intiate_data_ingestion(self):
        try:
            #reading data from mysql
            # df=read_sql_data()
            df = pd.read_csv("Raw_data.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            train_set,test_set = train_test_split(df, test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion completed")

            return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)
        

# if __name__ == "__main__":
#     obj = DataIngestion()
#     train_data,test_data=obj.intiate_data_ingestion()

#     data_transformation = DataTransformation()
#     data_transformation.initiate_data_transformation(train_data,test_data)

