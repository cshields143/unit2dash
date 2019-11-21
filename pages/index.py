
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
    html.H1('Guess the QB!', style={'text-transform':'uppercase'}),
    dbc.Row([
        html.Span('??', id='season-prompt'),
        html.Span('season', style={'padding-left':'0.25em'})
    ], style={'font-size':'1.5em', 'width':'15em', 'margin':'0 auto'}),
    dbc.Row([
        html.Span('Passing:', style={'font-weight':'bold', 'text-transform':'uppercase', 'margin-right':'0.5em'}),
        html.Span('??', id='completions-prompt'),
        html.Span('/', style={'font-weight':'bold', 'padding':'0 0.5em'}),
        html.Span('??', id='passatt-prompt'),
        html.Span('??', id='passyards-prompt', style={'padding':'0 1em'}),
        html.Span('??', id='passtds-prompt'),
        html.Span(':', style={'font-weight':'bold', 'padding':'0 0.5em'}),
        html.Span('??', id='ints-prompt')
    ], style={'font-size':'1.5em', 'width':'15em', 'margin':'0 auto'}),
    dbc.Row([
        html.Span('Rushing:', style={'font-weight':'bold', 'text-transform':'uppercase', 'margin-right':'0.5em'}),
        html.Span('??', id='rushatt-prompt'),
        html.Span('/', style={'font-weight':'bold', 'padding':'0 0.5em'}),
        html.Span('??', id='rushyards-prompt'),
        html.Span('/', style={'font-weight':'bold', 'padding':'0 0.5em'}),
        html.Span('??', id='rushtds-prompt')
    ], style={'font-size':'1.5em', 'width':'15em', 'margin':'0 auto'}),
    dbc.Row([
        html.Span('??', id='sacks-prompt'),
        html.Span('sacks,', style={'padding':'0 0.5em 0 0.25em'}),
        html.Span('??', id='sackyards-prompt'),
        html.Span('yards lost,', style={'padding':'0 0.5em 0 0.25em'}),
        html.Span('??', id='fumbles-prompt'),
        html.Span('fumbles', style={'padding-left':'0.25em'})
    ], style={'font-size':'1.5em', 'width':'17em', 'margin':'0 auto'})
], style={'text-align':'center'})