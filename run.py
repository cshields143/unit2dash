# Imports from 3rd party libraries
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import joblib
import pandas as pd

# Imports from this application
from app import app, server
from pages import index, manual

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Who\'s That QB?',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Manual', href='/manual', className='nav-link')), 
        #dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
        #dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')), 
    ],
    sticky='top',
    color='light', 
    light=True, 
    dark=False
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Christopher Shields', className='mr-2'), 
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:christopher.shields143@gmail.com'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/cshields143/unit2dash'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/chris-shields-827421194/') 
                ], 
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])

qbs = ['Drew Brees', 'Eli Manning', 'Tom Brady', 'Philip Rivers', 'Ben Roethlisberger',
       'Carson Palmer', 'Matt Ryan', 'Aaron Rodgers', 'Joe Flacco', 'Peyton Manning',
       'Alex Smith', 'Jay Cutler', 'Matthew Stafford', 'Ryan Fitzpatrick',
       'Matt Hasselbeck', 'Tony Romo', 'Andy Dalton', 'Cam Newton', 'Russell Wilson',
       'Matt Schaub', 'Michael Vick', 'Brett Favre', 'Matt Cassel']

model_maj = joblib.load('./majority.pkl')
list_maj = open('./byfreq.txt', 'r').read()
model_rfc = joblib.load('./randomforest.pkl')
league_norm = pd.read_csv('./years.txt').to_dict()
data = pd.read_csv('./z-scored.txt')
lr_models = {qb:joblib.load(f'./{qb.replace(" ","")}-lr.pkl') for qb in qbs}

def standardize(val, name, d, i):
    return (val - d[f'{name}-mean'][i]) / d[f'{name}-std'][i]

def ovr_lr(rows, models):
    probs = [models[qb].predict_proba(rows)[0][0] for qb in models]
    lbld = list(zip(models.keys(), probs))
    sums = sum([x[1] for x in lbld])
    divd = {x[0]:x[1]/sums for x in lbld}
    return divd

def get_scores(X, models):
    scores = ovr_lr(X, models)
    return scores

def get_highest(scores):
    maxi = max(scores.values())
    qb = [k for k in scores if scores[k] == maxi][0]
    return qb


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/manual':
        return manual.layout
    else:
        return dcc.Markdown('## Page not found')

# Pull random row from the data
@app.callback(Output('prompt-bucket', 'children'),
              [Input('trigger-game-round', 'n_clicks')])
def rand_row(_):
    row = data.sample().iloc[0];
    return dbc.Col([
        dbc.Row([
            html.Span(row['season'], id='season-prompt'),
            html.Span('season', style={'padding-left':'0.25em'})
        ], style={'font-style':'italic'}),
        dbc.Row([
            html.Span('Passing:', style={'font-weight':'bold', 'text-transform':'uppercase', 'margin-right':'0.5em'}),
            html.Span(row['completions'], id='completions-prompt'),
            html.Span('/', style={'font-weight':'bold', 'padding':'0 0.5em'}),
            html.Span(row['passatt'], id='passatt-prompt'),
            html.Span(row['passyards'], id='passyards-prompt', style={'padding':'0 1em'}),
            html.Span(row['passtds'], id='passtds-prompt'),
            html.Span(':', style={'font-weight':'bold', 'padding':'0 0.5em'}),
            html.Span(row['ints'], id='ints-prompt')
        ]),
        dbc.Row([
            html.Span('Rushing:', style={'font-weight':'bold', 'text-transform':'uppercase', 'margin-right':'0.5em'}),
            html.Span(row['rushatt'], id='rushatt-prompt'),
            html.Span('/', style={'font-weight':'bold', 'padding':'0 0.5em'}),
            html.Span(row['rushyards'], id='rushyards-prompt'),
            html.Span('/', style={'font-weight':'bold', 'padding':'0 0.5em'}),
            html.Span(row['rushtds'], id='rushtds-prompt')
        ]),
        dbc.Row([
            html.Span(row['sacks'], id='sacks-prompt'),
            html.Span('sack(s),', style={'padding':'0 0.5em 0 0.25em'}),
            html.Span(row['sackyards'], id='sackyards-prompt'),
            html.Span('yard(s) lost,', style={'padding':'0 0.5em 0 0.25em'}),
            html.Span(row['fumbles'], id='fumbles-prompt'),
            html.Span('fumble(s)', style={'padding-left':'0.25em'})
        ]),
        dbc.Row([
            html.Span('Answer:', style={'font-weight':'bold', 'padding-right':'0.5em'}),
            html.Span(row['player'], style={'width':'10em', 'background':'black', 'color':'black'})
        ])
    ])

# Generate prediction from input data
@app.callback(Output('manual-output', 'children'),
              [Input('trigger-manual-prediction', 'n_clicks')],
              [
                State('season-input', 'value'),
                State('completions-input', 'value'),
                State('passatt-input', 'value'),
                State('sacks-input', 'value'),
                State('rushatt-input', 'value'),
                State('passyards-input', 'value'),
                State('sackyards-input', 'value'),
                State('rushyards-input', 'value'),
                State('passtds-input', 'value'),
                State('ints-input', 'value'),
                State('rushtds-input', 'value'),
                State('fum-input', 'value')
              ])
def calc_pred(_, seas, cmps, att, sacks, carries, pyds, syds, ryds, ptds, ints, rtds, fums):
    if _ == None: return
    
    # "advanced" stats
    netatt = att + sacks
    netper = cmps / netatt
    netyds = pyds - syds
    nya = netyds / netatt
    ypc = ryds / carries
    tds = ptds + rtds
    tos = ints + fums
    touches = netatt + carries
    td_touch = tds / touches
    to_touch = tos / touches

    # standardize stats by league year
    def quick_stand(val, name):
        return standardize(val, name, league_norm, i)
    i = [k for k in league_norm['year'] if league_norm['year'][k] == seas][0]
    touch_z = quick_stand(touches, 'touches')
    netper_z = quick_stand(netper, 'net%')
    nya_z = quick_stand(nya, 'ny/a')
    ypc_z = quick_stand(ypc, 'ypc')
    td_touch_z = quick_stand(td_touch, 'td:touch')
    to_touch_z = quick_stand(to_touch, 'to:touch')

    # get predictions
    X = [[touch_z, netper_z, nya_z, ypc_z, td_touch_z, to_touch_z]]
    tom_pred = model_maj.predict(X)[0]
    dick_pred = model_rfc.predict(X)[0]
    harry_pred = get_highest(get_scores(X, lr_models))

    # construct output
    return dbc.Col([
      html.Div([
        html.Span('Tom:'),
        html.Span(' '),
        html.Span(tom_pred,
          id='tom-output',
          style={
            'color':'red'
          }
        )
      ], style={
        'font-size':'2.5em',
        'font-weight':'bold',
        'text-transform':'uppercase',
        'margin-bottom':'0.5em',
        'margin-top':'1em'
      }),
      html.Div([
        html.Span('Dick:'),
        html.Span(' '),
        html.Span(dick_pred,
          id='dick-output',
          style={
            'color':'green'
          }
        )
      ], style={
        'font-size':'2.5em',
        'font-weight':'bold',
        'text-transform':'uppercase',
        'margin-bottom':'0.5em'
      }),
      html.Div([
        html.Span('Harry:'),
        html.Span(' '),
        html.Span(harry_pred,
          id='harry-output',
          style={
            'color':'blue'
          }
        )
      ], style={
        'font-size':'2.5em',
        'font-weight':'bold',
        'text-transform':'uppercase',
        'margin-bottom':'0.5em'
      })
    ])

# Run app server: https://dash.plot.ly/getting-started

if __name__ == '__main__':
    app.run_server(debug=True)