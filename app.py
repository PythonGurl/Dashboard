import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

navbar = dbc.NavbarSimple(
    brand="PythonGurl",
    sticky="top",
    color="#95A5A6",
)


app.layout = html.Div([
    navbar,
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
                 'LA',
                 id='dropdown'
                 ),
    html.Div(id='display-value')
])


@app.callback(Output('display-value', 'children'),
              [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)
