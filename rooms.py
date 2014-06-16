rooms_list = []

class Room(object):
	def __init__(self,name,short_desc,long_desc,doors):
		self.name = name
		self.short_desc = short_desc
		self.long_desc = long_desc
		self.doors = doors
		rooms_list.append(self)
	def show_room_name(self):
		return "You are in a " + self.name + "."
	def show_full_desc(self):
		return self.show_room_name() + "\n" + self.long_desc

def find_room(l,s):
	for i in l:
		if i.name == s:
			return i
	return False

current_room = "courtyard"
previous_room = ""

courtyard = Room("courtyard","A courtyard with ivy hanging from all the walls.","You find yourself in a cool courtyard, lined with buildings on all sides. Ivy covers each of the four walls, leaving only small gaps for the doors leading into the buildings. The floor is paved with stone slabs.",{"north": "iron door", "east": "glass door", "south": "wooden door", "west": "blue door"})

conservatory = Room("conservatory","A glass-domed conservatory.","You are in a glass-domed conservatory. This room is oddly bare, but for a couple of benches up against the back wall.",{"west": "glass door"})
