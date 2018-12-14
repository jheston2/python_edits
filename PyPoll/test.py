import os
import csv
import numpy as np

total_votes = int()
df = []
candidates = []
candidates_unique = []
cand0_count = int()
cand1_count = int()
cand2_count = int()
cand3_count = int()
votes = []
d={}
# create list df
csvpath = os.path.join("election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        df.append(row)
        if row[2] not in d.keys():
            d[row[2]]=1
        else:
            d[row[2]]+=1
print(d)
# # count all votes
#     for row in df:
#         total_votes += 1

# # create list of candidates
# candidates = [item[2] for item in df]

# # create list of unique candidates
# for x in candidates:
#     if x not in candidates_unique:
#         candidates_unique.append(x)

# #count votes for each candidate
# cand0_count = sum(1 for x in candidates if x == candidates_unique[0])
# cand1_count = sum(1 for x in candidates if x == candidates_unique[1])
# cand2_count = sum(1 for x in candidates if x == candidates_unique[2])
# cand3_count = sum(1 for x in candidates if x == candidates_unique[3])

# #create list of votes
# votes.append(cand0_count)
# votes.append(cand1_count)
# votes.append(cand2_count)
# votes.append(cand3_count)

# print(votes)
# print(candidates_unique[votes.index(max(votes))])



# print(votes_list)

# for k,v in votes_list:
#     if v == max(v):
#         print(k)

