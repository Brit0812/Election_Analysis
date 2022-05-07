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
