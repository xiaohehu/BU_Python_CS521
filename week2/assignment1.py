#Init all varibles
nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman"]
verbs = ["pay", "put", "read", "run", "say", "see"]
adjs = ["other", "new", "good", "high", "old"]
sentence = ["Man verb on a adjective noun.", "Noun verb to the adjective ground.", "All the king’s adjective horses and all the king’s dainty noun could not verb scrambled egg man back together again."]
results = []

# Get the input value from user and check if it's a correct input
runTheGame = True
while runTheGame:
	# Check input value is validate or not
	line = input("integer: ")
	if line:
		try:
			number = int(line)
		except ValueError as err:
			print("The input should be an integer!")
			continue
	if number < 0:
		print("The input integer must be positive!")
		continue
	else:
		# Get index for each list
		indexSentence = number % len(sentence)
		indexNouns = number % len(nouns)
		indexVerbs = number % len(verbs)
		indexAdj = number % len(adjs)
		
		# Get values for picked item in each list
		pickedNoun = nouns[indexNouns]
		pickedVerb = verbs[indexVerbs]
		pickedAdj = adjs[indexAdj]
		pickedSentence = sentence[indexSentence]
		
		# Replace "verb" "adjecvite" and "noun" in the list by picked words
		pickedSentence = pickedSentence.replace("verb", pickedVerb)
		pickedSentence = pickedSentence.replace("adjective", pickedAdj)
		pickedSentence = pickedSentence.replace("noun", pickedNoun)
		
		# Check if the current made sentence is already in the result list
		if pickedSentence in results:
			print("The sentence is already in the list! \n")
		else:
			results.append(pickedSentence)
		print("\nThe current results are: \n")
		
		# Go through the result list and print out all items
		for item in results:
			print(item)
		
		# Let user input and check if the game should continue or not
		keepPlay = True
		while keepPlay:
			play = input("\nDo you want to keep playing? (y/n) ")
			
			if play.isalpha():
				# Make the program not case sensitive
				play = play.lower()
				if play == "y":
					break
				elif play == "n":
					runTheGame = False
					break
				else:
					print("Please input a \"y\" or \"n\"!")
			else:
				print("Please input a \"y\" or \"n\"!")
			
