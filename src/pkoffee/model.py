from typing import Callable, Tuple
import numpy as np


class Model:
    def __init__(self, name: str, func: Callable, p0: list, bounds: Tuple):
        self.name = name
        self.func = func
        self.p0 = p0
        self.bounds = bounds
        self.params = None
        self.r2 = None

    def fit(self, X: np.ndarray, Y: np.ndarray):
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        pass

    def evaluate(self, X: np.ndarray, Y: np.ndarray) -> float:
        pass
