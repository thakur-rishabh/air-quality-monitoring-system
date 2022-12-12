#!/usr/bin/env python3
from google.oauth2 import service_account
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from pandas.io import gbq
import os

# style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# gcp credential
credentials = service_account.Credentials.from_service_account_file('PUT_YOUT_SERVICE_USER_JSON')
project_id = 'class-project-312'

# Query
query = """
SELECT
  *
FROM
  `class-project-312.realTimeCO2.realTimeCO2-table`
LIMIT
  200
"""

# create df from big query
df = gbq.read_gbq(query, project_id=project_id, dialect='standard', credentials=credentials)

# css colurs
colors = {
    'background': '#d5e8f7',
    'text': '#000000'
}

# plotting
fig = px.line(df.sort_values(by=['timecollected', 'co2_ppm'], ascending=False), x="timecollected", y="co2_ppm")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='CO2 Level',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='CO2 level in yout home', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='co2_graph',
        figure=fig
    )
])

# main function
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
