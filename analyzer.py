import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    df["Region"] = df["Region"].astype(str).str.strip()
    df["Region"] = df["Region"].replace({
        "ΝΑ": "NA",
        "ΕΜΕΑ": "EMEA",
        "ΑΡАС": "APAC"
    })

    total_revenue = df['Revenue'].sum()

    growth = (
        (df['Revenue'].iloc[-1] - df['Revenue'].iloc[0])
        / df['Revenue'].iloc[0]
    ) * 100

    top_region = df.groupby('Region')['Revenue'].sum().idxmax()

    avg_churn = df['Churn'].mean()

    return {
        "total_revenue": int(total_revenue),
        "growth": float(round(growth, 2)),
        "top_region": str(top_region).strip(),
        "avg_churn": float(round(avg_churn, 2))
}