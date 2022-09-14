from statistics import median
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
import mapping

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

navbar = dbc.NavbarSimple(
    brand="PythonGurl",
    sticky="top",
    color="secondary",
    dark=True,
)

boroughs = mapping.borough_area()


app.layout = html.Div([
    navbar,
    html.H2('Hello World'),
    dcc.Dropdown(sorted(boroughs.keys()), placeholder='Select a borough',
                 id='borough-dropdown'),
    dcc.Dropdown(id='areas-dropdown', placeholder='Areas')
])


@ app.callback(Output('areas-dropdown', 'options'),
               Output('areas-dropdown', 'value'),
               Input('borough-dropdown', 'value'), prevent_initial_call=True
               )
def update_areas_dropdown(borough):
    val = False
    if borough:
        val = boroughs[borough][0]
    return boroughs[borough], val


if __name__ == '__main__':
    app.run_server(debug=True)
