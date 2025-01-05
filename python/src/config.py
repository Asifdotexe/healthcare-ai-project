import os
from pathlib import Path

# Define the root directory of the project (hopping 2 directories out)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

#Defining specific folders in your project (preventing hardcoded paths)
DATA_DIR = PROJECT_ROOT / 'data'
NOTEBOOKS_DIR = PROJECT_ROOT / 'python/notebook'
SRC_DIR = PROJECT_ROOT / 'python/src'

# for kagglehub usecase and not to be confused with the actual project data file path
# source fileL src/data_ingestion.py
KAGGLE_SOURCE_PATH = "redwankarimsony/chestxray8-dataframe"
KAGGLE_DATA_NAME = "train_df.csv"

# path to the file that has been ingested via the kagglehub pipeline 
# source file: src/data_ingestion.py
RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw', "chest_xray_vectorized_raw.csv")