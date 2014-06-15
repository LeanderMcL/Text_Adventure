import rooms

quit_strings = ["quit", "exit", "x", "q"]
look_strings = ["l", "look"]
move_strings = ["north", "south", "east", "west", "up", "down"]

print "Welcome!"
current_room = rooms.find_current_room(rooms.rooms_list)
print current_room.show_full_desc()

while True:
	current_room = rooms.find_current_room(rooms.rooms_list)
	rooms.previous_room = current_room.name
	user_input = raw_input("Enter a command: ").lower()
	if user_input in quit_strings:
		print "Bye!"
		break
	elif user_input in look_strings:
		print current_room.long_desc
	elif user_input in move_strings:
		print "Sorry! I know you want to move, but I can't do that yet."
	else:
		print "Sorry, I don't know how to parse that command yet."
		print current_room.show_room_name()
