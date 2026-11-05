from src.pipeline import get_grouped


def test_feature_2022(read_df):
    """Feature: the 2022 median salary must work and make sense."""
    salary_by_year = get_grouped(read_df)
    salary_2022 = salary_by_year.loc[2022, "50%"]
    assert isinstance(salary_2022, float)
    assert salary_2022 > 0
