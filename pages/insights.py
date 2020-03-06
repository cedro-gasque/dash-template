# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import eli5
from eli5.sklearn import PermutationImportance

from joblib import load
permuter = load('assets/permuter.pkl')
print('Pipeline loaded!')
feature_names = ['duration', 'tower_status_radiant', 'tower_status_dire', 'barracks_status_radiant', 'barracks_status_dire', 'first_blood_time']
# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
			
			I ended up with an absurdly high accuracy for this model,
			but that's mostly due to the data points I ended up picking.
			
			I ended up choosing first blood time (when the first kill happened), duration of the game,
			the "status" of both teams' barracks and both teams' towers
			(I have no idea what these mean, so this project was 95% a bust).
			
			Here you can see the permutation importances:
            """
        ),
		html.Img(src='../assets/permutation_importances.png', className='img-fluid'),
		
    ],
)

layout = dbc.Row([column1])