#imports modules
import os
import csv

#initialize variables
total_votes = 0
# profit = 0 
# previous_amt = 0
# total_change = 0
# greatest_change = 0
# least_change = 0
# greatest_month = ""
# least_month = ""

csvpath = os.path.join('..','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader, None)
    
    for row in csvreader:

        #count the rows to get number of months
        row_count = 1
        total_votes += row_count



print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")


