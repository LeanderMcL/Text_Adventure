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
		response = self.show_room_name() + "\n" + self.long_desc + "\n" + self.show_doors()
		return response
	def show_doors(self):
		response = ""
		for key in self.doors:
			response = response + "There is a " + self.doors[key] + " to the " + key + ".\n"
		return response

def find_room(l,s):
	for i in l:
		if i.name == s:
			return i
	return False

def show_room():
	if current_room == previous_room:
		return current_room.show_room_name()
	else:
		return current_room.show_full_desc()

courtyard = Room("courtyard","A courtyard with ivy hanging from all the walls.","You find yourself in a cool courtyard, lined with buildings on all sides. Ivy covers each of the four walls, leaving only small gaps for the doors leading into the buildings. The floor is paved with stone slabs.",{"north": "iron door", "east": "glass door", "south": "wooden door", "west": "blue door"})

conservatory = Room("conservatory","A glass-domed conservatory.","You are in a glass-domed conservatory. This room is oddly bare, but for a couple of benches up against the back wall.",{"west": "glass door"})

ballroom = Room("ballroom","An empty, echoing ballroom.","This ballroom is huge. And very, very dusty: no one has been here in a long time. A chandelier, hung with cobwebs, hangs above the centre of the room. The furniture is very spare: a few chairs and small tables are shoved up against the walls, leaving a vast, empty dancefloor. A grand piano stands against one wall, also dusty and unused.",{"south":"iron door"})

kitchen = Room("kitchen","A dusty kitchen.","This kitchen was probably once cosy and warm. Now, all the counter-tops are covered in a thick layer of dust. So is the wooden table which stands in the centre of the room.",{"north":"wooden door"})

gardeners_alcove = Room("gardener's alcove","A gardener's alcove.","This alcove is little more than a hole in the western wall of the courtyard. A table, shoved against the back wall, is stacked with tools and gardening equipment. There is dust everywhere, and cobwebs hang from the corners of the tiny room.",{"east":"blue door"})

current_room = courtyard
previous_room = None

print courtyard.show_doors()
