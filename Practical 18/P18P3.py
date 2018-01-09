"""

Prompt user for input as string
Create function count_code
set count as = 0
if empty string is entered print you did not enter a sentence
else for i in lower case letters, numbers and upper case letters 
set count to count of i within co and e
print count
call count code fucntion as count_code(string)
"""


def count_code(s):
	if s == "":
		print("You did not enter a sentence.")
	else:
		count = 0 
		for i in "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM":
			count += s.count ("co" +i+"e")
	print(count)

string = input("Please enter a sentence with the word 'code': \n")
count_code(string)



