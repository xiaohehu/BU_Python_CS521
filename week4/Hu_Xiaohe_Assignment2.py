'''
This file is a template that may be used for Assignment 2.  The intent is to supply
you with some code so you can focus on the new items in the program
'''
import operator
import os
import random
import sys


def load_csv_to_list(path_to_file):
    resultList = []
    #Validate Path to file exists
    if not os.path.exists(path_to_file):
      print("Path to file does NOT exist!")
      return resultList
    #Validate file exists
    elif not os.path.isfile(path_to_file):
      print("The file does NOT exist in the path!")
      return resultList
    #Return a list of items from file
    else:
      with open(path_to_file, "r") as readFile:
        resultList = readFile.read().splitlines()
      readFile.close()
    return resultList


def shuffle(sequence):
    #Write the code that will take a list and shuffle it randomly
    length = len(sequence)
    randomIndex = []
    # Generate a list with random order of index
    while len(randomIndex) < length:
      randomNum = random.randrange(0, length, 1)
      if randomNum not in randomIndex:
        randomIndex.append(randomNum)
      else:
        continue
    # Use the random order index list to shuffle the sentence/words list
    resultList = []
    for item in randomIndex:
      resultList.append(sequence[item])
    
    return resultList

def load_mad_lib_resource(path_to_resource):
    resourceList = []
    #Call load_csv_to_list
    resourceList = load_csv_to_list(path_to_resource)
    #Verify the file exists
    if len(resourceList) == 0:
        print("The list is empty!")
        return resourceList
    #Return a tuple of the shuffled list
    resourceTuple = tuple(shuffle(resourceList))
    return resourceTuple

def play_game(user_sentences,lower_bound, upper_bound):
    is_keep_playing = None

    while is_keep_playing != 'n':
      user_str_number = input("Please provide a number between {} and {}: ".format(lower_bound, upper_bound))
      try:
        user_number = int(user_str_number.strip().lower())
      except:
        print("Sorry the value provided is not an integer.")
        user_number = None

      if user_number is not None:
        if user_number < MIN_VALUE:
          print("Sorry the number provided is too small (lower than {})".format(MIN_VALUE))
        elif user_number > MAX_VALUE:
          print("Sorry the number provided is too big (greater than {})".format(MAX_VALUE))
        else:
          sentence_idx = random.randint(user_number, MAX_VALUE) % len(SENTENCES)
          noun_idx = random.randint(user_number, MAX_VALUE) % len(NOUNS)
          verb_idx = random.randint(user_number, MAX_VALUE) % len(VERBS)
          adjective_idx = random.randint(user_number, MAX_VALUE) % len(ADJECTIVES)
  
          # generate the mad lib sentence
          sentence = SENTENCES[sentence_idx].format(
                  noun=NOUNS[noun_idx],
                  verb=VERBS[verb_idx],
                  adjective=ADJECTIVES[adjective_idx],
          )
  
          #GENERATE THE SENTENCES AND WRITE TO THE FILE IF NOT ALREADY SAVED
          if sentence not in user_sentences:
            user_sentences.append(sentence)
            user_sentences.sort()
          else:
            print("This sentence is already in data file!")
          #PRINT ALL OF THE SENTENCES FOR THE USER THUS FAR
          for item in user_sentences:
            print(item)
  
      is_keep_playing = None  # reset
  
      while 'y' != is_keep_playing and 'n' != is_keep_playing:
        is_keep_playing = input("Do you want to keep playing? y / n: ")
        try:
          is_keep_playing = is_keep_playing.strip().lower()
        except:
          is_keep_playing = None
  
        if 'y' != is_keep_playing and 'n' != is_keep_playing:
          print("Sorry, I did not get that.")


# GET THE LISTS FROM THE FILES
def createResourceFiles(path_to_resource):
    nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman"]
    verbs = ["pay", "put", "read", "run", "say", "see"]
    adjs = ["other", "new", "good", "high", "old"]
    sentence = ["Man {verb} on a {adjective} {noun}.", "{noun} {verb} to the {adjective} ground.", "All the king’s {adjective} horses and all the king’s dainty {noun} could not {verb} scrambled egg man back together again."]
    #Change working directory to resource folder
    os.chdir(path_to_resource)
    with open("Senteces.csv", "w") as sentenceFile:
      for s in sentence:
        sentenceFile.write(s + "\n")
    sentenceFile.close()
    
    with open("Verbs.csv", "w") as verbFile:
      for v in verbs:
        verbFile.write(v + "\n")
    verbFile.close()
    
    with open("Nouns.csv", "w") as nounFile:
      for n in nouns:
        nounFile.write(n + "\n")
    nounFile.close()
    
    with open("Adjectives.csv", "w") as adjFile:
      for a in adjs:
        adjFile.write(a + "\n")
    adjFile.close()
  
# Step 1_a cerate "resources" folder to store all resource files
currentPath = os.getcwd()
resourcePath = os.path.join(currentPath, "resources")
if not os.path.exists(resourcePath):
    # Create the folder
    os.makedirs(resourcePath)
    # Create .csv files
    createResourceFiles(resourcePath)
    # After creating .csv files go back to orginal folder
    os.chdir(currentPath)
    
#VERIFY THE LISTS EXIST
SENTENCES = load_mad_lib_resource(os.path.join(resourcePath, "Senteces.csv"))
NOUNS = load_mad_lib_resource(os.path.join(resourcePath, "Nouns.csv"))
VERBS = load_mad_lib_resource(os.path.join(resourcePath, "Verbs.csv"))
ADJECTIVES = load_mad_lib_resource(os.path.join(resourcePath, "Adjectives.csv"))
while len(SENTENCES) == 0 or len(NOUNS) == 0 or len(VERBS) == 0 or len(ADJECTIVES) == 0:
    createResourceFiles(resourcePath)
    SENTENCES = load_mad_lib_resource(os.path.join(resourcePath, "Senteces.csv"))
    NOUNS = load_mad_lib_resource(os.path.join(resourcePath, "Nouns.csv"))
    VERBS = load_mad_lib_resource(os.path.join(resourcePath, "Verbs.csv"))
    ADJECTIVES = load_mad_lib_resource(os.path.join(resourcePath, "Adjectives.csv"))
    
# boundaries
MIN_VALUE = 0
MAX_VALUE = max(
        len(SENTENCES),
        len(NOUNS),
        len(VERBS),
        len(ADJECTIVES),
)

#PROMPT FOR USERNAME
userName = input("Please input your username: ")

#VERIFY THE A USER NAME WAS ENTERED ELSE EXIT THE PROGRAM
if not userName:
  print("Bye!")
  sys.exit()
  
#FIND OUT IF THERE IS AN EXISTING USER SAVED GAMES
userDataFile = userName + ".csv"
userDataPath = os.path.join(currentPath, userDataFile)
hasUserData = os.path.isfile(userDataPath)
# user's mad lib
user_sentences = []

#GET THE USER'S SAVED GAMES IF IT EXISTS
if hasUserData:
    with open(userDataPath, "r") as userData:
        user_sentences = userData.read().splitlines()
    userData.close()
#SORT THE USER SENTENCES
user_sentences.sort()
#CALL PLAY GAME FUNCTION
play_game(user_sentences, MIN_VALUE, MAX_VALUE)

#Save the current user data to a .csv file
with open(userDataFile, "w") as userData:
    for i in user_sentences:
        userData.write(i + "\n")
userData.close()
print("Bye!")
