# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from textwrap import dedent
# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(dedent("""
        
## Process

The first step was getting the data into a manageable form,
as my original data set was way too large,
with over 8 GB total data.

I ended up losing a lot of interesting information due to
not being able to actually matchup up any of the data with each other,
as I think the samples I used weren't actually part of a whole.

In the end, I just ended up choosing every
game with 10 players I had,
and measuring the six classes mentioned in Insights.

I used a pipeline with scikit-learn's SimpleImputer
and StandardScaler, followed by XGBoost's XGBClassifier.

```python

pipeline = make_pipeline(
    SimpleImputer(),
    StandardScaler(),
    XGBClassifier(max_depth=10,
                  learning_rate=0.2,
                  booster='gbtree',
                  gamma=0.01,
                  n_jobs=-1,
                  random_state=0,
                  early_stopping_rounds=50,
                  verbosity=3),
    verbose=True
)

```
            """
        )),

    ],
)

layout = dbc.Row([column1])