import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'GUST'

server = app.server

app.layout = html.Div(children=[
    html.H1(children='Get Ur Sh!t Together'),
    #How much you spend on Rent?
    html.Div(children='''
        How much you spend on Rent?
    '''),
    dcc.Input(
        id='num_rent',
        type='number',
        value=0
    ),
        #How much you spend on car?
    html.Div(children='''
        How much you spend on Car?
    '''),
    dcc.Input(
        id='num_car',
        type='number',
        value=0
    ),
            #How much you spend on Bills (Internet, phone, Nexflix)?
    html.Div(children='''
        How much you spend on Bills? (Internet, phone, Nexflix)
    '''),
    dcc.Input(
        id='num_bills',
        type='number',
        value=0
    ),
                #How much you spend on Bills (Internet, phone, Nexflix)?
    html.Div(children='''
        How much you spend on Food? (Average American spends $300 a month)
    '''),
    dcc.Input(
        id='num_food',
        type='number',
        value=0
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ["Rent", "Car", "Bills", "Food"], 'y': [0, 0, 0, 0], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.Div(children='''
    Whats your income each month?
'''),
    dcc.Input(
        id='income',
        type='number',
        value=0
    ),
    html.Div(id='the_break_down')
        #value=0)
])

#Updates the graph
@app.callback(
    Output('example-graph', 'figure'),
    [Input('num_rent', 'value'),
    Input('num_car', 'value'),
    Input('num_bills', 'value'),
    Input('num_food', 'value')])
def update_graph(num_rent, num_car, num_bills, num_food):
    return {
            'data': [
                {'x': ["Rent", "Car", "Bills", "Food"], 'y': [num_rent, num_car, num_bills, num_food], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
    }

@app.callback(
    Output(component_id='the_break_down', component_property='children'),
    [Input('income', 'value'),
    Input('num_rent', 'value'),
    Input('num_car', 'value'),
    Input('num_bills', 'value'),
    Input('num_food', 'value')])
def break_down(income, num_rent, num_car, num_bills, num_food):
    debt = num_rent + num_car + num_bills + num_food

    profit = income - debt
    return 'You spend ' + str(debt) + ' each month! That Leaves you with ' + str(profit)

if __name__ == '__main__':
    app.run_server(debug=True)