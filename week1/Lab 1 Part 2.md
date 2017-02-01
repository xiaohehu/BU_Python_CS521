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

1. Prompt user to input an integer and store it as an int variable `userInput`.  
 
2. Check if the input value is a positive integer:
 * Check if the class of user input is integer - if not, report error and ask user to input again; if is, continue
 * Check if the value of user input is greater than zero - if not, report error and ask user to input again; if is, continue
3. Divide `userInput` by the length of each list, and use the reminder as index to get corresponding list element from sentence, noun, adjective and verb list. Store each picked element as string variables `sentence`, `noun`, `adjective`, and `verb`.

4. Replace `"noun"` in the target sentence by `noun`, `"adjective"` by `adjective`, and `"verb"` by verb. Save the result sentence as string variable `resultSentence`.
5. Check if the result list contains `resultSentence`  
	* If not, push `resultSentence` into result list.
	* If contains, display alert message that the result sentence is duplicated.
6. Go through the result list and print all elements.
7. Prompt user for options, and check the input value:
	* If the input is not "y" or "n" or "Y" or "N", print out alert message to ask user input again.
	* If the input value is "y" or "Y", go back to step 1.
	* If the input value is "n" or "N", terminate the program.