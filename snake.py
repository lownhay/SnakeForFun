import random
import curses
import colors

scr = curses.initscr() #creat src
curses.curs_set(0)
sh, sw = scr.getmaxyx()
window = curses.newwin(sh, sw, 0, 0)
window.keypad(True)
window.timeout(50)
colors.create_colors()
live_nums = 3
snk_x = int(sh/4)
snk_y = int(sh/4)

snake = [
	[snk_y, snk_x],
	[snk_y, snk_x - 1],
	[snk_y, snk_x - 2]
]

window.bkgd(' ', curses.color_pair(5))

window.attron(curses.color_pair(1))
window.border('*', '*', '*', '*', '*', '*', '*', '*')
window.attroff(curses.color_pair(1))
food = [int(sh/2), int(sw/2)]



window.addch(food[0], food[1], 42, curses.color_pair(2))

key = curses.KEY_DOWN

while True:
	next_key = window.getch()
	#key = key if next_key == -1 else next_key
	key = key if (next_key == curses.KEY_DOWN and key == curses.KEY_UP or
	              next_key == curses.KEY_UP and key == curses.KEY_DOWN or
	              next_key == curses.KEY_LEFT and key == curses.KEY_RIGHT or
	              next_key == curses.KEY_RIGHT and key == curses.KEY_LEFT or
	              next_key == -1) else next_key

	new_head = snake[0].copy()

	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1
	if key == curses.KEY_LEFT:
		new_head[1] -= 1
		
	snake.insert(0, new_head)

	if snake[0] == food:
		food = None
		while food is None:
			new_food = [
				random.randint(1, sh - 1),
				random.randint(1, sw - 1)
			]
			food = new_food if new_food not in snake else None
		window.addch(food[0], food[1], 42, curses.color_pair(2))
	else:
		tail = snake.pop()
		window.addch(tail[0], tail[1], ' ')
		
	if snake[0][0] in [0, sh-1] or snake[0][1] in [0, sw-1] or snake[0] in snake[1:]:
		if live_nums > 0:
			live_nums -= 1
			for cors in snake[1:]:
				window.addch(cors[0], cors[1], ' ')
			snake = [
				[snk_y, snk_x],
				[snk_y, snk_x - 1],
				[snk_y, snk_x - 2]
			]
			key = curses.KEY_DOWN
		else:
			curses.endwin()
			quit()
	else:
		window.addch(snake[0][0], snake[0][1], 111, curses.color_pair(3))
	