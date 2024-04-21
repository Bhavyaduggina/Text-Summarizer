from textSummarizer.pipeline.stage01_dataingestion import DataIngestionTrainingPipeline
from textSummarizer.logging  import logger

STAGE_NAME ="DATA INGESTION STAGE"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    dataingestion=DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e 