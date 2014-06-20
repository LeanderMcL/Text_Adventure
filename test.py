import unittest, rooms, doors

class TestParsing(unittest.TestCase):
	test_room = rooms.Room("test room","This is the short description of the test room.","This is the long description of the test room.",{"north":"test door","west":"second test door"})
	second_test_room = rooms.Room("second test room","This is the short description of the second test room.","This is the long description of the second test room.",{"south":"test door","east":"second test door"})
	test_door = doors.Door("test door","Describing the test door.",{"south":"test room","north":"second test room"},True,False)
	second_test_door = doors.Door("second test door","This is the description of the second test door.",{"east":"test room","west":"second test room"},False,False)
	def test_Room_attributes(self):
		self.assertEqual("test room",self.test_room.name,"Test room's name should be 'test room'")
		self.assertEqual("This is the short description of the test room.",self.test_room.short_desc,"Should spit out the short description of the test room")
		self.assertEqual("This is the long description of the test room.",self.test_room.long_desc,"Should spit out the long description of the test room")
		self.assertEqual({"north":"test door","west":"second test door"},self.test_room.doors,"Should spit out the doors for the test room.")

	def test_Room_show_room_name(self):
		self.assertEqual("You are in a test room.",self.test_room.show_room_name(),"Should be 'You are in a test room.'")

	def test_Room_show_full_desc(self):
		self.assertEqual(self.test_room.show_room_name() + "\n" + self.test_room.long_desc + "\n" + self.test_room.show_doors(),self.test_room.show_full_desc(),"Should show the full description of the room.")

	def test_Room_show_doors(self):
		self.assertTrue("There is a test door to the north." in self.test_room.show_doors(),"North exit should show up in show_doors.")

	def test_find_room(self):
		self.assertEqual(rooms.find_room("test room"),self.test_room,"Should be able to find test room.")

	def test_show_room(self):
		rooms.current_room = self.test_room
		self.assertNotEqual(rooms.previous_room,rooms.current_room,"Previous room and current room should be unequal before assignment")
		self.assertEqual(rooms.show_room(),self.test_room.show_full_desc(),"Should show full description of room while current room and previous room are unequal.")
		rooms.previous_room = rooms.current_room
		self.assertTrue(rooms.current_room == rooms.previous_room,"Current room and previous room should be equal after reassignment.")
		self.assertEqual(rooms.show_room(),self.test_room.show_room_name(),"Should show only the room name while current room and previous room are equal.")

	def test_Door_attributes(self):
		self.assertEqual(self.test_door.name,"test door","Should spit out the name of the test door.")
		self.assertEqual(self.test_door.desc,"Describing the test door.","Should spit out the description of the test door.")
		self.assertEqual(self.test_door.exits,{"south":"test room","north":"second test room"},"Should spit out the exits for the test door.")
		self.assertEqual(self.test_door.closed,True,"The test door should be closed.")
		self.assertEqual(self.test_door.locked,False,"The test door should not be locked.")

	def test_find_door(self):
		self.assertEqual(doors.find_door("test door"),self.test_door,"Should be able to find the test door.")

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

