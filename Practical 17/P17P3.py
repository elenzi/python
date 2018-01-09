"""
Define two variables as strings
Define an input variable that accepts a string
Count to see if the two strings are both in the input variable the same number of times.
if count of string 1 equals count of string 2 then
print string1, "and", string2, "both appear the same number of times","(", s_input.count(string1)," times)"
else then print if they are counted the same number of times.

"""


string1 ="dog"
string2 ="cat"

s_input = input('Please input a string:\n')

if s_input.count(string1) == s_input.count(string2) :
    print(string1, "and", string2, "both appear the same number of times","(", s_input.count(string1)," times)")
else :
    print("Your input doesn't contain", string1, "or", string2, "the same number of times")
