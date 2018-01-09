"""
Function that takes a string as an argument and returns the number of times that the
string “code” (case-sensitive) appears anywhere in the given string


Prompt user for input as string
Create function count_code
if empty then print you did not enter a sentence
else print Number of occurences of 'code':", a.count("code")

call function count_code(string)
"""

string = input("Please enter a sentence with the word 'code': \n")

def count_code(a):
	if a == "":
		print("You did not enter a sentence.")
	else:
		print("Number of occurences of 'code':", a.count("code"))

count_code(string)		

