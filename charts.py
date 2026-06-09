import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_chart(file_path):

    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df["Region"] = df["Region"].astype(str).str.strip()
    df["Region"] = df["Region"].replace({
        "ΝΑ": "NA",
        "ΕΜΕΑ": "EMEA",
        "ΑΡАС": "APAC"
    })

    os.makedirs("outputs", exist_ok=True)

    chart_file = "outputs/revenue_chart.png"

    df.groupby("Region")["Revenue"].sum().plot(
        kind="bar"
    )

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")

    plt.tight_layout()

    plt.savefig(chart_file)
    plt.close()

    return chart_file