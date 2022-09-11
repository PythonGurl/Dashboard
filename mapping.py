import pandas as pd
import collections

df = pd.read_csv('RentData051022/medianAskingRent_All.csv')
print(df.shape)


def borough_area(df, key, val):
    d = collections.defaultdict(list)
    for row in range(df.shape[0]):
        k = df.at[row, key]
        v = df.at[row, val]
        d[k].append(v)
    return d


d = borough_area(df, 'Borough', 'areaName')
print(d)
