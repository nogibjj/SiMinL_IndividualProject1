"""Main function"""

from mylib.lib import *


def general_describe(csv):
    """general describe"""
    general_df = load_and_preprocess(csv)
    return general_df.describe()


def custom_describe(csv, col):
    """custom describe"""
    general_df = load_and_preprocess(csv)
    describe_dict = {
        "name": col,
        "mean": process_mean(general_df, col),
        "std": process_std(general_df, col),
        "median": process_median(general_df, col),
    }
    return describe_dict


def general_viz_combined(general_df, jupyter_render):
    """saves all the figures at once"""
    build_chart(general_df, jupyter_render)
    rolling_average(general_df, jupyter_render)


def save_to_markdown(csv):
    """save summary report to markdown"""
    general_df = load_and_preprocess(csv)
    describe_df = general_describe(csv)
    markdown_table1 = describe_df.to_markdown()
    general_viz_combined(general_df, False)
    # Write the markdown table to a file
    with open("stocks.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![MeanvsRisk](returnvsrisk.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![RollingAveXOM](rollingaverage.png)\n")
