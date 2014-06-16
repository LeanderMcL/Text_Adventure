class Door(object):
	def __init__(self,name,desc,exits,closed,locked):
		self.name = name
		self.desc = desc
		self.exits = exits
		self.closed = closed
		self.locked = locked

glass_door = Door("glass door","A glass door.",{"west": "courtyard","east":"conservatory"},True,False)
