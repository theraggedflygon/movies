import pandas as pd
import calplot
import csv
import matplotlib.pyplot as plt

days = pd.date_range('1/1/2020', '12/31/2022', freq='D')
counts = [0 for i in range(len(days))]

with open("data/heatmap_data.csv", 'r', encoding="windows-1252") as file:
    reader = csv.reader(file)
    date_idx = None
    title_idx = None
    current_date = None
    ctr = 0
    for idx, line in enumerate(reader):
        if idx == 0:
            date_idx = line.index("Date")
            title_idx = line.index("Movie Watched")
            continue
        if current_date is None:
            current_date = line[date_idx]
        elif current_date != line[date_idx]:
            ctr += 1
            current_date = line[date_idx]
        if line[title_idx] != "":
            counts[ctr] += 1


days = pd.date_range('1/1/2020', '12/31/2022', freq='D')

events = pd.Series(counts, index=days)
fig, axes = calplot.calplot(events, cmap='YlGn')
fig.savefig("heatmap.png", bbox_inches="tight")
