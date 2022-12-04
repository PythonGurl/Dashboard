import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, Input, Output, dcc, html
import read_data
import mapping

navbar = dbc.NavbarSimple(
    brand="PythonGurl",
    sticky="top",
    color="secondary",
    dark=True,
)


def get_layout():
    boroughs = mapping.borough_area()
    inventory_df = read_data.get_rental_inventory()
    inventory_graph = [
        dcc.Dropdown(sorted(boroughs.keys()),
                     placeholder='Select a borough', id='borough-dropdown'),
        dcc.Dropdown(id='areas-dropdown', placeholder='Areas'),
        dcc.Graph(id='area-inventory-line')
    ]
    inventory_sunburst = [
        dcc.Dropdown(sorted(set(inventory_df['date'].dt.year)), id='year-dropdown',
                     placeholder='Select a year'),
        dcc.Graph(id='area-inventory-sunburst')
    ]
    return html.Div([
        navbar,
        html.H2('Hello QQ'),
        dbc.Tabs(
            [
                dbc.Tab(inventory_graph, label='Rental Listings by Borough'),
                dbc.Tab(inventory_sunburst, label='Rental Listings by Year')
            ]
        ),
    ])
