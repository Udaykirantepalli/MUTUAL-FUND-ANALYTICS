import pandas as pd

scorecard = pd.read_csv(
    r"C:\Users\UDAY KIRAN\Desktop\mutual fund analytics\outputs\fund_scorecard.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

# Demo risk buckets
scorecard["risk_grade"] = "Moderate"

recommendations = (
    scorecard[
        scorecard["risk_grade"] == risk
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(
    recommendations[
        [
            "amfi_code",
            "sharpe_ratio",
            "fund_score"
        ]
    ]
)