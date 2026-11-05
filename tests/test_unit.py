from src.pipeline import get_grouped


def test_grouped(read_df):
    salary_by_year = get_grouped(read_df)
    assert salary_by_year.isna().sum().sum() == 0
