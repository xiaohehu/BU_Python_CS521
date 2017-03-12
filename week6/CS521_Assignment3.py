class Pet:
    #Create two variables kind and color; assign values    kind = "animal"
    color = "brown"

    def __init__(self, name):
        #In the constructor, initialize the pets name        self.name = name

    def do_tricks(self):
        
        #Print the name of the pet and that it is doing tricks        print(self.name + " is doing tricks")
        #Call the speak method        self.speak
        #Call the jump method        self.jump

    def speak(self):
        pass

    def jump(self):
        pass

class Jumper(Pet):
    #'This is a mixin class for jump'
    def jump(self):
        #Create jump method that prints that a Pet is jumping and the pets name        print(self.name + " is jumping")

class Dog(Jumper, Pet):  #You will need to inherit for this to work

    #Change kind to canine    kind = "canine"
        def __init__(self, name, owner, desc):
        super().__init__(name)
        self.desc = desc
        self.owner = owner

    def __str__(self):
        #Print the name and description of dog        print("I am a dog named " + self.name)
        if self.desc == None:
            print("None")
        else:
            print(self.name + "is a " + self.desc)
#        try:
#            print(self.name + "is a " + self.desc)
#        except AttributeError:
#            print("None")

    def __call__(self, action):
        #Rollover action prints the name of the dog and that it is rolling over        if action == "Rollover":
            print(self.name + " is rolling over")
        #Owner action returns the name of the owner        elif action == "Owner":
            print("My owner is " + self.owner)
        

class BigDog(Dog):  #You will need to inherit for this to work
    # Change the color to tan    color = "tan"
        def __init__(self, name, owner, desc, says):
        super().__init__(name, owner, desc)
        self.says = says
    def __str__(self):
        #Print the name and description of BigDog        super().__str__()

    def speak(self):       
        # Print dogs name and what it says        print(self.name + ": " + self.says)

class SmallDog(Dog):  #You will need to inherit for this to work

    # Change the color to brindle    color = "brindle"

    def __init__(self, name, owner, desc, says):
        super().__init__(name, owner, desc)
        self.says = says
    def __str__(self):
        #Print the name and description of SmallDog        super().__str__()

    def speak(self):       
        # Print dogs name and what it says        print(self.name + ": " + self.says)
    
class Cat(Jumper, Pet):  #You will need to inherit for this to work

    #Change the kind to feline    kind = "feline"
    
    def __init__(self, name, desc, says):
        super().__init__(name)
        self.desc = desc
        self.says = says

    def __str__(self):
        #Print the name and description of cat        print("I am a cat named " + self.name)
        if self.desc == None:
            print("None")
        else:
            print(self.name + "is a cat with" + self.desc)
        
    def speak(self):
        # Print cats name and what it says        print(self.name + " says " + self.says)

    def climb(self):
        #Prints the name of the cat and that it is climbing        print(self.name + " is climbing")

class HouseCat(Cat):  #You will need to inherit for this to work
    #Change the color to white    color = "white"

    def __init__(self, name, desc, says):
        super().__init__(name, desc, says)
    def __str__(self):
        #Print the name and description of cat        super().__str__()

    def speak(self):
        # Print cats name and what it says
        super().speak()
    

###########################################

#EXERCISE YOUR CODE

#    1. Instantiate each class(except jumper)objectPet = Pet("Taz")
objectDog = Dog("Roo", "George", None)
objectBigDog = BigDog("Noah", "Georage", "large, muscular dog", "Woof!!!")
objectSmallDog = SmallDog("Lucky", "Georage", "tiny, cute dog", "Yip!")
objectCat = Cat("Lion", None, "Meow!!!")
objectHouseCat = HouseCat("Zebra", "fluffy, white fur", "Purr")

#    2. Create a list of the instantiated objectsobjectList = [objectPet, objectDog, objectBigDog, objectSmallDog, objectCat, objectHouseCat]

#    3. Loop through the objectsfor objectItem in objectList:
    
#    4. Print __str__    try:
        objectItem.__str__()
    except AttributeError:
        pass
        
#    5. print the kind of pet    print(objectItem.kind)
    
#    6. Print the Color of the pet    print(objectItem.color)
    
#    7. Have the pet do tricks    objectItem.do_tricks()
    objectItem.speak()
    objectItem.jump()
#    8. if applicable, print rollover action and the owners name    try:
        objectItem.__call__("Rollover")
    except AttributeError:
        pass
    
    try:
        objectItem.__call__("Owner")
    except AttributeError:
        pass
        
#    9. If applicable, have the pet climb
    try:
        objectItem.climb()
    except AttributeError:
        pass
#   10. To separate each pet print underscores
    print("----------------------------------------")
