import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\Data\RAW\live_hdfc_nav.csv",
    index=False
)

print("Live NAV data saved successfully!")
print(df.head())