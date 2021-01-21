#imports modules
import os
import csv
from collections import Counter

#initialize variables
total_votes = 0
candidate = " "
vote_count1 = 0
vote_count2 = 0
vote_count3 = 0
vote_count4 = 0
candidates = []
candidate_name = []
candidate_vote = []
candidates_smaller = ['a', 'b', 'c', 'd', 'a', 'a', 'a', 'a', 'b', 'b']


csvpath = os.path.join('..','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader, None)
    
    for row in csvreader:

        #count the rows to get number of months
        row_count = 1
        total_votes += row_count
        
        #put candidates column into a list
        candidates.append(row[2])
        
        #put individual names into a list
       
    for name in candidates:
        if name not in  candidate_name:
                candidate_name.append(name)
        

            #for name in candidates_smaller:
        if name == candidate_name[0]:
                vote_count1 += 1
        elif name == candidate_name[1]:
            vote_count2 += 1
        elif name == candidate_name[2]:
            vote_count3 += 1
        elif name == candidate_name[3]:
            vote_count4 += 1
            
    vote = [vote_count1,vote_count2,vote_count3,vote_count4]

    #find the winner
    most_votes = max(vote)
    winner = vote.index(most_votes)

    #calculate vote percentages
    percent_1 = "{:.3%}".format(vote_count1/total_votes)       
    percent_2 = "{:.3%}".format(vote_count2/total_votes)
    percent_3 = "{:.3%}".format(vote_count3/total_votes)
    percent_4 = "{:.3%}".format(vote_count4/total_votes)    

    percent = [percent_1,percent_2,percent_3,percent_4]    




#cand = dict(zip(list(candidates),[list(candidates).count(i) for i in list(candidates)]))
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"{candidate_name[0]}: {percent[0]} ({vote[0]})")
print(f"{candidate_name[1]}: {percent[1]} ({vote[1]})")
print(f"{candidate_name[2]}: {percent[2]} ({vote[2]})")
print(f"{candidate_name[3]}: {percent[3]} ({vote[3]})")
print("--------------------------")
print(f"Winner: {candidate_name[winner]}")
print("--------------------------")

