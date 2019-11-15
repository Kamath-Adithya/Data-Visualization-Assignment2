import pandas as pd
import numpy as np
import chart_studio.plotly as ptly
import plotly.graph_objects as go

#reading csv files
eg = pd.read_csv('eg.csv', sep=',')
et = pd.read_csv('et.csv', sep=',')
gg = pd.read_csv('gg.csv', sep=',')
gt = pd.read_csv('gt.csv', sep=',')

#calculate average of percentage fixation
percentageFixation_averageEg = np.average(eg['percentage']*100)
percentageFixation_averageEt = np.average(et['percentage']*100)
percentageFixation_averageGg = np.average(gg['percentage']*100)
percentageFixation_averageGt = np.average(gt['percentage']*100)

tabX=[]
tabAvPercFixEg=[]
tabAvPercFixEt=[]
tabAvPercFixGg=[]
tabAvPercFixGt=[]

#put the average of each type of visualization into a table
for i in range(-1,17):
    val1=percentageFixation_averageEg
    val2=percentageFixation_averageEt
    val3=percentageFixation_averageGg
    val4=percentageFixation_averageGt
    tabAvPercFixEg.append(val1)
    tabAvPercFixEt.append(val2)
    tabAvPercFixGg.append(val3)
    tabAvPercFixGt.append(val4)
    tabX.append(i+1)

#Creating the graph
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}

fig_dict["layout"] = {"title" : "<b>Percent fixation per participant</b>"}
fig_dict["layout"]["xaxis"] = {"range": [0, 17], "title": "Participants"}
fig_dict["layout"]["yaxis"] = {"range": [0,100], "title": "Percentage Fixation %"}

#make data
data_dict1 = {
    "x": list(gt['num']),
    "y": list(gt['percentage']*100),
    "mode": "markers",
    "marker": {
        "sizemode": "area",
        "sizeref": 0,
        "size": 7,
        "symbol": 0,
        "opacity":0.5,
        "color":"red"
      },
    "hovertemplate" :
        "<b>Participant: %{x}</b><br><br>" +
        "Percentage fixation: %{y}%<br>",
    "name": "general tree"
    }
fig_dict["data"].append(data_dict1)

data_dict2 = {
    "x": list(et['num']),
    "y": list(et['percentage']*100),
    "mode": "markers",
    "marker": {
        "sizemode": "area",
        "sizeref": 0,
        "size": 7,
        "symbol": 0,
        "opacity":1,
        "color":"orange"
      },
    "hovertemplate" :
        "<b>Participant: %{x}</b><br><br>" +
        "Percentage fixation: %{y}%<br>",
    "name": "expert tree"
    }
fig_dict["data"].append(data_dict2)

data_dict3 = {
    "x": list(gg['num']),
    "y": list(gg['percentage']*100),
    "mode": "markers",
    "marker": {
        "sizemode": "area",
        "sizeref": 0,
        "size": 7,
        "symbol": 0,
        "opacity":0.5,
        "color":"royalblue"
      },
    "hovertemplate" :
        "<b>Participant: %{x}</b><br><br>" +
        "Percentage fixation: %{y}%<br>",
    "name": "general graph"
    }
fig_dict["data"].append(data_dict3)

data_dict4 = {
    "x": list(eg['num']),
    "y": list(eg['percentage']*100),
    "mode": "markers",
    "marker": {
        "sizemode": "area",
        "sizeref": 0,
        "size": 7,
        "symbol": 0,
        "opacity":0.5,
        "color":"green"
      },
    "hovertemplate" :
        "<b>Participant: %{x}</b><br><br>" +
        "Percentage fixation: %{y}%<br>",
    "name": "expert graph"
    }
fig_dict["data"].append(data_dict4)

#drawing the traces
fig = go.Figure(fig_dict)

fig.add_trace(go.Scatter(x=tabX, y=tabAvPercFixEg, name='Average Percentage Fixation EG', mode='lines',
                         line=dict(color='green', width=2)))
fig.add_trace(go.Scatter(x=tabX, y=tabAvPercFixEt, name='Average Percentage Fixation ET', mode='lines',
                         line=dict(color='orange', width=2)))
fig.add_trace(go.Scatter(x=tabX, y=tabAvPercFixGg, name='Average Percentage Fixation GG', mode='lines',
                         line=dict(color='royalblue', width=2)))
fig.add_trace(go.Scatter(x=tabX, y=tabAvPercFixGt, name='Average Percentage Fixation GT', mode='lines',
                         line=dict(color='red', width=2)))

fig.show()
