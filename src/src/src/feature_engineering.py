import pandas as pd


def create_features(df: pd.DataFrame):

    # Voltage stability
    df["voltage_stability"] = (
        df["Voltage_measured"]
        .rolling(window=5)
        .std()
    )

    # Temperature variation
    df["temperature_gradient"] = (
        df["Temperature_measured"]
        .diff()
    )

    # Capacity degradation
    df["capacity_decay_rate"] = (
        df["Capacity"]
        .pct_change()
    )

    # Energy efficiency
    df["energy_efficiency"] = (
        df["Voltage_measured"]
        * df["Current_measured"]
    )

    df = df.fillna(0)

    return df
