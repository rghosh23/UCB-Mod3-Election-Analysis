## Retrieve the data to load
import csv
import os
# Assign variable to the file we are loading
#1 direct path: file_to_load = "Resources/election_results.csv"
#2 indirect path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# Use the open statement to open the file as a text file.
#1: outfile = open(file_to_save, "w")
#2: using 'with open'
#with open(file_to_save, "w") as txt_file:   
    # Write some data into the file 
    #\n adds a newline when you call it
    #txt_file.write ("Counties in the Election")
    #txt_file.write ("-------------------------\n")
    #txt_file.write ("Arapahoe \n")
    #txt_file.write ("Denver \n")
    #txt_file.write ("Jefferson")
    # 2 : txt_file.write("Arapahoe, Denver, Jefferson")
    #close the file 
    #txt_file.close()

# initialize a total vote counter
total_votes = 0

#initalize candidate option variable
candidate_options = []

#initialize empty dictionary to hold candidate names and the votes cast for them
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
# 'with open' helps us read and write to a file, instead of just opening
with open(file_to_load) as election_data:
    # To do: read and analyze the data here 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print (headers)
## total number of votes cast
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        ## complete list of candidates who recieved the votes
        #print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # begin tracking the camdidate's vote count
            candidate_votes[candidate_name]= 0
    ## total number of votes each candidate won
        #add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

 # Print the total votes.
print(total_votes)
print(candidate_options)
print(candidate_votes)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    ## % of votes that each candidate won     
    #Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        ## winner of the election based on the popular vote
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
