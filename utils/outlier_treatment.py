import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class OutlierCapper(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        X = np.asarray(X)
        self.q1 = np.quantile(X, 0.25, axis=0)
        self.q3 = np.quantile(X, 0.75, axis=0)
        self.iqr = self.q3 - self.q1
        return self

    def transform(self, X):
        X = np.asarray(X)
        lower = self.q1 - 1.5 * self.iqr
        upper = self.q3 + 1.5 * self.iqr
        return np.clip(X, lower, upper)
