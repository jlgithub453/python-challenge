import os
import csv

election_csv = os.path.join("election_data.csv")

with open(election_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    number_votes=0
    candidate=""
    candidate_list=[]
    votes_won=1
    candidate_votes=[]
    for row in csvreader:
        number_votes+=1
        if row[2]!=candidate:
            candidate=row[2]
            candidate_list.append(candidate)
            candidate_votes.append(votes_won)
            votes_won=1
        else:
            votes_won+=1

candidate_votes.append(votes_won)
candidate_votes.remove(candidate_votes[0])

max_votes=0
winner=""
number_candidate=len(candidate_list)
for i in range(number_candidate):
    if candidate_votes[i]>=max_votes:
       max_votes=candidate_votes[i]
       winner=candidate_list[i]
percentage=[int(candidate/number_votes*100) for candidate in candidate_votes]

print("Election Results")
print("--------------------")
print("Total Votes: "+str(number_votes))
print("--------------------")
for i in range(number_candidate):
    print(candidate_list[i]+":"+str(percentage[i])+"%"+"("+str(candidate_votes[i])+")")
print("--------------------")
print("Winner: "+winner)
