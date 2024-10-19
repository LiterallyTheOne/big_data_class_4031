
import numpy as np 
import pandas as pd

data = pd.read_csv("data/nasdaq.csv",parse_dates=["Date"])

max_volume = data["Volume"].max()
min_volume = data["Volume"].min()


data_1 = data[data["Volume"] > min_volume * 1.1]

data_2 = data_1[data_1["Volume"] < max_volume * 0.9]

mid_close = data_2["Close"].median()

data_3 = data_2[data_2["Close"] > mid_close]

data_4 = data_3.copy()

data_4["Mid"] = (data_3["Close"] + data_3["Open"]) /2


data_5 = data_4[["Open","Close","Mid"]]

data_5.to_csv("result.csv")


