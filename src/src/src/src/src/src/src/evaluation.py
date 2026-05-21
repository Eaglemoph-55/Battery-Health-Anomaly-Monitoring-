import pandas as pd


def summarize_anomalies(df: pd.DataFrame):

    anomaly_count = (
        df["anomaly_score"] > 0
    ).sum()

    print(f"Detected anomalies: {anomaly_count}")

    print(df["anomaly_score"].value_counts())
