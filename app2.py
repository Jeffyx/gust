import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd 

df = pd.DataFrame({"Type" : ["Housing", "Car", "Bills"], "Cost" : [0,0,0]})
print(df)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),),
    dcc.Input(id='my-id', value='initial value', type='number'), #type='text'
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered for your Housing "{}"'.format(input_value)

@app.callback(
    Output(component_id='table', component_property='data'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return(df.loc[(df["Type"] == "Housing"), "Cost"] = input_value)

if __name__ == '__main__':
    app.run_server(debug=True)