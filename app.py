from src.end_to_end_data_science_project.logger import logging
from src.end_to_end_data_science_project.exception import CustomException
from src.end_to_end_data_science_project.components.data_ingestion import DataIngestion
from src.end_to_end_data_science_project.components.data_ingestion import DataIngestionConfig
from src.end_to_end_data_science_project.components.data_transformation import DataTransformationConfig, DataTransformation
from src.end_to_end_data_science_project.components.model_trainer import ModelTrainConfig,ModelTrainer
import pickle
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.end_to_end_data_science_project.pipeline.prediction_pipeline import CustomData,PredictPipeline

import sys

application = Flask(__name__)

app = application

# Route for home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=="GET":
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True) 




# if __name__=="__main__":
#     logging.info("The execution has started")

#     try:
#         # data_ingestion_config = DataIngestionConfig()
#         data_ingestion = DataIngestion()
#         train_data_path, test_data_path = data_ingestion.intiate_data_ingestion()

#         # data_transformation_confit = DataTransformationConfig()
#         data_transformation = DataTransformation()
#         train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

#         #Model tarining
#         model_trainer = ModelTrainer()
#         print(model_trainer.initiate_model_trainer(train_arr,test_arr))

#     except Exception as e:
#         logging.info("Custom exception")
#         raise CustomException(e,sys)