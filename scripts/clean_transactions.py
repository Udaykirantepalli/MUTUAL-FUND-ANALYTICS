import pandas as pd
import os

df = pd.read_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\RAW\08_investor_transactions.csv"
)

# Convert date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only positive transaction amounts
df = df[df["amount_inr"] > 0]

# Validate KYC values
valid_kyc = ["Verified", "Pending"]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

os.makedirs(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED",
    exist_ok=True
)

df.to_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED\08_investor_transactions_clean.csv",
    index=False
)

print("Rows after cleaning:", len(df))
print("Transaction Cleaning Complete")