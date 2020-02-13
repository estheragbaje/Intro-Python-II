from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [Item('Hats', 'headcover'), Item('Gloves', 'finger cover')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Hats', 'headcover'), Item('Gloves', 'finger cover')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('Hats', 'headcover'), Item('Gloves', 'finger cover')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('Hats', 'headcover'), Item('Gloves', 'finger cover')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Hats', 'headcover'), Item('Gloves', 'finger cover')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Declare all items
#


# Main
#
#Welcome note to new player
print("\nWelcome to the Adventure Game\n")
print("\nInstruction:\n Use keys n, s, e and w to move player in the North, South , East & West directions")

# Make a new player object that is currently in the 'outside' room.
player = Player("Player 1", room["outside"], [Item('Hats', 'headcover'), Item('Gloves', 'finger cover')]) 


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
  print("\nCurrent room:\n", player)
 

  user_input = input("\nEnter direction to move player to:\n")

  continueGame = player.move(room, user_input)

  if continueGame == False:
    break
  
