import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, Input, Output, dcc, html
import read_data
import mapping

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

navbar = dbc.NavbarSimple(
    brand="PythonGurl",
    sticky="top",
    color="secondary",
    dark=True,
)


def get_layout():
    boroughs = mapping.borough_area()
    return html.Div([
        navbar,
        html.H2('Hello World'),
        dcc.Dropdown(sorted(boroughs.keys()), placeholder='Select a borough',
                     id='borough-dropdown'),
        dcc.Dropdown(id='areas-dropdown', placeholder='Areas'),
        dcc.Graph(id='area-inventory')
    ])


app.layout = get_layout()


@app.callback(Output('areas-dropdown', 'options'),
              Output('areas-dropdown', 'value'),
              Input('borough-dropdown', 'value'), prevent_initial_call=True
              )
def update_areas_dropdown(borough):
    boroughs = mapping.borough_area()
    val = False
    if borough:
        val = boroughs[borough][0]
    return boroughs[borough], val


@app.callback(Output('area-inventory', 'figure'),
              #   Input('borough-dropdown', 'value'),
              Input('areas-dropdown', 'value')
              )
def area_inventory_fig(area):
    inventory_df = read_data.get_rental_inventory()
    df = inventory_df[inventory_df["areaName"] == area]
    fig = px.line(df, x='date', y='value', labels={
                  'value': 'Inventory'}, title='Rental Inventory')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
