
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
#column1 = dbc.Col(
#    [
#        dcc.Markdown(
#            """
#        
#            ## Predict the QB from the Game
#
#            This app will probably not benefit you. But it *does* incorporate machine learning, so yeah.
#
#            """
#        ),
#        dcc.Input(type='number', placeholder='SEASON', id="in-season"),
#        dcc.Input(type='number', placeholder='GAME', id="in-game"),
#        dcc.Input(type='number', placeholder='CMP', id="in-comps"),
#        dcc.Input(type='number', placeholder='ATT', id='in-atts'),
#        dcc.Input(type='number', placeholder='SACKS', id='in-sacks'),
#        dcc.Input(type='number', placeholder='CARRIES', id='in-carries'),
#        dcc.Input(type='number', placeholder='PASS YDS', id='in-pyds'),
#        dcc.Input(type='number', placeholder='SACK YDS', id='in-syds'),
#        dcc.Input(type='number', placeholder='RUSH YDS', id='in-ryds'),
#        dcc.Input(type='number', placeholder='PASS TDS', id='in-ptds'),
#        dcc.Input(type='number', placeholder='INTS', id='in-ints'),
#        dcc.Input(type='number', placeholder='RUSH TDS', id='in-rtds'),
#        dcc.Input(type='number', placeholder='FUM', id='in-fum'),
#        html.Button('GUESS!', id='party-started')
#    ],
#    md=4,
#)

#gapminder = px.data.gapminder()
#fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#           hover_name="country", log_x=True, size_max=60)

#column2 = dbc.Col(
#    [
#        html.Div(id='final-result')
#    ]
#)

#layout = dbc.Row([column1, column2])

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
        ])
    ])
])