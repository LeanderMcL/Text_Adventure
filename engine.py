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
			arguments = parser.is_move(look_arguments)
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
			this_door = doors.find_door(rooms.current_room.doors[arguments])
			if this_door.closed:
				action = "move closed"
				arguments = this_door
			else:
				other_exit = rooms.find_room(this_door.exits[arguments])
				arguments = other_exit
				rooms.previous_room = current_room
				rooms.current_room = other_exit
		else:
			action = "move direction error"
	response = output.generate_response(action,arguments)
	return response

def get_input():
	user_input = raw_input(output.prompt).lower()
	return user_input

def total_action(s):
	action, arguments = get_action(s)
	response = do_action(action,arguments)
	return response, action

def game_cycle(input_function):
	rooms.previous_room = rooms.current_room
	user_input = input_function()
	response, action = total_action(user_input)
	return response, action

def game_intro():
	intro = output.welcome + "\n" + rooms.current_room.show_full_desc()
	return intro
