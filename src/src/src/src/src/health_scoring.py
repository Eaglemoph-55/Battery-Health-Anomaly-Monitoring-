import pandas as pd


def calculate_health_index(df: pd.DataFrame):

    health_index = (

        (1 - df["voltage_stability"]) * 0.30 +

        (1 - abs(df["temperature_gradient"])) * 0.20 +

        (1 - abs(df["capacity_decay_rate"])) * 0.30 +

        (df["energy_efficiency"]) * 0.20
    )

    return health_index
