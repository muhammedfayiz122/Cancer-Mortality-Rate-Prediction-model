import os

# Setting the base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths for other files
RAW_DATASET = os.path.join(BASE_DIR, "data", "raw", "cancer_reg.csv")
# PROCESSED_DATASET = os.path.join(BASE_DIR, "data", "processed", "cancer_reg.csv")
# MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
