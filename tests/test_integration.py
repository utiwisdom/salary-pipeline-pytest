import pandas as pd


def test_read_df(read_df):
    # Python <-> file system integration
    assert isinstance(read_df, pd.DataFrame)
    assert read_df.shape[0] > 0
