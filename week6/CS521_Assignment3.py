class Pet:
    #Create two variables kind and color; assign values

    def __init__(self, name):
        #In the constructor, initialize the pets name

    def do_tricks(self):
        
        #Print the name of the pet and that it is doing tricks
        #Call the speak method
        #Call the jump method

    def speak(self):
        pass

    def jump(self):
        pass

class Jumper:
    'This is a mixin class for jump'
    def jump(self):
        #Create jump method that prints that a Pet is jumping and the pets name

class Dog:  #You will need to inherit for this to work

    #Change kind to canine

    def __str__(self):
        #Print the name and description of dog

    def __call__(self, action):
        #Rollover action prints the name of the dog and that it is rolling over
        #Owner action returns the name of the owner
        

class BigDog:  #You will need to inherit for this to work
    # Change the color to tan

    def __str__(self):
        #Print the name and description of BigDog

    def speak(self):       
        # Print dogs name and what it says

class SmallDog:  #You will need to inherit for this to work

    # Change the color to brindle

    def __str__(self):
        #Print the name and description of SmallDog

    def speak(self):       
        # Print dogs name and what it says
    
class Cat:  #You will need to inherit for this to work

    #Change the kind to feline

    def __str__(self):
        #Print the name and description of cat

    def speak(self):
        # Print cats name and what it says

    def climb(self):
        #Prints the name of the cat and that it is climbing

class HouseCat:  #You will need to inherit for this to work
    #Change the color to white

    def __str__(self):
        #Print the name and description of cat

    def speak(self):
        # Print cats name and what it says
    

###########################################

#EXERCISE YOUR CODE

#    1. Instantiate each class(except jumper)
#    2. Create a list of the instantiated objects
#    3. Loop through the objects
#    4. Print __str__
#    5. print the kind of pet
#    6. Print the Color of the pet
#    7. Have the pet do tricks
#    8. if applicable, print rollover action and the owners name
#    9. If applicable, have the pet climb
#   10. To separate each pet print underscores
