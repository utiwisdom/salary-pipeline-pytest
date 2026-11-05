import pytest
from src.pipeline import read_data


@pytest.fixture
def read_df():
    return read_data()
