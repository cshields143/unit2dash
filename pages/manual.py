import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

yr_opts = [{'label':x, 'value':x} for x in range(2004,2020)]

inputform = dbc.Col([
  html.H2('Manually enter game stats'),
  dbc.Row([
    dcc.Dropdown(
      id='season-input',
      options=yr_opts,
      placeholder='Season',
      style={'width':'10em'}
    )
  ], style={
    'margin-bottom':'8px'
  }),
  dbc.Row([
    dcc.Input(
      id='completions-input',
      type='number',
      placeholder='CMP',
      style={
        'width':'5em'
      }
    ),
    html.Span('/', style={
      'font-weight':'bold',
      'font-size':'1.5em',
      'display':'inline-block',
      'text-align':'center',
      'width':'1em'
    }),
    dcc.Input(
      id='passatt-input',
      type='number',
      placeholder='ATT',
      style={
        'width':'5em'
      }
    ),
    html.Span(style={
      'font-size':'1.5em',
      'display':'inline-block',
      'width':'1em'
    }),
    dcc.Input(
      id='passyards-input',
      type='number',
      placeholder='P. YDS',
      style={
        'width':'5em'
      }
    ),
    html.Span(style={
      'font-size':'1.5em',
      'display':'inline-block',
      'width':'1em'
    }),
    dcc.Input(
      id='passtds-input',
      type='number',
      placeholder='P. TDS',
      style={
        'width':'5em'
      }
    ),
    html.Span(':', style={
      'font-size':'1.5em',
      'font-weight':'bold',
      'display':'inline-block',
      'text-align':'center',
      'width':'1em'
    }),
    dcc.Input(
      id='ints-input',
      type='number',
      placeholder='INTS',
      style={
        'width':'5em'
      }
    )
  ], style={
    'margin-bottom':'8px'
  }),
  dbc.Row([
    dcc.Input(
      id='rushatt-input',
      type='number',
      placeholder='R. ATT',
      style={
        'width':'5em'
      }
    ),
    html.Span(style={
      'font-size':'1.5em',
      'font-weight':'bold',
      'display':'inline-block',
      'text-align':'center',
      'width':'1em'
    }),
    dcc.Input(
      id='rushyards-input',
      type='number',
      placeholder='R. YDS',
      style={
        'width':'5em'
      }
    ),
    html.Span(style={
      'font-size':'1.5em',
      'font-weight':'bold',
      'display':'inline-block',
      'text-align':'center',
      'width':'1em'
    }),
    dcc.Input(
      id='rushtds-input',
      type='number',
      placeholder='R. TDS',
      style={
        'width':'5em'
      }
    ),
    html.Span(style={
      'font-size':'1.5em',
      'font-weight':'bold',
      'display':'inline-block',
      'text-align':'center',
      'width':'1em'
    }),
    dcc.Input(
      id='fum-input',
      type='number',
      placeholder='FUM',
      style={
        'width':'5em'
      }
    )
  ], style={
    'margin-bottom':'8px'
  }),
  dbc.Row([
    dcc.Input(
      id='sacks-input',
      type='number',
      placeholder='SCK',
      style={
        'width':'5em'
      }
    ),
    html.Span(style={
      'font-size':'1.5em',
      'font-weight':'bold',
      'display':'inline-block',
      'text-align':'center',
      'width':'1em'
    }),
    dcc.Input(
      id='sackyards-input',
      type='number',
      placeholder='S. YDS',
      style={
        'width':'5em'
      }
    ),
    html.Span(style={
      'font-size':'1.5em',
      'font-weight':'bold',
      'display':'inline-block',
      'text-align':'center',
      'width':'1em'
    }),
    html.Button('GUESSES >>', id='trigger-manual-prediction')
  ])
])

layout = dbc.Row([inputform, html.Div(id='manual-output')])