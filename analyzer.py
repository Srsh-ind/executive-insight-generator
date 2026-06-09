import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)

    total_revenue = df['Revenue'].sum()

    growth = (
        (df['Revenue'].iloc[-1] - df['Revenue'].iloc[0])
        / df['Revenue'].iloc[0]
    ) * 100

    top_region = df.groupby('Region')['Revenue'].sum().idxmax()

    avg_churn = df['Churn'].mean()

    return {
        "total_revenue": total_revenue,
        "growth": round(growth, 2),
        "top_region": top_region,
        "avg_churn": round(avg_churn, 2)
    }