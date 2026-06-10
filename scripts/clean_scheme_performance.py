import pandas as pd
import os

df = pd.read_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\RAW\07_scheme_performance.csv"
)

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check expense ratio range
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

os.makedirs(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED",
    exist_ok=True
)

df.to_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED\07_scheme_performance_clean.csv",
    index=False
)

print("Rows after cleaning:", len(df))
print("Performance Cleaning Complete")