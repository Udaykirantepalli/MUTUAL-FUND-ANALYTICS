import pandas as pd
import os

folder_path = r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\RAW"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

for file in csv_files:
    print("\n" + "="*60)
    print("DATASET:", file)

    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())