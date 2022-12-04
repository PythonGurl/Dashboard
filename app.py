import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
from view import get_layout
from controller import get_callbacks

app = Dash(__name__, title='New York City Rental Market',
           external_stylesheets=[dbc.themes.CYBORG])
server = app.server


app.layout = get_layout()
get_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
