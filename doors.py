doors_list = []

class Door(object):
	def __init__(self,name,desc,exits,closed,locked):
		self.name = name
		self.desc = desc
		self.exits = exits
		self.closed = closed
		self.locked = locked
		doors_list.append(self)

def find_door(l,s):
	for i in l:
		if i.name == s:
			return i
	return False

glass_door = Door("glass door","A glass door.",{"west": "courtyard","east":"conservatory"},True,False)
iron_door = Door("iron door","An iron door.",{"south": "courtyard","north":"ballroom"},True,True)
wooden_door = Door("wooden door","A wooden door.",{"east": "courtyard","north":"kitchen"},True,False)
blue_door = Door("blue door","A door painted in cracked blue paint.",{"north": "courtyard","south": "gardener's alcove"},True,False)
