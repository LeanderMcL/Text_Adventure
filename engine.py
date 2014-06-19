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
	return action, arguments

def do_action(action,arguments):
	if action == "look direction":
		current_room = rooms.current_room
		if arguments in current_room.doors.keys():
			this_door_name = current_room.doors[arguments]
			this_door = doors.find_door(doors.doors_list,this_door_name)
			if this_door.closed:
				action = "look direction closed"
				arguments = this_door
			else:
				action = "look direction open"
				other_exit_name = this_door.exits[arguments]
				other_exit = rooms.find_room(rooms.rooms_list,other_exit_name)
				arguments = other_exit
		else:
			action = "look direction error"
	response = output.generate_response(action,arguments)
	return response

print "---TEST---"
print get_action("look north"), "Should be ('look direction', 'north')"
print do_action("look direction","north")
print do_action("look direction", "up")
print do_action("look direction", "south")
