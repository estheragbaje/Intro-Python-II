# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
#player had an item so we need to import item
from item import Item

class Player:
  def __init__(self, name, current_room, item):
    self.name = name 
    self.current_room = current_room
    self.item = item
  #adding method to the class

  def add_item(self, item):
    self.extend(item)

  def move(self, room, user_input):
    
    continueGame = True

    split = user_input.split(' ')
    if user_input == 'n':
      if self.current_room == room["outside"]:
        self.current_room = room["foyer"]

      
      elif self.current_room == room["foyer"]:
        self.current_room = room["overlook"]
      
      else:
        print("Movement isn't allowed")
        continueGame = False


    elif user_input == 's':
      if self.current_room == room["foyer"]:
        self.current_room = room["outside"]
      
      elif self.current_room == room["overlook"]:
        self.current_room = room["foyer"]
      
      else:
        print("Movement isn't allowed")
        continueGame = False

    elif user_input == 'e':
      if self.current_room == room["foyer"]:
        self.current_room = room["narrow"]
      
      else:
        print("Movement isn't allowed")
        continueGame = False

    elif user_input == 'w':
      if self.current_room == room["narrow"]:
        self.current_room = room["foyer"]
      
      else:
        print("Movement isn't allowed")
        continueGame = False
  
    elif user_input == 'q':
      print("Thanks for playing. Bye")

    else:
      print("Invalid input, there's no room there. \nEnter again")
    
    return continueGame

  def __str__(self):
    return f"Player {self.name} is in room {self.current_room} and has {self.item}"