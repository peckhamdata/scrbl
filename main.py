import curses

DOWN = 258
UP = 259
LEFT = 260
RIGHT = 261


def box():
    return [(0,0,'+'),(0,1,'-'),(0,2,'+'),
            (1,0,'|'),(1,1,' '),(1,2,'|'),
            (2,0,'+'),(2,1,'-'),(2,2,'+')]

def cursor():
    return [(0,0,'='),(0,1,'='),(0,2,'='),
            (1,0,'|'),(1,1,' '),(1,2,'|'),
            (2,0,'='),(2,1,'='),(2,2,'=')]

def render(shape, x, y):
    for char in shape:
        screen.addstr(char[0] + x, char[1] + y, char[2])

print("Preparing to initialize screen...")
screen = curses.initscr()
print("Screen initialized.")

tile_size = 3
board_width = 15
board_height = 15

x_offsets = range(0, board_width * (tile_size -1), tile_size -1)
y_offsets = range(0, board_height * (tile_size -1), tile_size -1)
for x in x_offsets:
    for y in y_offsets:
        render(box(), y, x)

x = 1
y = 1


render(cursor(), y_offsets[y], x_offsets[x])

screen.refresh()

curses.noecho()
screen.keypad(True)  # Maybe not perfect, but a good start?

while True:

    k = screen.getch()
    render(box(), y_offsets[y], x_offsets[x])
    curses.flushinp()
    if k == UP:
        y = y - 1
        if y < 0:
            y = 0;
    if k == DOWN:
        y = y + 1
        if y >= board_height:
            y = board_height -1
    if k == LEFT:
        x = x - 1
        if x < 0:
            x = 0
    if k == RIGHT: 
        x = x + 1
        if x >= board_width:
            x = board_width -1 
        
    render(cursor(), y_offsets[y], x_offsets[x])
