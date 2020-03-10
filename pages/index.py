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
        
            ## Who Won?

            "Who Won?" is an app that predicts which team won a DoTA 2 game based on the final results of a game.
            """
        ),
        dcc.Link(dbc.Button('Who Won?', color='primary'), href='/predictions')
    ],
    md=12,
)

layout = dbc.Row([column1])