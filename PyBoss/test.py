import os
import csv

df = []
first_Name = []

#create list df
csvpath = os.path.join("employee_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        df.append(row)

# create lists
empID = [item[0] for item in df]
full_Name = [item[1] for item in df]
first_Name = [item.split()[0] for item in full_Name]
print(first_Name[:10])
last_Name = [item.split()[1] for item in full_Name]
print(last_Name[:10])
