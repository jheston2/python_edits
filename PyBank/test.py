import os
import csv
import pandas as pd

csvpath = os.path.join("budget_data.csv")
count = int()
profitloss = float()
net = float()
df = []
profit = []
diffs= []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        df.append(row)
        profit.append(row[1])
    
    prev = profit[0]
    for row in profit:
        if prev == row:
            continue
        else:
            diffs.append(int(row)-int(prev))
            prev = int(row)

print(diffs.index(max(diffs)))
print(diffs[24])
print(df[25][0])

print(f"Greatest Increase in Profits: {df[diffs.index(max(diffs))+1][0]} (${max(diffs)})")
print(f"Greatest Increase in Profits: {df[diffs.index(min(diffs))+1][0]} (${min(diffs)})")