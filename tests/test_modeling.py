import numpy as np
import pandas as pd
from src.modeling import build_preprocess

def test_build_preprocess_runs():
    X = pd.DataFrame({"a":[1, np.nan, 3], "b":["x","y", np.nan]})
    pre = build_preprocess(num_cols=["a"], cat_cols=["b"])
    Z = pre.fit_transform(X)
    assert Z.shape[0] == 3
