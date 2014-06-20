import engine, rooms

def main():
	print engine.game_intro()
	while True:
		response, action = engine.game_cycle(engine.get_input)
		print response
		if action == "quit":
			break
		print rooms.show_room()

if __name__ == '__main__':
    main()
