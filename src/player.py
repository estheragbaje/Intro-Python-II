# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
  def __init__(self, name, current_room):
    self.name = name 
    self.current_room = current_room
  #adding method to the class
  def __str__(self):
    return f"Player {self.name} is in room {self.current_room}"

  def move(self, room, user_input):
    
    continueGame = True

    if user_input == 'n':
      if self.current_room == room["outside"]:
        self.current_room = room["foyer"]

      
      elif self.current_room == room["foyer"]:
        self.current_room = room["overlook"]
      
      else:
        print("Movement isn't allowed")
        continueGame = True


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