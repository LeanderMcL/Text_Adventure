import unittest, rooms, doors, engine, output, parser

class TestParsing(unittest.TestCase):

	test_room = rooms.Room("test room","This is the short description of the test room.","This is the long description of the test room.",{"north":"test door","west":"second test door"})
	second_test_room = rooms.Room("second test room","This is the short description of the second test room.","This is the long description of the second test room.",{"south":"test door","east":"second test door"})
	test_door = doors.Door("test door","Describing the test door.",{"south":"test room","north":"second test room"},True,False)
	second_test_door = doors.Door("second test door","This is the description of the second test door.",{"east":"test room","west":"second test room"},False,False)

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
		self.assertNotEqual(rooms.previous_room,rooms.current_room)
		self.assertEqual(rooms.show_room(),rooms.current_room.show_full_desc())
		rooms.previous_room = rooms.current_room
		self.assertTrue(rooms.current_room == rooms.previous_room)
		self.assertEqual(rooms.show_room(),rooms.current_room.show_room_name())

	def test_Door_attributes(self):
		self.assertEqual(self.test_door.name,"test door")
		self.assertEqual(self.test_door.desc,"Describing the test door.")
		self.assertEqual(self.test_door.exits,{"south":"test room","north":"second test room"})
		self.assertEqual(self.test_door.closed,True)
		self.assertEqual(self.test_door.locked,False)

	def test_find_door(self):
		self.assertEqual(doors.find_door("test door"),self.test_door)

	def test_get_action(self):
		self.assertEqual(engine.get_action("fish"),(None,None))
		self.assertEqual(engine.get_action("castle"),(None,None))
		self.assertEqual(engine.get_action("q"),("quit",None))
		self.assertEqual(engine.get_action("look"),("look",None))
		self.assertEqual(engine.get_action("look n"),("look direction","north"))
		self.assertEqual(engine.get_action("look fish"),("look error",None))
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

	def test_generate_response(self):
		self.assertEqual(output.generate_response(None,None),output.error_no_action)
		self.assertEqual(output.generate_response("quit",None),output.quit_message)
		self.assertEqual(output.generate_response("look",None),output.rooms.current_room.long_desc)
		self.assertEqual(output.generate_response("look direction closed",self.test_door),self.test_door.desc)
		self.assertEqual(output.generate_response("look direction open",self.test_room),self.test_room.short_desc)
		self.assertEqual(output.generate_response("look direction error",None),output.look_direction_error)
		self.assertEqual(output.generate_response("move",self.test_room),self.test_room.show_full_desc())
		self.assertEqual(output.generate_response("move direction error",None),output.move_direction_error)
		self.assertEqual(output.generate_response("move closed",self.test_door),output.move_closed_error(self.test_door.name))
		self.assertEqual(output.generate_response("garbage","garbage"),output.error_no_action)

	def test_move_closed_error(self):
		self.assertEqual(output.move_closed_error("test door"),"The test door is closed.")

	def test_match_any(self):
		self.assertEqual(parser.match_any(parser.look_strings,"look east"),True)
		self.assertEqual(parser.match_any(parser.quit_strings,"look east"),False)

	def test_get_argument(self):
		self.assertEqual(parser.get_argument("look north"),"north")
		self.assertEqual(parser.get_argument("get fish"),"fish")
		self.assertEqual(parser.get_argument("Bajorans"),False)

	def test_match(self):
		self.assertEqual(parser.match(parser.look_strings,"l"),"l")
		self.assertEqual(parser.match(parser.look_strings,"q"),False)

	def test_is_quit(self):
		self.assertEqual(parser.is_quit("quit"),"quit")
		self.assertEqual(parser.is_quit("q"),"q")
		self.assertEqual(parser.is_quit("look"),False)

	def test_is_look(self):
		self.assertEqual(parser.is_look("look"),"look")
		self.assertEqual(parser.is_look("l"),"l")
		self.assertEqual(parser.is_look("north"),False)

	def test_is_move(self):
		self.assertEqual(parser.is_move("north"),"north")
		self.assertEqual(parser.is_move("e"),"east")
		self.assertEqual(parser.is_move("gobbledegook"),False)

if __name__ == "__main__":
	unittest.main()
	
