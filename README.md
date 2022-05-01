# Overview of the Election Audit Analysis 
Election votes from US congressional precinct in Colorado are counted in 3 ways:
  - **Mail-in Ballots:** hand-counted at the central office
  - **Punch Cards:** collected and fed into a machine to tabulate the votes which are sent to the central office 
  - **Direct-Recording Electronic (DRE) counting:** votes are recorded and tabulated by the computer and sent to the central office
  
All the votes collected by the above three methods are gathered in a .csv file. Generally election audit analysis is done on Excel to analyze and compute the winning candidate and their statistics.  
## Purpose
Tom, who is charge of auditing and analyzing the election votes, asks for our help to analyze the results using Python. The following results need to be tabulated:
  - total number of votes
  - total votes per county
  - percentage of votes per county
  - the county with the largest turnout
  - total votes per candidate
  - percentage of votes per candidate
  - winning candidate
  
  If the following analysis is succesful, this method will be used for US Senatorial elections and other elections as well.
  
# Election Audit Results
- How many votes were cast in this congressional election?
 
  A total of *369,711* votes were cast.
 
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

  The election audit summary of each county:
    - Jefferson - 38,855 votes (10.5%)
    - Denver - 306,055 votes (82.8%)
    - Arapahoe - 24,801 (6.7%)
  
- Which county had the largest number of votes?

  **Denver County** had the largest number of votes cast with 82.8% of the votes amounting to a total of *306,055* votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

  The election statistics summary of the 3 candidates running:
    - Charles Casper Stockham - 85,213 votes (23.0%)
    - Diana DeGette - 272,892 votes (73.8%)
    - Raymon Anthony Doane - 11,606 (3.1%)
    
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  
  The winner of the election is **Diana DeGette** who got *272,892* votes which is 73.8% of the total votes.
 
 ![Screen Shot 2022-05-01 at 11 45 01 AM](https://user-images.githubusercontent.com/102441140/166160028-b1afcbd4-a9a0-44f7-9857-eb2dee26312c.png)

# Election Audit Summary 

Python is a very versatile tool. This script runs through huge set of voter data and pulls out the candidate names and county names. It also counts the total votes by each candidate or each county and also calculates the percentage of votes by the necessary category. Using conditional statements, this script can easily compute the winning candidate and also check with county had the largest voter turnout. For example, this code was originally writen to pull out candidate names and calculate their statistics. With a slight modification to that code, we were able to pull out county names instead. Similarly, any other category we are interested in from this dataset can be pulled out by looping through all the headers and finding out the relevant category to analyze. Moreover, this code can be applied to any voter dataset which makes it a more universal method to analyze. In Excel, if we used VBA on this dataset, it would only be applicable to this specific sheet. With '*import os*, we can apply this script to any other file. By this method, we are also protecting the data from any malicious tampering which is easier to do on VBA. Thus, overall, using Python in an VS Code environment to inspect and analyze the .csv data file is a better way to analyze and audit the election. 
