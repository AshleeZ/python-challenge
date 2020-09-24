# Import Modules
import os
import csv

# Set path for file 
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip first row of headers
    next(csvreader)

    #Calculate number of rows in dataset
    total_votes = sum(1 for row in csvreader)

    #Reset iteration for csv file
    csvfile.seek(0)
    next(csvreader)

    #Create empty list to store all values in candidates columns of dataset
    candidates_list = []

    #Create for loop to go through each row and add all iterations of candidate names to created list
    for row in csvreader:
        candidates_list.append(row[2])
    
    #Use the set function to create a list of unique names in the list
    candidates = list(set(candidates_list))

    #Declare temporary variables to store values for use later
    vote_count = None
    percent_votes = None
    
    #Create empty lists to store values in temporary variables
    votes_list = []
    percent_votes_list = []

    #Create for loop to calculate votes and percentage won for each candidate and store them in separate lists
    for candidate in candidates:

        vote_count = candidates_list.count(candidate)
        percent_votes = "{:.3%}".format(vote_count/total_votes)
        votes_list.append(vote_count)
        percent_votes_list.append(percent_votes)
        vote_count = None
        percent_votes = None

    #Create empty list to store candidates names and percentage won in order of highest to lowest votes
    sorted_candidates_list = []
    sorted_percent_list = []

    #Create a copy of the list with total votes for each candidate and sort them from highest to lowest
    sorted_votes_list = votes_list.copy()
    sorted_votes_list.sort(reverse=True)

    #Create a for loop to order candidates and their percentages won based on how many votes they received
    for placement in sorted_votes_list:
        for votes in votes_list:
            if placement == votes:
                sorted_candidates_list.append(candidates[votes_list.index(votes)])
                sorted_percent_list.append(percent_votes_list[votes_list.index(votes)])

    #Sort percentage won list from highest to lowest
    percent_votes_list.sort()

    #Print analysis to terminal
    print(f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------''')

    for name in sorted_candidates_list:
        print(name + ": " + str(sorted_percent_list[sorted_candidates_list.index(name)]) + " (" + str(sorted_votes_list[sorted_candidates_list.index(name)]) + ")")

    print(f'''-------------------------
Winner: {sorted_candidates_list[0]}
-------------------------''')

#Set path for output file 
output_txt = os.path.join('.', 'analysis', 'election_analysis.txt')

#Open the output file and print to text file
with open(output_txt, "w") as text_file:

    print(f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------''', file=text_file)

    for name in sorted_candidates_list:
        print(name + ": " + str(sorted_percent_list[sorted_candidates_list.index(name)]) + " (" + str(sorted_votes_list[sorted_candidates_list.index(name)]) + ")", file=text_file)

    print(f'''-------------------------
Winner: {sorted_candidates_list[0]}
-------------------------''', file=text_file)