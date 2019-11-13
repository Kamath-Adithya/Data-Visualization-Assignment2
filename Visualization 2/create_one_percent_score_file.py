# create percent fixation and score graph

import csv
import pandas as pd
import plotly.io as pio
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

    # [participant, percent vis, score]

    data = []

    eg_data.pop(0)
    for row in eg_data:
        row.insert(0, 'eg')
        data.append(row)

    et_data.pop(0)
    for row in et_data:
        row.insert(0, 'et')
        data.append(row)

    gg_data.pop(0)
    for row in gg_data:
        row.insert(0, 'gg')
        data.append(row)

    gt_data.pop(0)
    for row in gt_data:
        row.insert(0, 'gt')
        data.append(row)

    print(data)

    with open(base_path + "percent_score.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter = ',')

        for line in data:
            writer.writerow(line)


main()