import rooms, parser

def generate_response(action,arguments):
	if not action:
		return error_no_action
	elif action == "quit":
		return quit_message
	elif action == "look":
		return rooms.current_room.long_desc
	return True

error_no_action = "I have no idea what you're talking about."
quit_message = "Thanks for playing!\nGoodbye!"
