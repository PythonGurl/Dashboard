import pandas as pd
import plotly.express as px


def _normalize(df):
    df = df.melt(
        id_vars=["areaName", "Borough", "areaType"],
        value_vars=list(df.columns[3:]),
        var_name='date',
        value_name='value',
    )
    df["date"] = pd.to_datetime(df["date"])
    return df


def get_rental_inventory():
    df = pd.read_csv('RentData051022/rentalInventory_All.csv')
    df = df.dropna()
    return _normalize(df)


if __name__ == '__main__':
    d = get_rental_inventory()
    df = d[d.areaName == 'Sunnyside']
    print(df.head())
    fig = px.line(df, x='date', y='value')
    fig.show()
