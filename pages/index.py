
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

layout = dbc.Col([
    html.Button('Guess the QB!', id='trigger-game-round', style={'font-size':'2em','font-weight':'bold', 'text-transform':'uppercase', 'width':'10em', 'display':'block', 'margin':'0 auto'}),
    html.Div(id='prompt-bucket', style={'font-size':'1.5em', 'width':'18em', 'margin':'1.5em auto'}),
    dbc.Row([
        dbc.Col([
            html.Button('Forget', id='trigger-score-clear', style={'margin-bottom':'0.5em'}),
            html.Table([
                html.Thead([
                    html.Tr([
                        html.Th('Player', style={'padding':'0.25em 0.5em'}),
                        html.Th('Score', style={'padding':'0.25em 0.5em'})
                    ])
                ], style={'background':'#ddd', 'border-bottom':'1px solid #666'}),
                html.Tbody(id='score-output', style={'text-align':'center'})
            ])
        ]),
        dbc.Col(id='options-output', style={'font-size':'1.5em', 'text-align':'center'}),
        dbc.Col(id='guess-outputs', style={'font-size':'1.5em', 'text-transform':'uppercase', 'font-weight':'bold'})
    ])
])