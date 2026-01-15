from typing import Callable, Tuple, Optional
import numpy as np
from scipy.optimize import curve_fit
from dataclasses import dataclass


@dataclass
class Model:
    """Represents a curve fitting model for productivity data."""
    
    name: str
    func: Callable
    p0: list
    bounds: Tuple = (-np.inf, np.inf)
    
    def __post_init__(self):
        """Store fit results after initialization."""
        self.params: Optional[np.ndarray] = None
        self.r2: Optional[float] = None
        self.fitted: bool = False
    
    def fit(self, X: np.ndarray, Y: np.ndarray, maxfev: int = 20000) -> 'Model':
        """Fit the model to data and calculate R² score."""
        self.params, _ = curve_fit(
            self.func, X, Y, 
            p0=self.p0, 
            bounds=self.bounds, 
            maxfev=maxfev
        )
        self.fitted = True
        
        yhat = self.predict(X)
        ss_res = float(np.sum((Y - yhat) ** 2))
        ss_tot = float(np.sum((Y - np.mean(Y)) ** 2))
        self.r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict Y values for given X using fitted parameters."""
        if not self.fitted or self.params is None:
            raise ValueError(f"Model '{self.name}' must be fitted before prediction")
        return self.func(X, *self.params)
    
    def __repr__(self) -> str:
        if self.fitted:
            return f"Model(name='{self.name}', R²={self.r2:.3f})"
        return f"Model(name='{self.name}', unfitted)"
