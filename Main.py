import rooms, doors

# these lists contain the acceptable strings for various kinds of commands
quit_strings = ["quit", "exit", "x", "q"]
look_strings = ["l", "look"]
move_strings = ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]
# there is a probably a way to combine all the legal look strings and all the legal move strings
# with a list comprehension but I can't think of it right now
look_direction_strings = ["look north", "look south", "look east", "look west", "look up", "look down"]

print "Welcome!"
current_room = rooms.find_room(rooms.rooms_list,rooms.current_room)
print current_room.show_full_desc()

while True:
	current_room = rooms.find_room(rooms.rooms_list,rooms.current_room)
	rooms.previous_room = current_room.name
	user_input = raw_input("Enter a command: ").lower()
	if user_input in quit_strings:
		print "Bye!"
		break
	elif user_input in look_strings:
		print current_room.long_desc
	elif user_input in move_strings:
		print "Sorry! I know you want to move, but I can't do that yet."
	elif user_input in look_direction_strings:
		print "Sorry! I know you want to look in a direction, but I can't do that yet."
	else:
		print "Sorry, I don't know how to parse that command yet."
		print current_room.show_room_name()
