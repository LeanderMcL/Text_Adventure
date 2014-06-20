import rooms, parser

def generate_response(action,arguments):
	response = error_no_action
	if action == "quit":
		response = quit_message
	elif action == "look":
		response = rooms.current_room.long_desc
	elif action == "look direction closed":
		response = arguments.desc
	elif action == "look direction open":
		response = arguments.short_desc
	elif action == "look direction error":
		response = look_direction_error
	elif action == "move":
		response = arguments.show_full_desc()
	elif action == "move direction error":
		response = move_direction_error
	elif action == "move closed":
		response = move_closed_error(arguments.name)
	return response

error_no_action = "I have no idea what you're talking about."
quit_message = "Thanks for playing!\nGoodbye!"
look_error = "You can't look at that!"
look_direction_error = "There's nothing to look at in that direction."
move_direction_error = "You can't go that way."

def move_closed_error(s):
	response = "The %s is closed." % s
	return response
