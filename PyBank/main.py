#imports modules
import os
import csv

#initialize variables
number_of_rows = 0
profit = 0 
previous_amt = 0
total_change = 0
greatest_change = 0
least_change = 0
greatest_month = ""
least_month = ""

csvpath = os.path.join('..','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=",")
    # skip header row
    csv_header = next(csvreader, None)
    
    
    # loop through rows
    for row in csvreader:
        #net total amount of Profit/Losses
        profit += int(row[1])

        #count the rows to get number of months
        row_count = 1
        number_of_rows += row_count
        
        #calculate change
        new_amt = int(row[1])
        change = new_amt - previous_amt
        total_change += change
        if previous_amt == 0:
            total_change = 0
        previous_amt = new_amt

        #fine greatest increase/decrease and month
        if change > greatest_change:
            greatest_change = change
            greatest_month = row[0]
        elif change < least_change:
            least_change = change
            least_month = row[0]

    #print analysis
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {number_of_rows}")
    print(f"Total ${profit}")
    avg_change = total_change/(number_of_rows - 1)
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits: {greatest_month} (${greatest_change})")
    print(f"Greatest Decrease in Profits: {least_month} (${least_change})")
    
# Specify the file to write to
output_path = os.path.join("..", "analysis", "Financial_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline = '') as text_file:

    # Write to the text file
    text_file.write("Financial Analysis\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total Months: {number_of_rows}\n")
    text_file.write(f"Total ${profit}\n")
    text_file.write(f"Average Change: ${round(avg_change, 2)}\n")
    text_file.write(f"Greatest Increase in Profits:  {greatest_month} (${greatest_change})\n")
    text_file.write(f"Greatest Decrease in Profits:  {least_month} (${least_change})\n")
    
    





        