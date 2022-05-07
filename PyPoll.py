#Goals of the assignment (this is the pseudocode)
#Retrive the required data 
#1. total casted votes 
#2. List of candidates
#3. percentage of votes for each candidate 
#4. total votes for EACH candidate 
#5. winner of the election- popular vote

import csv
import os
file_to_load= os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)
   headers= next(file_reader)
   print(headers)