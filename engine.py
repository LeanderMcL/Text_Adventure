import rooms, doors, parser, output

def get_action(s):
	action = None
	arguments = None
	if parser.is_quit(s):
		action = "quit"
	elif parser.is_look(s):
		action = "look"
	elif parser.is_look_with_args(s):
		look_arguments = parser.is_look_with_args(s)
		if parser.is_move(look_arguments):
			action = "look direction"
			arguments = look_arguments
		else:
			action = "look error"
	elif parser.is_move(s):
		action = "move"
		arguments = parser.is_move(s)
	return action, arguments

def do_action(action,arguments):
	if action == "look direction":
		current_room = rooms.current_room
		if arguments in current_room.doors.keys():
			this_door = doors.find_door(current_room.doors[arguments])
			if this_door.closed:
				action = "look direction closed"
				arguments = this_door
			else:
				action = "look direction open"
				other_exit = rooms.find_room(this_door.exits[arguments])
				arguments = other_exit
		else:
			action = "look direction error"
	elif action == "move":
		current_room = rooms.current_room
		if arguments in current_room.doors.keys():
			this_door = get_door(rooms.current_room.doors[arguments])
			if this_door.closed:
				action = "move closed"
				arguments = this_door.name
			else:
				other_exit = get_room(this_door.exits[arguments])
				arguments = other_exit
				rooms.previous_room = current_room
				rooms.current_room = other_exit
		else:
			action = "move direction error"
	response = output.generate_response(action,arguments)
	return response

print "---TEST---"
print get_action("look north"), "Should be ('look direction', 'north')"
print do_action("look direction","north")
print do_action("look direction", "up")
print do_action("look direction", "south")
