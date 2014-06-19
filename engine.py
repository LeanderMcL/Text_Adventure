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
	response = output.generate_response(action,arguments)
	return response

print "---TEST---"
print get_action("look north"), "Should be ('look direction', 'north')"
