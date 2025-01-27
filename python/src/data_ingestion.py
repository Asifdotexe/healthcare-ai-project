import os
import kagglehub
import pandas as pd
import logging


from src.config import (PROJECT_ROOT, DATA_DIR, KAGGLE_SOURCE_PATH,
                        KAGGLE_DATA_NAME)

def ingest_data():
    """Ingests the data from kaggle using kagglehub"""
    # Download latest version of data from kaggle
    path = kagglehub.dataset_download(KAGGLE_SOURCE_PATH)
    # Load the dataset as a pandas dataframe and save it to the raw directory
    df = pd.read_csv(os.path.join(path,KAGGLE_DATA_NAME))

    # standardize the dataset columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    data_save_path = os.path.join(DATA_DIR, 'raw', "chest_xray_vectorized_raw.csv")
    df.to_csv(data_save_path, index=False)
    
    print(f"✅ | Dataset ingested and updated please check {data_save_path}")