# from re import X
# x=0 
# while x <= 5:
#     print(x)
#     x= x+1
# numbers= [0, 1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)
# #same as above 
# for num in range(5):
#     print(num)

import csv
import os 
dir(os)

file_to_open= os.path.join("Resources","testing_file_stuff_CSV.csv")
with open(file_to_open) as practice:
    print(practice.read())
file_to_practice= os.path.join("analysis","practicing_files.txt")
open(file_to_practice, "w")
files_practice= open(file_to_practice, "w")
files_practice.write("Hello, im practicing")

with open(file_to_practice, 'w') as files_practice:
   files_practice.write("hello world, how are you")
   files_practice.write("\nCounties in the Elections\n -----------------------\nArapahoe\nDenver\nJefferson")



#Goals of the assignment (this is the pseudocode)
#Retrive the required data 
#1. total casted votes 
#2. List of candidates
#3. percentage of votes for each candidate 
#4. total votes for EACH candidate 
#5. winner of the election- popular vote

# import csv
# import os
# file_to_load= os.path.join("Resources","election_results.csv")
# # file_to_save = os.path.join("analysis","election_analysis.txt")
# total_votes= 0
# candidate_options=[]
# #Dictionary 
# candidate_votes={}
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0

# with open(file_to_load) as election_data:
#    file_reader = csv.reader(election_data)
#    headers= next(file_reader)
#    for row in file_reader:
#       total_votes +=1
#       #Good info below 
#       #The standard Python format to increment a variable is 
#       # number = number + 1, which can be augmented to number += 1.
#       candidate_name=row[2]
#       if candidate_name not in candidate_options:
#          candidate_options.append(candidate_name)
#          #tracking count
#          candidate_votes[candidate_name] = 0
#       candidate_votes[candidate_name] += 1
# with open(file_to_save, "w") as txt_file:
#    election_results = (
#       f"\nElection Results\n"
#       f"-------------------------\n"
#       f"Total Votes: {total_votes:,}\n"
#       f"-------------------------\n")
#    print(election_results, end="")
#     # Save the final vote count to the text file.
#    txt_file.write(election_results)
#    for candidate_name in candidate_votes:
#       votes= candidate_votes[candidate_name]
#       vote_percentage = float(votes)/ float(total_votes)*100
#       candidate_results=(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
#       print(candidate_results)
#       txt_file.write(candidate_results)
#       if (votes > winning_count) and (vote_percentage >winning_percentage):
#          winning_count= votes
#          winning_percentage= vote_percentage
#          winning_candidate= candidate_name
#    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#    #why is it only showing raymon and not the other 2 candidates in the txt?
#    winning_candidate_summary = (
#       f"-------------------------\n"
#       f"Winner: {winning_candidate}\n"
#       f"Winning Vote Count: {winning_count:,}\n"
#       f"Winning Percentage: {winning_percentage:.1f}%\n"
#       f"-------------------------\n")
#    print(winning_candidate_summary)
#    txt_file.write(winning_candidate_summary)
# # # rem, when commiting to git write "git add ." the periods important 
# # #  otherwise youll get an error 