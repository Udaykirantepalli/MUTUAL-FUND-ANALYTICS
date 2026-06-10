import pandas as pd

df = pd.read_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\RAW\02_nav_history.csv"
)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = df.groupby(
    "amfi_code"
)["nav"].ffill()

# Keep only positive NAV
df = df[df["nav"] > 0]

df.to_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED\02_nav_history_clean.csv",
    index=False
)

print(df.shape)
print("NAV Cleaning Complete")