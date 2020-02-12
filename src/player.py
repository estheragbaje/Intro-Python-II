# Write a class to hold player information, e.g. what room they are in
# currently.
class Room:
  def __init__(self, name, description):
    self.name = name 
    self.description = description
    self.n_to = None  
    self.s_to = None
    self.e_to = None
    self.w_to = None