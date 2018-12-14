import os
import csv

csvpath = os.path.join("budget_data.csv")
count = int()
profitloss = int()
net = int()
df = []
profit = []
diffs = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # for row in csvreader:
    #     print(row)

    next(csvreader)
    for row in csvreader:
        #count months
        count += 1
        
        #sum profit/loss
        profitloss = int(row[1])
        net += profitloss 
        
        #list of profits/loss
        df.append(row)
        profit.append(row[1])

    prev = profit[0]
    for row in profit:
        if prev == row:
            continue
        else:
            diffs.append(int(row)-int(prev))
            prev = int(row)

    print(f"Total Months: {count}")
    print(f"Total Profit/Losses: ${net}")
    print(f"Average Change: ${round(sum(diffs)/len(diffs),2)}")
    print(f"Greatest Increase in Profits: {df[diffs.index(max(diffs))+1][0]} (${max(diffs)})")
    print(f"Greatest Decrease in Profits: {df[diffs.index(min(diffs))+1][0]} (${min(diffs)})")