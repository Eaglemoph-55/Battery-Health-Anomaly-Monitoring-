from src.data_loader import load_dataset

from src.preprocessing import BatteryPreprocessor

from src.feature_engineering import create_features

from src.anomaly_detection import HybridAnomalyDetector

from src.health_scoring import calculate_health_index

from src.visualization import (
    plot_capacity,
    plot_anomalies
)

from src.evaluation import summarize_anomalies


# Load dataset
df = load_dataset(
    "data/raw/battery_data.csv"
)

# Feature engineering
df = create_features(df)

# Preprocessing
processor = BatteryPreprocessor()

X = processor.clean_data(df)

# Anomaly detection
detector = HybridAnomalyDetector()

anomaly_scores = detector.detect(X)

df["anomaly_score"] = anomaly_scores

# Health index
df["health_index"] = calculate_health_index(df)

# Evaluation
summarize_anomalies(df)

# Visualization
plot_capacity(df)

plot_anomalies(df)

print(df.head())
