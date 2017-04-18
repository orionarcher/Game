import os
import room
import monster

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item: # you have work to do here
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)



# Cases are a type of item that is stored in a seperate inventory

# They trigger a combat sequence when activated, and give a reward if defeated

class Case(Item): # this is an adaptation of item code
    def __init__(self, name, desc, difficulty, open=True):
        self.name = name
        self.desc = desc
    def battle(self): # this is thoroughly incomplete, i will finish this 4/18

        print("Today we hear litigation on the case:")
        print("People v. " + str(self.name))
        print("The case involves the following: ")
        print(self.desc)
        courtroom = Room("You are in the courtroom")
        courtroom.addExit(str(player.location), player.location)
        player.location = courtroom
        case = Monster(name, difficulty*5, courtroom)
