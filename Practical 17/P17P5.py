"""
Checks whether the string s is a palindrome
Assumes that s is a str with only lowercase letters and no non-letters.
Returns True if s is a palindrome;
Returns False otherwise.
Recursive function.
Has print statements to trace its operation.

"""

def isPalindrome(s):
	"""Checks whether the string s is a palindrome
    Assumes s is a str.
    Returns True if the letters in s form a palindrome;
    Returns False otherwise.
    Case and non-letters are ignored."""
	def toChars(s):
		"""Converts a string to lowercase and removes non-letters
        Assumes s is a str.
        Converts uppercase letters to lowercase and removes non-letter"""
        # convert uppercase letters to lowercase
		s = s.lower()
		# Start with an empty string
		letterstring = ""
		for c in s:
			if c in "abcdefghijklmnopqrstuvwxyz":
				letterstring += c
		return letterstring
	def isPal(s):
		print("isPal function called with argument", s)
		if len(s) <= 1:
			# A palindrome of length 0 or 1 is a palindrome
			print("About to return True from isPal from the base case")
			return True
		else:
			# Compare the first and the last letters and check the remainder of the string
			return s[0] == s[-1] and isPal(s[1:-1])
	return isPal(toChars(s))

string = input("Please enter a sentence (leave empty if you wish to exit)")

while string != "":
	if isPalindrome(string):
		print (string, "is a palindrome")
	else:
		print(string, "is not a palindrome")
	string = input("Please enter a sentence (leave empty if you wish to exit)")

print("Finished")