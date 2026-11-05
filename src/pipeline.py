from pathlib import Path
import pandas as pd

DF_PATH = Path(__file__).resolve().parent.parent / "data" / "salaries.csv"


def read_data(path=DF_PATH) -> pd.DataFrame:
    """Load the salaries dataset."""
    return pd.read_csv(path)


def get_grouped(df: pd.DataFrame) -> pd.DataFrame:
    """Salary summary statistics per work year."""
    return df.groupby("work_year").agg({"salary": "describe"})["salary"]
