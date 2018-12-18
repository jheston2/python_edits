import os
import csv

df = []
EmpID = {}

#open csv
csvpath = os.path.join("employee_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # next(csvreader)
    for row in csvreader:
        # df.append(row)

        var = row[1].split()
        print(type(str(var[1:2])))
        print(str(var[1:2]))
        print(len(row[1].split()),row[1])
        
        # create dictionary
        EmpID[row[0]] = {
        
        #Last name not working
        'First Name': row[1].split()[0],
        'Last Name': row[1].split()[1:2],

        # 'DOB':row[2],
        # 'DOB': f"{row[2].split('-')[1]}adsf",

        'SSN':row[3],
        
        'State':row[3],
        
        }
        

    print(EmpID['232']['First Name'])
    print(EmpID['232']['Last Name'])
    # print(EmpID['232']['DOB'])