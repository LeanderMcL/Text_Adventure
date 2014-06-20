import unittest, rooms, doors, engine, output, parser

class TestParsing(unittest.TestCase):

# First: setting up a simple two-room game to test with

	test_room = rooms.Room("test room","This is the short description of the test room.","This is the long description of the test room.",{"north":"test door","west":"second test door"})
	second_test_room = rooms.Room("second test room","This is the short description of the second test room.","This is the long description of the second test room.",{"south":"test door","east":"second test door"})
	test_door = doors.Door("test door","Describing the test door.",{"south":"test room","north":"second test room"},True,False)
	second_test_door = doors.Door("second test door","This is the description of the second test door.",{"east":"test room","west":"second test room"},False,False)

# Test the rooms module

	def test_Room_attributes(self):
		self.assertEqual("test room",self.test_room.name,"Test room's name should be 'test room'")
		self.assertEqual("This is the short description of the test room.",self.test_room.short_desc)
		self.assertEqual("This is the long description of the test room.",self.test_room.long_desc)
		self.assertEqual({"north":"test door","west":"second test door"},self.test_room.doors)

	def test_Room_show_room_name(self):
		self.assertEqual("You are in a test room.",self.test_room.show_room_name())

	def test_Room_show_full_desc(self):
		self.assertEqual(self.test_room.show_room_name() + "\n" + self.test_room.long_desc + "\n" + self.test_room.show_doors(),self.test_room.show_full_desc())

	def test_Room_show_doors(self):
		self.assertTrue("There is a test door to the north." in self.test_room.show_doors())

	def test_find_room(self):
		self.assertEqual(rooms.find_room("test room"),self.test_room)

	def test_show_room(self):
		rooms.current_room = self.test_room
		rooms.previous_room = self.second_test_room
		self.assertNotEqual(rooms.previous_room,rooms.current_room)
		self.assertEqual(rooms.show_room(),rooms.current_room.show_full_desc())
		rooms.previous_room = rooms.current_room
		self.assertTrue(rooms.current_room == rooms.previous_room)
		self.assertEqual(rooms.show_room(),rooms.current_room.show_room_name())

# Test the doors module

	def test_Door_attributes(self):
		self.assertEqual(self.test_door.name,"test door")
		self.assertEqual(self.test_door.desc,"Describing the test door.")
		self.assertEqual(self.test_door.exits,{"south":"test room","north":"second test room"})
		self.assertEqual(self.test_door.closed,True)
		self.assertEqual(self.test_door.locked,False)

	def test_find_door(self):
		self.assertEqual(doors.find_door("test door"),self.test_door)

# Test the engine module where the game logic lives

	def test_get_action(self):
		self.assertEqual(engine.get_action("fish"),(None,None))
		self.assertEqual(engine.get_action("castle"),(None,None))
		self.assertEqual(engine.get_action("q"),("quit",None))
		self.assertEqual(engine.get_action("look"),("look",None))
		self.assertEqual(engine.get_action("look n"),("look direction","north"))
		self.assertEqual(engine.get_action("l n"),("look direction","north"))
		self.assertEqual(engine.get_action("look fish"),("look error","fish"))
		self.assertEqual(engine.get_action("north"),("move","north"))

	def test_do_action(self):
		rooms.current_room = self.test_room
		self.assertEqual(engine.do_action("look direction","north"),self.test_door.desc)
		self.assertEqual(engine.do_action("look direction","west"),self.second_test_room.short_desc)
		self.assertEqual(engine.do_action("look direction","up"),output.look_direction_error)
		self.assertEqual(engine.do_action("move","west"),self.second_test_room.show_full_desc())
		self.assertEqual(rooms.current_room,self.second_test_room)
		self.assertEqual(engine.do_action("move","south"),output.move_closed_error(self.test_door.name))
		self.assertEqual(engine.do_action("move","up"),output.move_direction_error)
		self.assertEqual(engine.do_action("look error","fish"),output.look_error("fish"))

# NB: Not bothering to test get_input(), which only grabs the string from raw_input()

	def test_total_action(self):
		rooms.current_room = self.test_room
		self.assertEqual(engine.total_action("look"),(rooms.current_room.long_desc,"look"))
		self.assertEqual(engine.total_action("south"),(output.move_direction_error,"move"))
		self.assertEqual(engine.total_action("north"),(output.move_closed_error("test door"),"move"))
		self.assertEqual(engine.total_action("west"),(rooms.current_room.show_full_desc(),"move"))
		self.assertEqual(engine.total_action("fish"),(output.error_no_action,None))
		self.assertEqual(engine.total_action("look south"),(self.test_door.desc,"look direction"))
		self.assertEqual(engine.total_action("look north"),(output.look_direction_error,"look direction"))
		self.assertEqual(engine.total_action("look east"),(self.test_room.short_desc,"look direction"))
		self.assertEqual(engine.total_action("look fish"),(output.look_error("fish"),"look error"))
		self.assertEqual(engine.total_action(""),(output.error_no_action,None))

	def test_game_cycle(self):
		rooms.current_room = self.test_room
		self.assertEqual(engine.game_cycle(lambda:"hello"),(output.error_no_action,None))
		self.assertEqual(engine.game_cycle(lambda:"look"),(rooms.current_room.long_desc,"look"))
		self.assertEqual(engine.game_cycle(lambda:"south"),(output.move_direction_error,"move"))
		self.assertEqual(engine.game_cycle(lambda:"north"),(output.move_closed_error("test door"),"move"))
		self.assertEqual(engine.game_cycle(lambda:"west"),(rooms.current_room.show_full_desc(),"move"))
		self.assertEqual(engine.game_cycle(lambda:"look south"),(self.test_door.desc,"look direction"))
		self.assertEqual(engine.game_cycle(lambda:"look north"),(output.look_direction_error,"look direction"))
		self.assertEqual(engine.game_cycle(lambda:"look east"),(self.test_room.short_desc,"look direction"))
		self.assertEqual(engine.game_cycle(lambda:"look fish"),(output.look_error("fish"),"look error"))
		self.assertEqual(engine.game_cycle(lambda:""),(output.error_no_action,None))

	def test_game_intro(self):
		self.assertEqual(engine.game_intro(),output.welcome + "\n" + rooms.current_room.show_full_desc())

# Test the output module which generates strings for the output

	def test_generate_response(self):
		self.assertEqual(output.generate_response(None,None),output.error_no_action)
		self.assertEqual(output.generate_response("quit",None),output.quit_message)
		self.assertEqual(output.generate_response("look",None),output.rooms.current_room.long_desc)
		self.assertEqual(output.generate_response("look direction closed",self.test_door),self.test_door.desc)
		self.assertEqual(output.generate_response("look direction open",self.test_room),self.test_room.short_desc)
		self.assertEqual(output.generate_response("look direction error",None),output.look_direction_error)
		self.assertEqual(output.generate_response("look error","fish"),output.look_error("fish"))
		self.assertEqual(output.generate_response("move",self.test_room),self.test_room.show_full_desc())
		self.assertEqual(output.generate_response("move direction error",None),output.move_direction_error)
		self.assertEqual(output.generate_response("move closed",self.test_door),output.move_closed_error(self.test_door.name))
		self.assertEqual(output.generate_response("garbage","garbage"),output.error_no_action)

	def test_move_closed_error(self):
		self.assertEqual(output.move_closed_error("test door"),"The test door is closed.")

# Test the parser module which parses the input given by the user

	def test_match_any(self):
		self.assertEqual(parser.match_any(parser.look_strings,"look east"),True)
		self.assertEqual(parser.match_any(parser.quit_strings,"look east"),False)
		self.assertEqual(parser.match_any(parser.look_strings,"l east"),True)
		self.assertEqual(parser.match_any(parser.quit_strings,"l east"),False)

	def test_get_argument(self):
		self.assertEqual(parser.get_argument("look north"),"north")
		self.assertEqual(parser.get_argument("get fish"),"fish")
		self.assertEqual(parser.get_argument("Bajorans"),False)
		self.assertEqual(parser.get_argument(""),False)

	def test_match(self):
		self.assertEqual(parser.match(parser.look_strings,"l"),"l")
		self.assertEqual(parser.match(parser.look_strings,"q"),False)
		self.assertEqual(parser.match(parser.look_strings,""),False)

	def test_is_quit(self):
		self.assertEqual(parser.is_quit("quit"),"quit")
		self.assertEqual(parser.is_quit("q"),"q")
		self.assertEqual(parser.is_quit("look"),False)
		self.assertEqual(parser.is_quit(""),False)

	def test_is_look(self):
		self.assertEqual(parser.is_look("look"),"look")
		self.assertEqual(parser.is_look("l"),"l")
		self.assertEqual(parser.is_look("north"),False)
		self.assertEqual(parser.is_look(""),False)

	def test_is_look_with_args(self):
		self.assertEqual(parser.is_look_with_args("look args"),"args")
		self.assertEqual(parser.is_look_with_args("l args"),"args")
		self.assertEqual(parser.is_look_with_args("l east"),"east")

	def test_is_move(self):
		self.assertEqual(parser.is_move("north"),"north")
		self.assertEqual(parser.is_move("e"),"east")
		self.assertEqual(parser.is_move("gobbledegook"),False)
		self.assertEqual(parser.is_move(""),False)

if __name__ == "__main__":
	unittest.main()
	
