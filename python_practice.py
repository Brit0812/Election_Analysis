#Goals of the assignment (this is the pseudocode)
#Retrive the required data 
#1. total casted votes 
#2. List of candidates
#3. percentage of votes for each candidate 
#4. total votes for EACH candidate 
#5. winner of the election- popular vote

 # import the datetime class from the datetime module.
import datetime
import os
 #.now lets to get the preset time 
now= datetime.datetime.now()
print ("The time right now is", now)
# is there a way to reformat the date?
# the abbreviation for datetime is dt 
import datetime as dt 
now= dt.datetime.now()
print("The time right now is", now)

#while in the terminal type in python3- then do all this 
import csv
dir(csv)
#dir- short for directory 
#you can do dir(int), dir(float) etc 

# Assign a variable for the file to load and the path.
file_to_load = ('Resources/election_results.csv')
#open the file to read it 
election_data = open(file_to_load,'r')
#perform the analysis 
#close the file
election_data.close()

#another way to open the file- 
#with open(file_to_load) as election_data:
  # print(election_data.read())
#when we dont have the direct path file we use (os):
#print(dir(os))<-- brings up the directory, which includes 'path'
import csv
import os
dir(os)
file_to_load= os.path.join("Resources","election_results.csv")
with open(file_to_load) as election_data:
   print(election_data.read())

# # Assign a variable for the file to load and the path.
# #file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# #with open(file_to_load, 'r') as election_data:
#     # Print the file object.
#      #print(election_data)

file_to_save = os.path.join("analysis","election_analysis.txt")
open(file_to_save, "w")
outfile= open(file_to_save, "w")
outfile.write("hello world, im brit")
outfile.close()
#above is the general code- below its with the WITH so that we dont need the open close etc 
with open(file_to_save, 'w') as txt_file:
   txt_file.write("hello world, how are you")
   txt_file.write("Arapahoe, ")
   txt_file.write("Denver, ")
   txt_file.write("Jefferson, ")
   # if ther is no comma space, there will be NO space between the words OR
   txt_file.write("Arapahoe, Denver, Jefferson")
   #if you want each county on a different line you need a /n 
   txt_file.write("\nArapahoe\nDenver\nJefferson")
   txt_file.write("\nCounties in the Elections\n-----------------------\nArapahoe\nDenver\nJefferson")
 
file_reader = csv.reader(election_data)
