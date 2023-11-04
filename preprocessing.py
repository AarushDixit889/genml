import pandas as pd
from sklearn.preprocessing import LabelEncoder


class PreprocessorModule:
    def __init__(self, data):
        self.data = data
        self.le = LabelEncoder()

    def applyLabelEncoder(self, col):
        self.data[col] = self.le.fit_transform(self.data[col])
        return self.data

    def oneHotEncode(self, col):
        df = pd.get_dummies(self.data[col])
        self.data = self.data.add(df)
        return self.data

    def makeNewFeature(self, col_name, values):
        self.data[col_name] = values
        return self.data

    def get_data(self): return self.data
