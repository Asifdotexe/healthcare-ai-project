from pathlib import Path

# Define the root directory of the project (hopping 2 directories out)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

#Defining specific folders in your project (preventing hardcoded paths)
DATA_DIR = PROJECT_ROOT / 'data'
NOTEBOOKS_DIR = PROJECT_ROOT / 'python/notebook'
SRC_DIR = PROJECT_ROOT / 'python/src'

# for kagglehub usecase and not to be confused with the actual project data
# file path
# source file: src/data_ingestion.py
KAGGLE_SOURCE_PATH = "redwankarimsony/chestxray8-dataframe"
KAGGLE_DATA_NAME = "train_df.csv"

# for the kagglehub usecase and not to be confused with the actual project data file path
# source file: src/data_ingestion.py
NIH_DATA_ENTRY_PATH = "nih-chest-xrays/data"
NIH_DATA_ENTRY_NAME = "Data_Entry_2017.csv"