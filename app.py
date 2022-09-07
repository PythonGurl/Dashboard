import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

navbar = dbc.NavbarSimple(
    brand="PythonGurl",
    sticky="top",
    color="secondary",
    dark=True,
)


app.layout = html.Div([
    navbar,
    html.H2('Hello World'),
    dcc.RadioItems(['New York City', 'Montreal', 'San Francisco'],
                   'Montreal', id='buttons'),
    html.Div(id='display-value')
])


@ app.callback(Output('display-value', 'children'),
               [Input('buttons', 'value')])
def display_value(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)
