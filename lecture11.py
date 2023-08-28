from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_daq as daq

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Interactive Demo" 

df = pd.read_csv('https://raw.githubusercontent.com/wenjiun/MCM7003DualInputCallbackDemo/main/cpi_headline.csv')

app.layout = html.Div(
    [html.H1("Data Visualization"),
    dcc.Dropdown(['overall', 'food_beverage', 'alcohol_tobacco',
       'clothing_footwear', 'housing_utilities', 'furnishings', 'health',
       'transport', 'communication', 'recreation_culture', 'education',
       'hospitality', 'misc'], 'overall', id='my-dropdown'),
    daq.ColorPicker(
        id='my-color-picker',
        label='Color Picker',
        value=dict(hex='#119DFF')
    ),
    dcc.Graph(id='graph-output', figure ={})]
)


@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Input(component_id='my-dropdown', component_property='value'),
    Input(component_id='my-color-picker', component_property='value')
)

def update_my_graph(dropdown_chosen, color_chosen):
    fig = px.line(df, x='date', y=dropdown_chosen, title=dropdown_chosen).update_layout(xaxis_title="Date", yaxis_title="Index")
    fig.update_traces(line_color=color_chosen['hex'])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
