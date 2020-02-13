# Implement a class to hold room information. This should have name and
# description attributes.

#add items to a room
from item import Item

class Room:
  def __init__(self, name, description, item):
    self.name = name 
    self.description = description
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
    self.item = item

def add_item(self, item):
  self.extend(item)

def __repr__(self):
    return f"In room {self.name}. \n{self.description} \n{self.item}"