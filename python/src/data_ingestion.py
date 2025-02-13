import os
import chardet
import kagglehub
import pandas as pd


from config import (DATA_DIR, 
                    KAGGLE_SOURCE_PATH, KAGGLE_DATA_NAME, 
                    NIH_DATA_ENTRY_PATH, NIH_DATA_ENTRY_NAME)

def ingest_data(source_path: str, data_set_name: str):
    """Ingests the data from kaggle using kagglehub"""
    # Download latest version of data from kaggle
    path = kagglehub.dataset_download(source_path, path=data_set_name)
    # Load the dataset as a pandas dataframe and save it to the raw directory

    # Detect the file's encoding
    with open(path, 'rb') as file:
        result = chardet.detect(file.read())
        print(result)
    # Use the detected encoding
    df = pd.read_csv(path, encoding=result['encoding'])

    # standardize the dataset columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    dataset_name = data_set_name.split('.')[0].lower()
    data_save_path = os.path.join(DATA_DIR, 'raw', f"{dataset_name}_raw.csv")
    df.to_csv(data_save_path, index=False)
    
    print(f"✅ | Dataset ingested and updated please check {data_save_path}")
    

# ingesting the chest-xray binary dataset from Kagglehub
ingest_data(source_path=KAGGLE_SOURCE_PATH, data_set_name=KAGGLE_DATA_NAME)
# ingesting the 2017 data entry dataset from Kagglehub
ingest_data(source_path=NIH_DATA_ENTRY_PATH, data_set_name=NIH_DATA_ENTRY_NAME)