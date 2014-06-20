import rooms, doors, engine, output, parser

def main():
	print "Welcome!"
	print rooms.current_room.show_full_desc()

	while True:
		rooms.previous_room = rooms.current_room
		user_input = raw_input("Enter a command: ").lower()
		action, arguments = engine.get_action(user_input)
		response = engine.do_action(action,arguments)
		print response
		if action == "quit":
			break
		print rooms.show_room()

if __name__ == '__main__':
    main()
