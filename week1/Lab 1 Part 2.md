# Lab 1 Part 2

## Xiaohe Hu

### Data structure and varibles
**Data structure needed:**

* List
* String

**Variables might needed:**

* Noun list
* Adjective list
* Verb list
* Unfinished sentence list
* Result sentence list
* Couple strings to store user picked sentence and words
* Couple integers to store user's input number and picking element's index

### Control flow

> Init 5 lists contain noun, adjective, verb, sentence and result (noun, adjective, verb and sentence lists should have different number of elements. Initial value of result list is empty).

1. Let user input an integer and store it as an int variable. 
2. Check if the input value is a positive integer (the following code):

	~~~python
	#Check if the input value is an integer
	try:
   		val = int(userInput)
   		...

	# Check if the input integer is positive
	if val > 0:
		...
	~~~
	
	* If not (the input value is not a intger, or the integer is negative) report error and ask user to input again.
	* If is, continue.
3. Divide user input by the length of each list, and use the reminder as list index to get the sentence, noun, adjective and verb from each list.

	~~~python
	index = userInput % len(list)
	~~~
	
4. Replace "noun", "verb" and "adjective" by the picked noun word, verb word and adjective word. Get the result sentence.
5. Check if the result list contains the same result sentence(go through the result list, compare each item with the current sentence, pseudocode is followed):

	~~~python
	for sentence in resultList:
		if sentence == currentSentence:
			# Current sentence is in the result list
			...
		else:
			# Current sentence is not in the result list
			...
	~~~
	* If the current result sentence is not in the result list then save it.
	* If the current result sentence is already in the result do not save it and print out alert message.
6. Go through the result list and print all content of the list.
7. Print out message to ask if user want to play it again, and check the input value:
	* If the input is not "y" or "n" or "Y" or "N", print out alert message to ask user input again.
	* If the input value is "y" or "Y", go back to step 1.
	* If the input value is "n" or "N", terminate the program.