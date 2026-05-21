import matplotlib.pyplot as plt


def plot_capacity(df):

    plt.figure(figsize=(10, 5))

    plt.plot(df["Capacity"])

    plt.title("Battery Capacity Degradation")

    plt.xlabel("Cycle")

    plt.ylabel("Capacity")

    plt.grid(True)

    plt.show()


def plot_anomalies(df):

    plt.figure(figsize=(10, 5))

    plt.scatter(
        range(len(df)),
        df["Capacity"],
        c=df["anomaly_score"]
    )

    plt.title("Battery Anomaly Detection")

    plt.xlabel("Cycle")

    plt.ylabel("Capacity")

    plt.grid(True)

    plt.show()
