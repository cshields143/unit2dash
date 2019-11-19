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
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predict the QB from the Game

            This app will probably not benefit you. But it *does* incorporate machine learning, so yeah.

            """
        ),
        dcc.Input(type='number', placeholder='SEASON'),
        dcc.Input(type='number', placeholder='GAME'),
        dcc.Input(type='number', placeholder='CMP'),
        dcc.Input(type='number', placeholder='ATT'),
        dcc.Input(type='number', placeholder='SACKS'),
        dcc.Input(type='number', placeholder='CARRIES'),
        dcc.Input(type='number', placeholder='PASS YDS'),
        dcc.Input(type='number', placeholder='SACK YDS'),
        dcc.Input(type='number', placeholder='RUSH YDS'),
        dcc.Input(type='number', placeholder='PASS TDS'),
        dcc.Input(type='number', placeholder='INTS'),
        dcc.Input(type='number', placeholder='RUSH TDS'),
        dcc.Input(type='number', placeholder='FUM'),
        html.Button('GUESS!', id='party-started')
        #dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    md=4,
)

#gapminder = px.data.gapminder()
#fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Div(id='final-result')
    ]
)

layout = dbc.Row([column1, column2])