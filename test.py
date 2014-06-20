import unittest, rooms, doors, engine, output

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
		self.assertEqual(engine.do_action("move","south"),output.move_closed_error(self.test_door.name))
		self.assertEqual(engine.do_action("move","up"),output.move_direction_error)
"""
    def test_get_argument(self):
        self.assertEqual('north', get_argument("look north"), "look north Should be north")
        self.assertEqual('fish', get_argument("get fish"), "get fish Should be fish")
        self.assertEqual(False, get_argument("Bajorans"), "Should be False")

    def test_check_look_direction(self):
        self.assertEqual('north', check_look_direction("look north"), "look north Should be north")
        self.assertEqual('fish', check_look_direction("l fish"), "l fish Should be fish")
        self.assertEqual(False, check_look_direction("gobbledegook"), "gobbledegook Should be False")

    def test_string_matching(self):
        self.assertEqual(True, match_any(quit_strings,"exit please"), "exit please Should be True")
        self.assertEqual(True, match_any(look_strings,"look fish"), "look fish Should be True")
        self.assertEqual(True, match_any(move_strings,"dance north"), "dance north Should be True")
        self.assertEqual(False, match_any(quit_strings,"fish"), "fish Should be False")
        self.assertEqual(False, match_any(look_strings,"this string is gobbledegook"), " this string is gobbledegook Should be False")
"""
if __name__ == '__main__':
    unittest.main()

