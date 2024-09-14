from main import *

example_csv = "stocks.csv"


def test_describe():
    """test describe"""
    describe_test = general_describe(example_csv)
    assert describe_test.shape == (8, 15)


def test_two_describes():
    """test with custom describe function"""
    describe_test = general_describe(example_csv)
    custom_test = custom_describe(example_csv, "XOM")
    assert describe_test.loc["mean", "XOM"] == custom_test["mean"]
    assert describe_test.loc["std", "XOM"] == custom_test["std"]


def test_summary_and_viz_to_markdown():
    """converts to markdown()"""
    save_to_markdown(example_csv)


if __name__ == "__main__":
    test_describe()
    test_two_describes()
    test_summary_and_viz_to_markdown()
