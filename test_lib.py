"""
Test goes here

"""

from mylib.lib import *

example_csv = "stocks.csv"


def test_load_and_preprocess():
    """test that loading the csv will work"""
    general_df = load_and_preprocess(example_csv)
    assert general_df is not None
    assert general_df.shape == (252, 15)


def test_stats():
    """test that checks the data operations is working"""
    general_df = load_and_preprocess(example_csv)
    mean_test = process_mean(general_df, "XOM")
    median_test = process_median(general_df, "XOM")
    std_test = process_std(general_df, "XOM")
    describe_test = general_df.describe()
    assert describe_test.loc["mean", "XOM"] == mean_test
    assert describe_test.loc["std", "XOM"] == std_test
    # assert median_test == 53.0


if __name__ == "__main__":
    test_load_and_preprocess()
    test_stats()
