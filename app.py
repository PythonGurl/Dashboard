import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, Input, Output, dcc, html
import read_data
import mapping
import layout

app = Dash(__name__, title='New York City Rental Market',
           external_stylesheets=[dbc.themes.CYBORG])
server = app.server


app.layout = layout.get_layout()

# Callbacks ---------------------------------------------

## Rental Inverntory Line Chartn ##
# auto update area dropdowns based on selected borough


@app.callback(
    Output('areas-dropdown', 'options'),
    Output('areas-dropdown', 'value'),
    Input('borough-dropdown', 'value'), prevent_initial_call=True
)
def update_areas_dropdown(borough):
    boroughs = mapping.borough_area()
    val = False
    if borough:
        val = boroughs[borough][0]
    return boroughs[borough], val


@app.callback(
    Output('area-inventory-line', 'figure'),
    Input('areas-dropdown', 'value')
)
def area_inventory_line(area):
    inventory_df = read_data.get_rental_inventory()
    df = inventory_df[inventory_df['areaName'] == area]
    fig = px.line(df, x='date', y='value', labels={
                  'value': 'Inventory'}, title='Rental Inventory')
    return fig

## Sunburst Chart ##


@app.callback(
    Output('area-inventory-sunburst', 'figure'),
    Input('year-dropdown', 'value')
)
def area_inventory_sunburst(year):
    inventory_df = read_data.get_rental_inventory()
    df = inventory_df[(inventory_df['areaType'] != 'submarket')
                      & (inventory_df['areaType'] != 'borough')
                      & (inventory_df.date.dt.year == year)]
    fig = px.sunburst(df, path=['Borough', 'areaName'], values='value')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
