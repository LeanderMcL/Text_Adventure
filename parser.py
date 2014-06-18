import pyparsing, rooms, doors

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

def check_look_at(s):
	if match_any(look_strings,s):
		direction = get_argument(s)
		return direction
	return False

def match(l,s):
	if s in l:
		return s
	return False

def is_quit(s):
	return match(quit_strings,s)

def is_look(s):
	return match(look_strings,s)

# these lists contain the acceptable strings for various kinds of commands
quit_strings = ["quit", "exit", "x", "q"]
look_strings = ["l", "look"]
move_strings = ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]

print "---TEST---"
print is_quit("quit"), "is_quit('quit') Should be 'quit'"
print is_quit("look"), "is_quit('look') Should be False"
print match(quit_strings,"quit"), "match(quit_strings,'quit'), Should be 'quit'"
print match(quit_strings,"look"), "match(quit_strings,'look'), Should be False"
