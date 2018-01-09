"""
Write a function to  that takes 2 arguments and returns true is either of the strings appears in the second sentence

create function check_string which takes 2 arguments a and b
set a and b to lower case letters

prompt the user for string 1 and string 2

print the fucntion check_string and take in string 1 and string 2 as arguments
"""



def check_String(a, b):
	a = a.lower()
	b = b.lower()
	if a in b and b.rfind(a)+len(a) == len(b):
		return True
	elif b in a and a.rfind(b)+len(b) == len(a):
		return True
	else:
		return False


string1 = input("Please enter the first sentence: \n")
string2 = input("Please enter the second sentence: \n")

print(check_String(string1, string2))
