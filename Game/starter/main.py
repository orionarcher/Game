from room import Room
from player import Player
from item import Item
from monster import Monster
from npc import Jani
import os
import updater

player = Player()

def createWorld():
    manager = Room("You are in your manager's  office")
    mailroom = Room("You are in the mail room")
    customer = Room("You are the customer service room")
    janitor = Room("You are in the janitor's closet")
    accountant = Room("You are in the accountants office")
    liability = Room("You are in the liability office")
    bathroom = Room("You are in the bathroom")
    office = Room("You are in your own office")

    Room.connectRooms(manager, "mail-room", mailroom, "management")
    Room.connectRooms(manager, "accounting", accountant, "management")
    Room.connectRooms(customer, "mail-room", mailroom, "customer-service")
    Room.connectRooms(customer, "accounting", accountant, "customer-service")
    Room.connectRooms(customer, "janitors-closet", janitor, "customer-service")
    Room.connectRooms(janitor,"liability",liability,"janitors-closet")
    Room.connectRooms(liability,"accounting",accountant,"liability")
    Room.connectRooms(liability, "bathroom", bathroom, "liability")
    Room.connectRooms(accountant,"your-office",office,"accounting")

    i = Item("Rock", "This is just a rock.")
    i.putInRoom(office)
    player.location = accountant
    Monster("Bob the monster", 20, office)
    Jani("Jani", liability, player) # this is how you make NPC's

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasPeople():
        print("This room contains the following people:") # not monsters
        for p in player.location.people:
            print(p.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go to following rooms:")
    for e in player.location.exitNames():
        print(e)
    print()
    print()

def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("cases -- shows your current cases")
    print("describe <case> -- gives description and difficulty of case")
    print("pickup <item> -- picks up the item")
    print("talk <person> -- talks to a person")
    print("argue <case> -- enter the courtroom to argue your case")
    print()
    input("Press enter to continue...")



createWorld()
playing = True
while playing and player.alive:
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()

#### BASICS ####
        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            player.goDirection(commandWords[1]) 
            timePasses = True
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "exit":
            playing = False

#### INVENTORY ####
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "inventory":
            player.showInventory()

#### CASES ####
        elif commandWords[0].lower() == "cases": #lists cases
            player.showCases()
        elif commandWords[0].lower() == "describe": #describes one case
            targetCase = command[9:]
            target = player.getCaseByName(targetCase)
            if target != False:
                print(target.desc)
            else:
                print("No such case.")
                commandSuccess = False

        elif commandWords[0].lower() == "argue": # this enters the case named <case>
            enterCase = command[6:]
            for i in cases:
                if i == enterCase:
                    enterCase.battle()
                else:
                    print("No such case.")


#### INTERACT ####
        elif commandWords[0].lower() == "attack": # needs to be reworked
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")
                commandSuccess = False
        elif commandWords[0].lower() == "talk": # initiate conversation with NPC
            targetName = command[5:]
            target = player.location.getPeopleByName(targetName)
            if target != False:
                target.talk()
            else:
                print("No such person.")
        else:
            print("Not a valid command")
            commandSuccess = False

    if timePasses == True:
        updater.updateAll()
