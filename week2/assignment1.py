#Init all varibles
nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman"]
verbs = ["pay", "put", "read", "run", "say", "see"]
adjs = ["other", "new", "good", "high", "old"]
sentence = ["Man verb on a adjective noun.", "Noun verb to the adjective ground.", "All the king’s adjective horses and all the king’s dainty noun could not verb scrambled egg man back together again."]

# Get the input value from user and check if it's a correct input
line = input("integer: ")
inputIsCorrect = False
while !inputIsCorrect:
	if line:
		try:
			number = int(line)
		except ValueError as err:
			print(err)
	if number < 0:
		print("The input integer must be positive.")
	else
