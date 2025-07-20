from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__  == '__main__':
    try:
        trainingPipelineConfig = TrainingPipelineConfig
        dataingestionconfig = DataIngestionConfig
        logging.info("Enter The Try Block")
    except Exception as e:
        raise NetworkSecurityException(e, sys)    