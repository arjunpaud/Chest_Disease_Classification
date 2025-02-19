from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation_with_mlflow import EvaluationPipeline

STAGE_NAME= "Data Ingestion stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed<<<<\n\n x======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Prepare Base Model"

try:
    logger.info(f"*************")
    logger.info(f">>>>>>>Stage{STAGE_NAME} started <<<<")
    prepare_base_model=PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Training"

try:
    logger.info(f"*************")
    logger.info(f">>>>>>>Stage{STAGE_NAME} started <<<<")
    model_trainer=ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x======x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Model Evaluation"

try:
    logger.info(f"*************")
    logger.info(f">>>>>>>Stage{STAGE_NAME} started <<<<")
    model_eval=EvaluationPipeline()
    model_eval.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x======x")
except Exception as e:
    logger.exception(e)
    raise e

