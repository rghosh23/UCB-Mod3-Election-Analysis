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

# Open the election results and read the file
# 'with open' helps us read and write to a file, instead of just opening
with open(file_to_load) as election_data:
    # To do: read and analyze the data here 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print (headers)
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

## total number of votes cast
## complete list of candidates who recieved the votes
## % of votes that each candidate won
## total number if votes each candidate won
## winner of the election based on the popular vote