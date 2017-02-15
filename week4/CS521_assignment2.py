'''
This file is a template that may be used for Assignment 2.  The intent is to supply
you with some code so you can focus on the new items in the program
'''
import operator
import os
import random


def load_csv_to_list(path_to_file):
  #Validate Path to file exists

  #Validate file exists

  #Return a list of items from file



def shuffle(sequence):
    'Returns a shuffled list'

    #Write the code that will take a list and shuffle it randomly



def load_mad_lib_resource(path_to_resource):
  #Call load_csv_to_list

  #Verify the file exists

  #Return a tuple of the shuffled list


def play_game(user_sentences,lower_bound, upper_bound):
    is_keep_playing = None

    while is_keep_playing != 'n':
        user_str_number = input(
            "Please provide a number between {} and {}".format(lower_bound, upper_bound)
    )

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

        #PRINT ALL OF THE SENTENCES FOR THE USER THUS FAR

    is_keep_playing = None  # reset

    while 'y' != is_keep_playing and 'n' != is_keep_playing:
      is_keep_playing = input("Do you want to keep playing? y / n")
      try:
        is_keep_playing = is_keep_playing.strip().lower()
      except:
        is_keep_playing = None

      if 'y' != is_keep_playing and 'n' != is_keep_playing:
        print("Sorry, I did not get that.")


# GET THE LISTS FROM THE FILES

#VERIFY THE LISTS EXIST

# boundaries
MIN_VALUE = 0
MAX_VALUE = max(
        len(SENTENCES),
        len(NOUNS),
        len(VERBS),
        len(ADJECTIVES),
)

#PROMPT FOR USERNAME

#VERIFY THE A USER NAME WAS ENTERED ELSE EXIT THE PROGRAM

#FIND OUT IF THERE IS AN EXISTING USER SAVED GAMES

# user's mad lib
user_sentences = []

#GET THE USER'S SAVED GAMES IF IT EXISTS

#SORT THE USER SENTENCES

#CALL PLAY GAME FUNCTION

print("Bye!")
