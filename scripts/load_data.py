# scripts/load_data.py

import pandas as pd
import os

# Construct path relative to the project root
data_path = os.path.join("..", "data", "diabetes.csv")

# Read the dataset
try:
    df = pd.read_csv(data_path)
    print("Dataset loaded successfully.")
    print(df.head())  # Display the first few rows
except FileNotFoundError:
    print("Dataset not found. Make sure it's in the 'data' folder.")
