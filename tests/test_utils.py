import pandas as pd
from src.utils import money_to_float, rmse

def test_money_to_float():
    s = pd.Series(["$1,234.50", "12", None, "bad"])
    out = money_to_float(s)
    assert out.iloc[0] == 1234.50
    assert out.iloc[1] == 12
    assert pd.isna(out.iloc[2])
    assert pd.isna(out.iloc[3])

def test_rmse():
    assert rmse([0, 0], [3, 4]) == 3.5355339059327378
