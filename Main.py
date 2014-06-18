import re, rooms, doors, engine, output, parser

"""
print "---TEST--- get_argument"
print get_argument("look north"), "look north Should be north"
print get_argument("get fish"), "get fish Should be fish"
print get_argument("Bajorans"), "Should be False"
print "---END TEST---"

print "---TEST--- check_look_direction"
print check_look_direction("look north"), "look north Should be north"
print check_look_direction("l fish"), "l fish Should be fish"
print check_look_direction("gobbledegook"), "gobbledegook Should be False"

print "---TEST--- string matching"
print match_any(quit_strings,"exit please"), "exit please Should be True"
print match_any(look_strings,"look fish"), "look fish Should be True"
print match_any(move_strings,"dance north"), "dance north Should be True"
print match_any(quit_strings,"fish"), "fish Should be False"
print match_any(look_strings,"this string is gobbledegook"), " this string is gobbledegook Should be False"
print "---END TEST---"
"""

print "Welcome!"
current_room = rooms.current_room
print current_room.show_full_desc()

while True:
	rooms.previous_room = current_room
	user_input = raw_input("Enter a command: ").lower()
	print rooms.show_room()
	action, arguments = engine.get_action(user_input)
	response = output.generate_response(action,arguments)
	print response
	if action == "quit":
		break
	elif user_input in parser.move_strings:
		print "Sorry! I know you want to move, but I can't do that yet."
