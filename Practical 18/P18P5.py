

def xyz_there(str):
	str = str.replace(".xyz", "")
	if "xyz" in str:
		return True
	else:
		return False 


string1 = input("Please enter the first sentence: \n")

print(xyz_there(string1))
