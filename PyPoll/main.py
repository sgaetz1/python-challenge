#import modules
import os
import csv

#initialize variables
total_votes = 0
vote_count1 = 0
vote_count2 = 0
vote_count3 = 0
vote_count4 = 0
candidates = []
candidate_name = []
vote = []
percent = []

#open the csv file
csvpath = os.path.join('..','Resources','election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
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
        
        #count the votes for each candidate
        if name == candidate_name[0]:
                vote_count1 += 1
        elif name == candidate_name[1]:
            vote_count2 += 1
        elif name == candidate_name[2]:
            vote_count3 += 1
        elif name == candidate_name[3]:
            vote_count4 += 1
    
    #put votes in a list        
    vote = [vote_count1,vote_count2,vote_count3,vote_count4]

    #find the winner: winner is the index of candidate with most votes
    most_votes = max(vote)
    winner = vote.index(most_votes)

    #calculate vote percentages
    percent_1 = "{:.3%}".format(vote_count1/total_votes)       
    percent_2 = "{:.3%}".format(vote_count2/total_votes)
    percent_3 = "{:.3%}".format(vote_count3/total_votes)
    percent_4 = "{:.3%}".format(vote_count4/total_votes)    
    #put percentages in a list
    percent = [percent_1,percent_2,percent_3,percent_4]    


#print to the terminal
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

#Specify the file to write to
output_path = os.path.join("..", "analysis", "Election_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline = '') as text_file:

    # Write to the text file
    text_file.write("Election Results\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("--------------------------\n")
    text_file.write(f"{candidate_name[0]}: {percent[0]} ({vote[0]})\n")
    text_file.write(f"{candidate_name[1]}: {percent[1]} ({vote[1]})\n")
    text_file.write(f"{candidate_name[2]}: {percent[2]} ({vote[2]})\n")
    text_file.write(f"{candidate_name[3]}: {percent[3]} ({vote[3]})\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Winner: {candidate_name[winner]}\n")
    text_file.write("--------------------------\n")

