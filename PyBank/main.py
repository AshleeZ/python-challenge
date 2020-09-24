# Import Modules
import os
import csv

# Set path for file 
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip first row of headers
    next(csvreader)

    #Declare variable for total months and calculate for dataset
    total_months = sum(1 for row in csvreader)

    #Reset iteration for csv file
    csvfile.seek(0)
    next(csvreader)

    #Declare variable for net total amount of "Profit/Losses" and start at 0
    net_total_amount = 0

    #Create for loop to add values in column 2 to variable for each row in csvreader
    for row in csvreader:
        net_total_amount += int(row[1])
    
    #Reset iteration for csv file
    csvfile.seek(0)
    next(csvreader)
    
    #Declare variables to store "Date" and "Profit/Losses" as a lists 
    date_list = []
    profit_loss_list = []

    #Create for loop to store "Date" and "Profit/Losses" column of each row in lists created
    for row in csvreader:
        date_list.append(row[0])
        profit_loss_list.append(int(row[1]))

    #Drop the first date in date_list since there is no change
    date_list.pop(0)

    #Declare a variable to store the difference between each row in column 2
    change_list = []

    #Create for loop to calculate the change between each row in column 2
    for profit_loss in profit_loss_list[1:]:
        change = profit_loss_list[profit_loss_list.index(profit_loss)]-profit_loss_list[(profit_loss_list.index(profit_loss))-1]
        
        #Add each change calculated into the list created
        change_list.append(change)

    #Calculate average monthly change 
    average_monthly_change = format((sum(change_list))/(len(change_list)), '.2f')

    #Calculate greatest increase in profits using change_list
    greatest_increase = max(change_list)

    #Calculate greatest decrease in profits using change_list
    greatest_decrease = min(change_list)

    #Combine date_list and change_list into dictionary to determine when each change occurred
    datedict = dict(zip(change_list, date_list))

    #Reset iteration for csv file
    csvfile.seek(0)
    next(csvreader)

    #Create for loop to find date of greatest increase in profits in dictionary
    for change in datedict:

        if change == greatest_increase:
            greatest_increase_date = datedict[change]

    #Reset iteration for csv file
    csvfile.seek(0)
    next(csvreader)

    #Create for loop to find date of greatest decrease in profits in dictionary
    for change in datedict:

        if change == greatest_decrease:
            greatest_decrease_date = datedict[change]

    #Print analysis to terminal
    print(f'''
Financial Analysis
-------------------------------
Total Months: {total_months}
Total: ${net_total_amount}
Average Change: ${average_monthly_change}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
    ''')

#Set path for output file 
output_txt = os.path.join('.', 'analysis', 'budget_analysis.txt')

#Open the output file and print to text file
with open(output_txt, "w") as text_file:
    print(f'''
Financial Analysis
-------------------------------
Total Months: {total_months}
Total: ${net_total_amount}
Average Change: ${average_monthly_change}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
    ''', file=text_file)