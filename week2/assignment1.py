#Init all varibles
nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman"]
verbs = ["pay", "put", "read", "run", "say", "see"]
adjs = ["other", "new", "good", "high", "old"]
sentence = ["Man verb on a adjective noun.", "Noun verb to the adjective ground.", "All the king’s adjective horses and all the king’s dainty noun could not verb scrambled egg man back together again."]
results = []

# Get the input value from user and check if it's a correct input
keepPlay = True
while keepPlay:
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
		# Get index
		indexSentence = number % len(sentence)
		indexNouns = number % len(nouns)
		indexVerbs = number % len(verbs)
		indexAdj = number % len(adjs)
		# Get values for picked item in each list
		pickedNoun = nouns[indexNouns]
		pickedVerb = verbs[indexVerbs]
		pickedAdj = adjs[indexAdj]
		pickedSentence = sentence[indexSentence]
		
		pickedSentence = pickedSentence.replace("verb", pickedVerb)
		pickedSentence = pickedSentence.replace("adjective", pickedAdj)
		pickedSentence = pickedSentence.replace("noun", pickedNoun)
		
		if pickedSentence in results:
			print("The sentence is already in the list! \n")
		else:
			results.append(pickedSentence)
		print("The current results are: \n")
		for item in results:
			print(item)
		
		inputPlay = True
		while inputPlay:
			play = input("Do you want to keep playing? (y/n) ")
			
			if play.isalpha():
				if play is "y":
					break
				elif play is "n":
					keepPlay = False
					break
				else:
					print("Please input a \"y\" or \"n\"!")
			else:
				print("Please input a \"y\" or \"n\"!")
			
