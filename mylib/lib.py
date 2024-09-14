import pandas as pd
import matplotlib.pyplot as plt


# Data Loading and Preprocessing:
def load_and_preprocess(csv):
    """loads the data"""
    general_df = pd.read_csv(csv)
    return general_df


# Data Operations
def process_mean(general_df, col):
    """returns the mean of a specific col in dataframe"""
    general_mean = general_df[col].mean()
    return general_mean


def process_median(general_df, col):
    """returns the median of a specific col in dataframe"""
    general_median = general_df[col].median()
    return general_median


def process_std(general_df, col):
    """returns the std of a specific col in dataframe"""
    general_std = general_df[col].std()
    return general_std


# Charts: mean return vs risk
def build_chart(general_df, jupyter_render):
    "visualisation of mean return vs risk"
    # data_frame = pd.read_csv(csv)
    ror = general_df.pct_change() * 100
    mean = ror.mean()
    standard_deviation = ror.std()
    plt.scatter(standard_deviation, mean, s=general_df.mean(), alpha=0.4)
    plt.title("Mean Return vs Risk", fontsize=10, fontweight="bold")
    plt.xlabel("Risk (standard deviation)", fontsize=10)
    plt.ylabel("Mean Return", fontsize=10)
    plt.grid()
    if not jupyter_render:
        plt.savefig("returnvsrisk.png")
    else:
        plt.show()
    plt.savefig("returnvsrisk.png")


# 5 day rolling average
def rolling_average(general_df, jupyter_render):
    """line chart"""
    # general_df = pd.read_csv(general_df)
    name = "XOM"
    n = len(general_df)
    xdata = range(1, n + 1)
    plt.figure(figsize=(6, 4))
    plt.plot(
        xdata,
        general_df[name],
        linewidth=1,
        color="b",
        alpha=0.8,
        label="Daily Price Trend",
    )
    days = [5, 25, 40, 60, 90, 120]
    for k in days:
        ma = general_df.rolling(k).mean()
        plt.plot(xdata, ma[name], linewidth=1, label="{0}-day moving avg.".format(k))
    plt.title(
        "Moving Average Stock Price for {}".format(name), fontsize=10, fontweight="bold"
    )
    plt.xlabel("Day", fontsize=10)
    plt.ylabel("Price", fontsize=10)
    plt.legend()
    plt.grid()
    if not jupyter_render:
        plt.savefig("rollingaverage.png")
    else:
        plt.show()
