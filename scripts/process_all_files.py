import pandas as pd
import os

raw_folder = r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\RAW"
processed_folder = r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED"

os.makedirs(processed_folder, exist_ok=True)

files = [f for f in os.listdir(raw_folder) if f.endswith(".csv")]

for file in files:

    path = os.path.join(raw_folder, file)

    df = pd.read_csv(path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Special cleaning for NAV file
    if file == "02_nav_history.csv":
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values(["amfi_code", "date"])
        df["nav"] = df.groupby("amfi_code")["nav"].ffill()
        df = df[df["nav"] > 0]

    # Special cleaning for transactions
    elif file == "08_investor_transactions.csv":
        df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        df = df[df["amount_inr"] > 0]

    # Special cleaning for performance
    elif file == "07_scheme_performance.csv":
        df = df[
            (df["expense_ratio_pct"] >= 0.1)
            & (df["expense_ratio_pct"] <= 2.5)
        ]

    output_file = file.replace(".csv", "_clean.csv")

    df.to_csv(
        os.path.join(processed_folder, output_file),
        index=False
    )

    print(f"Processed: {output_file}")

print("All datasets processed successfully!")