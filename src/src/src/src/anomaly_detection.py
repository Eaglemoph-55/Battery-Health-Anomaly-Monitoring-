import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN


class HybridAnomalyDetector:

    def __init__(self):

        self.iso_model = IsolationForest(
            contamination=0.03,
            random_state=42
        )

        self.dbscan = DBSCAN(
            eps=1.5,
            min_samples=10
        )

    def detect(self, X):

        iso_predictions = self.iso_model.fit_predict(X)

        dbscan_predictions = self.dbscan.fit_predict(X)

        final_scores = []

        for i in range(len(X)):

            score = 0

            if iso_predictions[i] == -1:
                score += 1

            if dbscan_predictions[i] == -1:
                score += 1

            final_scores.append(score)

        return np.array(final_scores)
