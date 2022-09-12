import collections
import pandas as pd


def borough_area():
    df = pd.read_csv('RentData051022/medianAskingRent_All.csv')
    df = df.dropna()
    d = collections.defaultdict(list)
    for row in df.index:
        k = df.at[row, 'Borough']
        v = df.at[row, 'areaName']
        d[k].append(v)
    return d


if __name__ == "__main__":
    d = borough_area()
    print(d)
