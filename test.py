import unittest

from Main import get_argument, check_look_direction, match_any, quit_strings, move_strings, look_strings

class TestParsing(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()

