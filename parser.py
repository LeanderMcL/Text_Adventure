import re, rooms, doors

def match_any(l,s):
	for i in l:
		match_regex = i + "\w"
		if re.match(match_regex,s):
			return True
	return False

def get_argument(s):
	split_string = s.split()
	join_string = " "
	argument = join_string.join(split_string[1:])
	if len(argument) > 0:
		return argument
	return False

def match(l,s):
	if s in l:
		return s
	return False

def is_quit(s):
	return match(quit_strings,s)

def is_look(s):
	return match(look_strings,s)

def is_look_with_args(s):
	if match_any(look_strings,s):
		return get_argument(s)

def is_move(s):
	for key in direction_map:
		if s in direction_map[key]:
			return key
	return False

# these lists contain the acceptable strings for various kinds of commands
quit_strings = ["quit", "exit", "x", "q"]
look_strings = ["l", "look"]
direction_map = {
	"north": ["north", "n"],
	"south": ["south", "s"],
	"east": ["east", "e"],
	"west": ["west", "w"],
	"up": ["up", "u"],
	"down": ["down", "d"]
}
