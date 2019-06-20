import curses

def create_colors():
	curses.start_color()
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
	curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLACK)