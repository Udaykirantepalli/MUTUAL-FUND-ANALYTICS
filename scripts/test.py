import pandas as pd

df = pd.read_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\RAW\01_fund_master.csv"
)

print(df.isnull().sum())