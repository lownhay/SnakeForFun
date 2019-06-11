import random
import curses

scr = curses.initscr() #creat src
curses.curs_set(0)
sh, sw = scr.getmaxyx()
window = curses.newwin(sh, sw, 0, 0)
window.keypad(True)
window.timeout(50)

snk_x = int(sh/4)
snk_y = int(sh/4)

snake = [
	[snk_y, snk_x],
	[snk_y, snk_x - 1],
	[snk_y, snk_x - 2]
]

food = [int(sh/2), int(sw/2)]

window.addch(food[0], food[1], '*')

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
		window.addch(food[0], food[1], '*')
	else:
		tail = snake.pop()
		window.addch(tail[0], tail[1], ' ')
		
	if snake[0][0] in [-1, sh] or snake[0][1] in [-1, sw] or snake[0] in snake[1:]:
		curses.endwin()
		quit()
	else:
		window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
	