import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav = pd.read_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED\02_nav_history_clean.csv"
)

transactions = pd.read_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED\08_investor_transactions_clean.csv"
)

performance = pd.read_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\PROCESSED\07_scheme_performance_clean.csv"
)

# Save tables into database
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")