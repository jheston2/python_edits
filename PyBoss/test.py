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

# create lists
empID = [item[0] for item in df]

full_Name = [item[1] for item in df]
first_Name = [item.split()[0] for item in full_Name]
last_Name = [item.split()[1] for item in full_Name]

DOB1 = [item[2] for item in df]
DOB_Y = [item.split('-')[0] for item in DOB1]

DOB_M = [item.split('-')[1] for item in DOB1]

DOB_D = [item.split('-')[2] for item in DOB1]

# DOB2 = list(zip(DOB_M,DOB_D,DOB_Y))
# DOB3 = list((f"{DOB2[0]}/{DOB2[1]}/{DOB2[2]}" for x in DOB2))

print(DOB1[:10])

for x in DOB1:
    print(DOB1[:2])