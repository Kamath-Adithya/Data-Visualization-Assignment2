# create percent fixation and score graph

import csv
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os.path

def main():
    base_path = os.path.dirname(os.path.realpath(__file__)) + r"\Percent_Time\\"
    with open(base_path + "percent_scores_eg.csv", mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        eg_data = list(reader)

    with open(base_path + "percent_scores_et.csv", mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        et_data = list(reader)

    with open(base_path + "percent_scores_gg.csv", mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        gg_data = list(reader)

    with open(base_path + "percent_scores_gt.csv", mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        gt_data = list(reader)

    eg_x = []
    eg_y = []
    et_x = []
    et_y = []
    gg_x = []
    gg_y = []
    gt_x = []
    gt_y = []

    # x = percent fixation
    # y = score

    eg_data.pop(0)
    for row in eg_data:
        eg_x.append(row[1])
        eg_y.append(row[2])
    
    et_data.pop(0)
    for row in et_data:
        et_x.append(row[1])
        et_y.append(row[2])

    gg_data.pop(0)
    for row in gg_data:
        gg_x.append(row[1])
        gg_y.append(row[2])
    
    gt_data.pop(0)
    for row in gt_data:
        gt_x.append(row[1])
        gt_y.append(row[2])


    fig = make_subplots(rows = 2, cols = 2, 
                        subplot_titles=("Expert Graph", "Expert Tree", "General Graph", "General Tree"))
    
    fig.add_trace(
    go.Scatter(
        x=eg_x, 
        y=eg_y,
        mode="markers"),
    row=1, col=1
    )

    fig.add_trace(
    go.Scatter(
        x=et_x,
        y=et_y,
        mode="markers"),
    row=1, col=2
    )

    fig.add_trace(
    go.Scatter(
        x=gg_x, 
        y=gg_y,
        mode="markers"),
    row=2, col=1
    )

    fig.add_trace(
    go.Scatter(
        x=gt_x, 
        y=gt_y,
        mode="markers"),
    row=2, col=2
    )

    # Update xaxis properties
    fig.update_xaxes(title_text="Percent Fixation", row=1, col=1)
    fig.update_xaxes(title_text="Percent Fixation", row=1, col=2)
    fig.update_xaxes(title_text="Percent Fixation", row=2, col=1)
    fig.update_xaxes(title_text="Percent Fixation", row=2, col=2)

    # Update yaxis properties
    fig.update_yaxes(title_text="Score", range=[0, 1], row=1, col=1)
    fig.update_yaxes(title_text="Score", range=[0, 1], row=1, col=2)
    fig.update_yaxes(title_text="Score", range=[0, 1], row=2, col=1)
    fig.update_yaxes(title_text="Score", range=[0, 1], row=2, col=2)

    fig.update_layout(height=600, width=800, title_text="Subplots")

    fig.show()




main()