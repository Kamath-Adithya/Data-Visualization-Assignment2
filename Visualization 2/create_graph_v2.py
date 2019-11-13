# create graph v2

import plotly.io as pio
import pandas as pd

df = pd.read_csv(r"C:\Users\Steven\Documents\School\Fall 2019\Data Viz\Project 2\Percent_Time\percent_score.csv",
                sep=',',
                names=["group", "participant", "percent", "score"])

colors = ['red', 'green', 'yellow', 'orange']

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df["percent"],
  y = df["score"],
  text = df["participant"],
  hovertemplate = 
        "<b>Participant: %{text}</b><br><br>" +
        "Percentage fixation: %{x}<br>" +
        "Score: %{y}<br>",
  opacity = 0.6,
  marker = dict(
        size = 15,
        line = dict(
            width = 2,
            color = 'black'
        )
  ),
  transforms = [
      dict(
        type = 'groupby',
        groups = df["group"],
        styles = [
        dict(target = 'gg', value = dict(marker = dict(color = 'red'))),
        dict(target = 'gt', value = dict(marker = dict(color = 'blue'))),
        dict(target = 'et', value = dict(marker = dict(color = 'green'))),
        dict(target = 'eg', value = dict(marker = dict(color = 'yellow')))
        ]
    )]
)]

layout = dict(
    title = '<b>Percent Fixation vs. Score</b>',
    yaxis = dict(
        title = 'Score',
        range = [0,1]
    ),
    xaxis = dict(
        title = 'Percent Fixation',
        range = [0,1],
        tickformat=".2%"
    )
)

fig_dict = dict(data=data, layout=layout)
pio.show(fig_dict, validate=False)