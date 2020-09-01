#
# Instructions:
# Work through the following prompts. Prompts marked with "We Do", we will work
# on together, as a class; prompts marked with "You Do", you will be given time
# to work through on your own.
#
# Tip: comment out your solution to each prompt before moving on to the next
# one! This will keep your console clear.
#
# from cffi import model

#
# Prompt 1: We Do
#
# Define a class for a Car. Your Car class should have the following
# properties:
#
#    - make
#    - model
#    - color
#
# Your Car class should have the following methods:
#
#    - drive: print 'vroom vroom' to the console
#
# Once you create your class definition create two instances.
#
# class car:
    
#     def __init__(self, color, model, make):
#         self.color = color
#         self.model = model
#         self.make = make
    
#     def __str__(self):
#         return f"This is a {self.color} {self.make} {self.model}"

#     def drive(self):
#         print(f"{self.model} goes Vroom Vroom")
        
# instance1 = car("Ford", "Fusion", "White")
# print(instance1)

# instance2 = car("GMC", "Acadia", "silver")
# print(instance2)

# #
# # Prompt 2: We Do
# #
# # We're going to modify our Car class from the previous prompt and extend it to
# # create a Toyota class:
# #
# #   - Extend your Car class to create a Toyota class. The make property will always
# #     be 'Toyota'. Add a drive method to your Toyota class.
# #
# # Make an instance of your Toyota class.
# #

# class Toyota(car):
    
#     def __init__(self, color, model, make="toyota"):
#         super().__init__(color, model, make)
    
#     def drive(self):
#         print("Toyota Rules")    
            
# camry = Toyota("Blue", "Camry")
# print(camry)

# bmw = Toyota("Silver", "BMW")
# print(bmw)

# bmw.drive()

#
# Prompt 3: You Do
#
# Define a class for your favorite animal (dog, cat, giraffe, etc). Give your
# class 3 attributes and two methods.
#
# After you've defined your class, create 3 instances.
#


class dog:

    def __init__(self, color, type, size):
        self.color = color
        self.type = type
        self.size = size

    def __str__(self):
        return f"your dog's details are:- {self.color} {self.type} {self.size}"

    def hobby(self):
        print(f"{self.type} are hard to train (level 3/10)")
        
# louie = dog("black", "docshand", "small-size")
# print(louie)

# reggie = dog("golden", "golden-retriever", "big-size")
# print(reggie)

# lab = dog("white", "Labrador", "big-size")
# print(lab)

# class Toyota(car):
    
#     def __init__(self, color, model, make="toyota"):
#         super().__init__(color, model, make)
    
#     def drive(self):
#         print("Toyota Rules")    
            
# camry = Toyota("Blue", "Camry")
# print(camry)

# bmw = Toyota("Silver", "BMW")
# print(bmw)

# bmw.drive()


# Prompt 4: You Do
#
# Once we've completed the above, work through the following changes to your
# Car and Toyota classes:
#
#   - move the color property to your Toyota class
#   - move the drive method to your Car class
#   - add a property to your Toyota class
#   - add a property to your Car class and "fill it in" for your Toyota class
#
class car:
    
    def __init__(self, model, make):
        self.model = model
        self.make = make
    
    def __str__(self):
        return f"This is a {self.make} {self.model}"
        
        
instance1 = car("Ford", "Fusion")
print(instance1)

instance2 = car("GMC", "Acadia")
print(instance2)


class Toyota(car):
    
    def __init__(self, color, model, make="toyota", year="2020"):
        super().__init__(model, make)
        self.color = color
        self.year = year
          
    def drive(self):
        print(f"{self.model} has {self.color} color and goes Vroom Vroom")

            
camry = Toyota("Blue", "Camry", "2020")
print(camry)

bmw = Toyota("Silver", "lexus", "2019")
print(bmw)

bmw.drive()


#
# Prompt 5: You Do
#
# Define and Animal class with the following properties and methods:
#
#   - group (Invertebrates, Fish, Amphibians, Reptiles, Birds, and Mammals)
#   - eat: log "yum yum" to the console
#   - sleep: log "zzzzz" to the console
#
# Modify your animal from the previous prompt so that it extends your new
# Animal class.
#
# Create an instance of your animal class (the one that extends the Animal
# class).
#
class animal(dog):

    def __init__(self, color, type, size, group):
        super().__init__(color, type, size)
        self.group = group
    
    def __str__(self):
            return f"your dog's details are:- {self.color} {self.type} {self.size} {self.group}"
        
    def eat(self):
        print("yum yum")
    
    def sleep(self):
        print("zzzzz")

        
louie = animal("black", "docshand", "small-size", "Invertebrates")
print(louie)

reggie = animal("golden", "golden-retriever", "big-size", "Invertebrates")
print(reggie)

lab = animal("white", "Labrador", "big-size", "Invertebrates")
print(lab)

louie.eat()
louie.sleep()

#
# Prompt 6: You Do
#
# Define a Card class with the following properties:
#
#   - suit (hearts, spades, clubs, diamonds)
#   - rank (Ace, 2, 3, 4, .. Jack, King, Queen)
#   - score (1, 2, 3, 4, ... 11, 12, 13)
#
# Define a Deck class with the following properties and methods:
#
#   - length (the number of cards - should start at 52)
#   - cards (an array of cards in the deck)
#   - draw: return a random card from the cards array
#
# When you create an instance of your Deck class (i.e. in your constructor),
# fill in the cards array with 52 instances of your Card class. You can do
# this with a nested for loop - first loop through an array of all possible
# suits, then loop through an array of all possible ranks. Inside your inner
# loop, create an instance of your Card class and push it into the Deck's cards
# array.
#
# Instantiate an instance of your Deck and start drawing random cards!
#

import random


class Card:

    def __init__(self, suit, rank, score):
        self.suit = suit
        self.rank = rank
        self.score = score
        
    
class Deck:
    
    def __init__(self, length, cards):
        # super().__init__(suit, rank, score, length, cards)
        self.length = length
        self.cards = cards
        
    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            # for score in range(1, 14):
                for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                    # self.cards.append(Card(suit, score, rank))
                    self.cards.append(Card(suit, rank, score=""))
                    print(len(self.cards))

                    # return self.cards
    def draw(self):
        drawn_card = random.choice(self.cards)
        print(f"{drawn_card.rank} of {drawn_card.suit}")

                
deck = Deck(52, [])
deck.build()
deck.draw()

