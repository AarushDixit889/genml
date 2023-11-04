from pycaret.regression import setup, compare, pull, predict, save_model, load_model


class RegressionModel:
    def __init(self):
        self.best_model = None
        self.setup_df = None

    def setup(self, data_with_y, target_column):
        setup_df = setup(data_with_y, target=target_column)
        self.setup_df = pull()
        return self.setup_df

    def train(self):
        self.best_model = compare()
        return pull()

    def save_model(self, path):
        save_model(self.best_model, path)

    def load_model(self, path):
        self.best_model = load_model(path)
        return self.best_model

    def predict(self, X):
        return predict(self.best_model, X)
