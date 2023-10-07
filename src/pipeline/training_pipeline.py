import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__ == '__main__':
   obj = DataIngestion()
   train_data , test_data = obj.intiate_data_ingestion()
   data_transformation = DataTransformation()
   train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_path=train_data,test_path=test_data)
   model_trainer = ModelTrainer()
   model_trainer.initiate_model_trainer(train_arr,test_arr)
