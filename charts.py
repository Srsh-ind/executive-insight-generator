import pandas as pd
import matplotlib.pyplot as plt


def generate_chart(file_path):

    df = pd.read_csv(file_path)

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