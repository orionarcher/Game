import random
import updater
from item import Case

class Person:
    def __init__(self, name, room, player):
        self.name = name
        self.room = room
        self.meetings = 0 #each time you talk to the person this stat goes up
        self.player = player #this makes sure we can modify the players stats
        room.addPerson(self)
        updater.register(self)
    def update(self):
        None


#### People ####

class Jani(Person): # Jani works in the liability department right now
    def __init__(self, name, room, player):
        Person.__init__(self, name, room, player) # using the previous init function
        self.desc = "Jani is a short greasy man."

    def talk(self):
        if self.meetings == 0: # I know this is ugly but it is easy to modify
            print("""
You see a short greasy man working at his desk. As you enter, he approaches:

Hey, I'm Jani, I'm the liability guy. I have some work for you. This damn 
orphanage happens to be in the path of a clients highway project. If could get
the project approved by the DOT. That'd be great.
""")
            print("""'superhighway' added to cases""")
            casedescription = """
RoadCorp has spent seven years developing the SuperRoad project, which will
connect RoadCorp's two corporate offices. Unfortunately, the 'Orphanage for
orphans with terminal diseases' happens to be right in the path of the 
road! You need to clear up this misunderstanding by rezoning the property as
an industrial site so that the 'Orphanage for orphans with terminal diseases'
can be demolished as quickly as possible. Difficulty 1.
"""
            newcase = Case("superhighway", casedescription, 1)
            self.player.cases.append(newcase) #modify players cases
            self.meetings += 1
        elif self.meetings == 1: # this is throwaway code rn
            print("Oh, you again.")
            self.meetings += 1
        elif self.meetings > 1:
            print("get the fuck out of here and never come back")
            self.meetings += 1