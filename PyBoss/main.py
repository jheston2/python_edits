import os
import csv

df = []

#create list df
csvpath = os.path.join("employee_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        df.append(row)

print(df)