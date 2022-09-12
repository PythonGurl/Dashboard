import pandas as pd
import collections


def borough_area():
    df = pd.read_csv('RentData051022/medianAskingRent_All.csv')
    df.dropna()
    d = collections.defaultdict(list)
    for row in range(df.shape[0]):
        k = df.at[row, 'Borough']
        v = df.at[row, 'areaName']
        d[k].append(v)
    return d


if __name__ == "__main__":
    d = borough_area()
    print(d)
