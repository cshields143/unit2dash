# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

column1 = dbc.Col([
  html.H1('Can you beat Tom, Dick, & Harry?', style={'text-align':'center', 'font-weight':'bold', 'font-size':'2.5em', 'margin-bottom':'0.5em'}),
  html.P('Who here doesn\'t have fond memories of sitting with friends, looking up random statistics, and trying to guess the player who put up those numbers? Ah, to be young again...'),
  dcc.Markdown('Now the classic game can go on **forever** thanks to the power of machine learning! And with access to [this project\'s source code](https://github.com/cshields143/unit2dash), including Jupyter notebooks, you can experiment with your own models and combinations of strategies!'),
  html.H2('Gathering & Wrangling the Data', style={'text-align':'center', 'font-weight':'bold', 'font-size':'1.75em', 'margin':'1em'}),
  dcc.Markdown('Every QB game in the NFL from 2004 to 2019 (thru Week 11) was sourced from [Pro Football Reference](https://www.pro-football-reference.com/). Properly massaging this data proved crucial to success.'),
  html.P('For each quarterback in each game, the following stats were recorded:'),
  dbc.Row([
    dbc.Col(dcc.Markdown('''
    - Completions
    - Pass attempts
    - Passing yards
    - Passing touchdowns
    - Interceptions
    - Sacks
    - Sack yards
    ''')),
    dbc.Col(dcc.Markdown('''
    - Rush attempts
    - Rushing yards
    - Rushing touchdowns
    - Fumbles
    '''))
  ]),
  html.P('We want to be able to distinguish scrambling and dual-threat QBs like Aaron Rodgers or Cam Newton from pocket passers like Peyton Manning and Tom Brady--hence the rushing stats included amongst the more customary passing stats.'),
  html.P('At this point, in order to still cover different aspects of performance but also reduce the number of features our models would have to consider, the following "advanced" stats were computed:'),
  dcc.Markdown('''
    - total number of touches (pass attempts, rush attempts, & sacks)
    - completion percentage
    - net yards per pass attempt
    - yards per rush attempt
    - "rush split" (ratio of rushing yards to total yards)
    - touchdowns per touch & turnovers per touch
  '''),
  html.P('By comparing the changes in league average for each of these stats, we see that standardizing the data by year is also necessary:'),
  html.P(html.A(html.Img(src='../assets/overtime.png', width=700, style={'display':'block', 'margin':'0 auto'}), href='../assets/overtime.png')),
  html.P('We exclude postseason games so that some QBs aren\'t over-represented at the expense of others. We exclude any QBs with fewer than 100 games, more so that we have enough data to build a model out of than for any other reason (sorry, draft class of 18).'),
  html.P('This leaves us with 3,700 rows of data and 23 players:'),
  dbc.Row([
    dbc.Col(dcc.Markdown('''
      - Drew Brees
      - Eli Manning
      - Tom Brady
      - Philip Rivers
      - Ben Roethlisberger
      - Carson Palmer
      - Matt Ryan
      - Aaron Rodgers
      - Joe Flacco
      - Peyton Manning
      - Alex Smith
      - Jay Cutler
    ''')),
    dbc.Col(dcc.Markdown('''
      - Matthew Stafford
      - Ryan Fitzpatrick
      - Matt Hasselbeck
      - Tony Romo
      - Andy Dalton
      - Cam Newton
      - Russell Wilson
      - Matt Schaub
      - Michael Vick
      - Brett Favre
      - Matt Cassel
    '''))
  ]),
  html.H2('Tom: The Neophyte', style={'text-align':'center', 'font-weight':'bold', 'font-size':'1.75em', 'margin':'1em'}),
  dcc.Markdown('Tom doesn\'t know squat about football... except for one thing: *who\'s played the most games in this timeframe?* Tom figures he doesn\'t **have** to know squat about football; if he just guesses the player who represents the largest number of rows, he\'s bound to get some of them right.'),
  dcc.Markdown('This is called the **majority baseline**. As we can see from the following plot of class distributions, his favorite guesses are Drew Brees, Eli Manning, & Tom Brady:'),
  html.P(html.A(html.Img(src='../assets/class-dist.png', width=500, style={'display':'block', 'margin':'0 auto'}), href='../assets/class-dist.png')),
  html.P('The default evaluation metric for multiclass problems is called "subset accuracy": for every single game, did the model get it exactly right?  It\'s as harsh as it sounds, and our majority baseline only gets about 6% of them right (because, well, Drew Brees has played in about 6% of all qualified games).'),
  html.P('ROC/AUC is often more informative than subset accuracy, telling us how well our model makes distinctions instead of simply how accurate it is; Dick and Harry will use this metric to evaluate models instead.'),
  html.H2('Dick: The Casual Fan', style={'text-align':'center', 'font-weight':'bold', 'font-size':'1.75em', 'margin':'1em'}),
  dcc.Markdown('Dick enjoys football, and has been watching for these past 15 years. As he watches, he builds his own decision trees for classifying games--this is implemented with a **random forest ensemble** classifier.'),
  html.P('Randomized cross-validation searching was used to fine-tune the model, and the final results can be illustrated with a plot of the forest\'s feature importances:'),
  html.P(html.Img(src='../assets/rfc-fis.png', width=400, style={'display':'block', 'margin':'0 auto'})),
  html.P('100 decision trees were used in this ensemble model. While it may not be terribly informative, I still find it fascinating to follow these decision trees and watch the probabilities evolve. Here is one such tree:'),
  html.P(html.A(html.Img(src='../assets/rf-tree.png', width=600, style={'display':'block', 'margin':'0 auto'}), href='../assets/rf-tree.png')),
  html.P('"Wait, what was their NY/A? Yeah, typical Jay Cutler."'),
  html.P('The ROC/AUC score, a big fat 49% (with 50% representing no powers of distinction) left me wanting more. Enter Harry.'),
  html.H2('Harry: The Guy With Too Much Time On His Hands', style={'text-align':'center', 'font-weight':'bold', 'font-size':'1.75em', 'margin':'1em'}),
  dcc.Markdown('Harry doesn\'t just watch football, he maintains his own little garden of machine learning models. Using **logistic regression**, every QB gets their own individual model; these models evaluate each game on a **one-vs-all** basis. Instead of trying to guess between Russell Wilson, Jay Cutler, or Brett Favre, Harry instead asks each of his models, "Does this look like Russell Wilson or not? What about you, Jay Cutler or not-Jay Cutler?" And so on.'),
  html.P('The accuracy scores of the individual models can be found below, illustrating that some players have more distinctive play-styles:'),
  html.P(html.A(html.Img(src='../assets/ovr-lrs.png', width=500, style={'display':'block', 'margin':'0 auto'}), href='../assets/ovr-lrs.png')),
  html.P('When employed in concert, we have an ROC/AUC score of about 30%, which... I mean, I\'m moving the needle, okay? Multiclass is hard, and just being able to distinguish at all is a gift.'),
  html.H2('With An Eye To the Future', style={'text-align':'center', 'font-weight':'bold', 'font-size':'1.75em', 'margin':'1em'}),
  html.P('To my mind, the most interesting thing to fall out of this is the guessing game itself: We see that an arbitrary limitation in the possible answers introduces patterns in the predictive capabilities of the models.'),
  html.P('Could sampling thousands of rounds of our quessing game provide fodder for a new model? How accurate would such a model be? As the user is provided with each model\'s prediction before making their own, can such non-deterministic information be included among the fodder--could this also be used to improve performance?'),
  dcc.Markdown('At the risk of stating the obvious, I believe one thing to be certain: [topological data analysis](https://en.wikipedia.org/wiki/Topological_data_analysis) would be super helpful.')
], style={'max-width':'60em', 'margin':'0 auto'})

layout = dbc.Row([column1])