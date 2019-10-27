import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.colors as mcolors

class ant:

    # Direction
    antUp = 0
    antRight = 1
    antDown = 2
    antLeft = 3
    # Movement
    turnRight = 0
    turnLeft = 1
    # Colors: Movement
    color_data = dict()
    antBlue = 0 # Color 0
    White = 1   # Color 1
    color_data[White] = turnRight
    Black = 2   # Color 2
    color_data[Black] = turnLeft
    Red = 3     # Color 3
    color_data[Red] = turnRight
    Green = 4   # Color 4
    color_data[Green] = turnLeft
    Yellow = 5
    color_data[Yellow] = turnRight
    color_dataStr = ['Blue', 'White', 'Black', 'Red', 'Green', 'Yellow']  # Color list
    # Iterations per draw
    max_i = 1000
    # Value board
    max_N = 250
    nextGen_board = np.ones((max_N, max_N))

    # IGNORE # Initialize board with values if iterations per draw
    #nextGen_board[0, 0] = Black
    #nextGen_board[0, 1] = Red
    #nextGen_board[0, 2] = Green
    #nextGen_board[0, 3] = antBlue

    # Initialize with position and direction
    def __init__(self):
        # Semi-random position (more or less middle of board)
        self.y = ant.max_N//2
        self.x = ant.max_N//2
        #Random direction
        self.direction = random.randrange(0, 4)

    # Move ant
    def move(self):
        # Ant board
        currentGen_board = ant.nextGen_board.copy()
        self.antPosition(currentGen_board)
        # Limit edges
        if((self.y > 1) and (self.y < ant.max_N-1) and (self.x > 1) and (self.x < ant.max_N-1)):
            # Range through each color until match is found
            for color in range(1, len(ant.color_data)+1):
                if(ant.nextGen_board[self.y, self.x] == color):
                    self.directionColor(color)
        return currentGen_board

    # Set ant position
    def antPosition(self, currentGen_board):
        # Ant blue
        currentGen_board[self.y, self.x] = ant.antBlue

    # Change ant direction and previous color
    def directionColor(self, color):
        # Advance one color
        if(color < len(ant.color_data)):
            ant.nextGen_board[self.y, self.x] = color+1
        else:
            ant.nextGen_board[self.y, self.x] = 1
        # Turn right
        if(ant.color_data[color] == ant.turnRight):
            # Change direction
            if(self.direction < 3):
                self.direction += 1
            else:
                self.direction = 0
            self.advance()
            
        # Turn left
        if(ant.color_data[color] == ant.turnLeft):
            # Change direction
            if(self.direction > 0):
                self.direction += -1
            else:
                self.direction = 3
            self.advance()

    # Advance one position
    def advance(self):
        if(self.direction == ant.antUp):
            self.y += 1
        elif(self.direction == ant.antRight):
            self.x += 1
        elif(self.direction == ant.antDown):
            self.y += -1
        else:
            self.x += -1

# Number of ants
ant_1 = ant()
#ant_2 = ant()
#ant_3 = ant()

fig, ax = plt.subplots()
plt.axis("off")

def animate(i):
    for i in range(0, ant.max_i):
        move = ant_1.move()
        #move = ant_2.move()
        #move = ant_3.move()
    #move[ant_1.y, ant_1.x] = 0
    #move[ant_2.y, ant_2.x] = 0
    cmap = mcolors.ListedColormap(ant.color_dataStr)
    im = ax.imshow(move, cmap = cmap)
    im.set_data(move)
    return [im]

animation = anim.FuncAnimation(fig, animate, frames = 100, interval = 1, blit = False, repeat = True)
plt.show()