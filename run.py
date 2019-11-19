# Imports from 3rd party libraries
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import joblib

# Imports from this application
from app import app, server
from pages import index

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Who\'s That QB?',
    brand_href='/', 
    children=[
        #dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
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
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/cshields143/'), 
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


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    else:
        return dcc.Markdown('## Page not found')

# Generate prediction from input data
@app.callback(Output('final-result', 'children'),
              [Input('party-started', 'n_clicks')],
              [
                State('in-season', 'value'),
                State('in-game', 'value'),
                State('in-comps', 'value'),
                State('in-atts', 'value'),
                State('in-sacks', 'value'),
                State('in-carries', 'value'),
                State('in-pyds', 'value'),
                State('in-syds', 'value'),
                State('in-ryds', 'value'),
                State('in-ptds', 'value'),
                State('in-ints', 'value'),
                State('in-rtds', 'value'),
                State('in-fum', 'value')
              ])
def calc_pred(_, seas, game, cmps, att, sacks, carries, pyds, syds, ryds, ptds, ints, rtds, fums):
    if _ == None: return
    game_as_quint = (game + 1) // 5
    season_offset = (seas - 2004) * 5
    quint = game_as_quint + season_offset
    netatt = att + sacks
    netper = cmps / netatt
    netyds = pyds - syds
    nya = netyds / netatt
    ypc = ryds / carries
    tds = ptds + rtds
    tos = ints + fums
    pred = model.predict([[netper, netatt, netyds, nya, carries, ryds, ypc, tds, tos]])[0]
    return dbc.Col([
        dcc.Markdown(f'''
            - **Net Cmp%** {netper * 100:.2f}%
            - **Net Pass Attempts** {netatt}
            - **Net Pass Yards** {netyds}
            - **Net Yards / Attempt** {nya:.2f}
            - **Rush Attempts** {carries}
            - **Rush Yards** {ryds}
            - **Yards / Carry** {ypc:.2f}
            - **Touchdowns** {tds}
            - **Turnovers** {tos}
        '''),
        html.Div(pred, style={'font-size':'48px', 'font-weight':'bold', 'color':'red', 'text-transform':'uppercase'})
    ])

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    model = joblib.load('./rfc.pkl')
    app.run_server(debug=True)