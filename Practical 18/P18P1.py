


"""
Checks whether the string s is a palindrome
Assumes that s is a str with only lowercase letters and no non-letters.
Returns True if s is a palindrome;
Returns False otherwise.
Recursive function.
Has print statements to trace its operation.

"""

def isPalindrome(s):
	def toChars(s):
		s = s.lower()
		letterstring = ""
		for c in s:
			if c in "abcdefghijklmnopqrstuvwxyz":
				letterstring += c
		return letterstring
	def isPal(s):
		length = len(s)
		i = 0
		while i < length / 2 + 1:
		    if s[i] != s[-i - 1]:
		        return False
		        break
		    i += 1
		else:
		    return True
	return isPal(toChars(s))

string = input("Please enter a sentence (leave empty if you wish to exit)\n")

while string != "":
	if isPalindrome(string):
		print (string, "is a palindrome")
	else:
		print(string, "is not a palindrome")
	string = input("Please enter a sentence (leave empty if you wish to exit) \n")

print("Finished")