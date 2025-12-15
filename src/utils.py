import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

def money_to_float(s: pd.Series) -> pd.Series:
    return pd.to_numeric(
        s.astype(str).str.replace(r"[$,]", "", regex=True),
        errors="coerce"
    )

def rmse(y_true, y_pred) -> float:
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))
