import os # changed 8:13

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.cases = [] # the cases
        self.health = 50
        self.alive = True


#### ACTIONS####
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)

#### CASES ####
    def showCases(self): # lists cases by name
        clear()
        print("Your current assignments are:")
        print()
        for i in self.cases:
            print(i.name)
        print()
        input("Press enter to continue...")
    def addCase(self, case):
        self.cases.append(case)
    def getCaseByName(self, name): # returns the case itself, not the name
        for i in self.cases:
            if i.name.lower() == name.lower():
                return i
        return False

#### ITEMS ####
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")

#### COMBAT ####
    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")
