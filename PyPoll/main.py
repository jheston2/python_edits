import os
import csv

total_votes = int()
df = []
candidates = []
candidates_unique = []
cand0_count = int()
cand1_count = int()
cand2_count = int()
cand3_count = int()
winner = str()
votes = []

#create list df
csvpath = os.path.join("election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        df.append(row)

# count all votes
    for row in df:
        total_votes += 1

# create list of candidates
candidates = [item[2] for item in df]

# create list of unique candidates
for x in candidates:
    if x not in candidates_unique:
        candidates_unique.append(x)

#count votes for each candidate
cand0_count = sum(1 for x in candidates if x == candidates_unique[0])
cand1_count = sum(1 for x in candidates if x == candidates_unique[1])
cand2_count = sum(1 for x in candidates if x == candidates_unique[2])
cand3_count = sum(1 for x in candidates if x == candidates_unique[3])

#create list of votes, determine winner
votes.append(cand0_count)
votes.append(cand1_count)
votes.append(cand2_count)
votes.append(cand3_count)
winner = candidates_unique[votes.index(max(votes))]

#print
print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------")
print(f"{candidates_unique[0]}: {round(cand0_count/total_votes,4)*100}% ({cand0_count})")
print(f"{candidates_unique[1]}: {round(cand1_count/total_votes,4)*100}% ({cand1_count})")
print(f"{candidates_unique[2]}: {round(cand2_count/total_votes,4)*100}% ({cand2_count})")
print(f"{candidates_unique[3]}: {round(cand3_count/total_votes,4)*100}% ({cand3_count})")
print(f"----------------------")
print(f"Winner: {winner}")
print(f"----------------------")

#export results to text file
file = open("results.txt","w")
file.write(f"Election Results \n")
file.write(f"----------------------\n")
file.write(f"Total Votes: {total_votes}\n")
file.write(f"----------------------\n")
file.write(f"{candidates_unique[0]}: {round(cand0_count/total_votes,4)*100}% ({cand0_count})\n")
file.write(f"{candidates_unique[1]}: {round(cand1_count/total_votes,4)*100}% ({cand1_count})\n")
file.write(f"{candidates_unique[2]}: {round(cand2_count/total_votes,4)*100}% ({cand2_count})\n")
file.write(f"{candidates_unique[3]}: {round(cand3_count/total_votes,4)*100}% ({cand3_count})\n")
file.write(f"----------------------\n")
file.write(f"Winner: {winner}\n")
file.write(f"----------------------\n")