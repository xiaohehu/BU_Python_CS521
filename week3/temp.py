"""
Step 1: create a new .csv file and write 0 - 10 into the file, each line has only one number
"""
with open("number.csv", "w") as numberFile:
	for i in range(11):
		numberFile.write(str(i) + '\n')
numberFile.close()

"""
Step 2: Read the csv file, put each number into a list. And convert all str to int
"""
# Read file
with open("number.csv", "r") as numberFile:
	numberListStr = numberFile.read().splitlines()
numberFile.close()
# Convert str to int
numberListInt = []
for i in numberListStr:
	numberListInt.append(int(i))
	
"""
Step 3: Print content of the list
"""
for item in numberListInt:
	print(item)