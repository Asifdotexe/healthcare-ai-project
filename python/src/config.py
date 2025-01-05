from pathlib import Path

# Define the root directory of the project (hopping 2 directories out)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

#Defining specific folders in your project (preventing hardcoded paths)
DATA_DIR = PROJECT_ROOT / 'data'
NOTEBOOKS_DIR = PROJECT_ROOT / 'python/notebook'
SRC_DIR = PROJECT_ROOT / 'python/src'
print(SRC_DIR)