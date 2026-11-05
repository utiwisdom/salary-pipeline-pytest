from src.pipeline import get_grouped


def test_reading_speed(benchmark, read_df):
    """Performance: measure how fast the grouping step runs."""
    @benchmark
    def run_pipeline():
        get_grouped(read_df)
