# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

from joblib import load
pipeline = load('assets/whowon.pkl')
print('Pipeline loaded!')
import pandas as pd

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Move the sliders around and determine who won this hypothetical game of DoTA.

            """
        ),
		html.H2('Who Won?'),
		html.Div(id='prediction-content', className='lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
		dcc.Markdown('#### Game Duration (seconds)'),
		daq.Slider(
			id='duration',
			max=4500,
			value=2500,
			min=500,
			step=1,
			marks={n: str(n) for n in range(500, 4600, 500)}
		),
		html.Br(),
		dcc.Markdown('#### Radiant Tower Status'),
		daq.Slider(
			id='radianttower',
			max=2047,
			value=1000,
			min=0,
			step=1,
			marks={n: str(n) for n in range(0, 2050, 250)}
		),
		html.Br(),
		dcc.Markdown('#### Dire Tower Status'),
		daq.Slider(
			id='diretower',
			max=2047,
			value=1000,
			min=0,
			step=1,
			marks={n: str(n) for n in range(0, 2050, 250)}
		),
		html.Br(),
		dcc.Markdown('#### Radiant Barracks Status'),
		daq.Slider(
			id='radiantbarracks',
			max=63,
			value=36,
			min=0,
			step=1,
			marks={n: str(n) for n in range(0, 65, 10)}
		),
		html.Br(),
		dcc.Markdown('#### Dire Barracks Status'),
		daq.Slider(
			id='direbarracks',
			max=63,
			value=36,
			min=0,
			step=1,
			marks={n: str(n) for n in range(0, 65, 10)}
		),
		html.Br(),
		dcc.Markdown('#### First Blood (seconds)'),
		daq.Slider(
			id='firstblood',
			max=400,
			value=110,
			min=0,
			step=1,
			marks={n: str(n) for n in range(0, 410, 50)}
		)
    ]
)

@app.callback(
	Output('prediction-content', 'children'),
	[Input('duration', 'value'),
	 Input('radianttower', 'value'),
	 Input('diretower', 'value'),
	 Input('radiantbarracks', 'value'),
	 Input('direbarracks', 'value'),
	 Input('firstblood', 'value')]
)
def predict(duration, tower_status_radiant, tower_status_dire, barracks_status_radiant, barracks_status_dire, first_blood_time):
	df = pd.DataFrame(columns=['duration', 'tower_status_radiant', 'tower_status_dire',
							   'barracks_status_radiant', 'barracks_status_dire', 'first_blood_time'],
					  data=[[duration, tower_status_radiant, tower_status_dire,
							 barracks_status_radiant, barracks_status_dire, first_blood_time]])
	y_pred = pipeline.predict(df)[0]
	confidence = pipeline.predict_proba(df)[0][0]
	return f'{"Radiant" if y_pred == True else "Dire"} won! {confidence * 100 : .3f}% confident.'


layout = dbc.Row([column1, column2])