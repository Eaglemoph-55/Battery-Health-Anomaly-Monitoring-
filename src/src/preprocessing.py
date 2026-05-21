import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


class BatteryPreprocessor:

    def __init__(self):

        self.imputer = SimpleImputer(strategy="median")

        self.scaler = StandardScaler()

    def clean_data(self, df: pd.DataFrame):

        numeric_columns = df.select_dtypes(
            include=["float64", "int64"]
        ).columns

        df[numeric_columns] = self.imputer.fit_transform(
            df[numeric_columns]
        )

        scaled_data = self.scaler.fit_transform(
            df[numeric_columns]
        )

        scaled_df = pd.DataFrame(
            scaled_data,
            columns=numeric_columns
        )

        return scaled_df
