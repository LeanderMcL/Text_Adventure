import rooms, doors, parser

def get_action(s):
	action = None
	arguments = None
	if parser.is_quit(s):
		action = "quit"
	elif parser.is_look(s):
		action = "look"
	return action, arguments

def get_current_and_previous_rooms():
	pass	
