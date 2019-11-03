import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.colors as mcolors

class ant:
#--------------Direction-------------
    antUp = 0
    antRight = 1
    antDown = 2
    antLeft = 3
#--------------Movement--------------
    turnRight = 0
    turnLeft = 1
#----------Colors: Movement----------
    #Example patterns in the multiple-color extension of Langton's ants:
        #RLR: Grows chaotically. It is not known whether this ant ever produces a highway.
        #LLRR: Grows symmetrically.
        #LRRRRRLLR: Fills space in a square around itself.
        #LLRRRLRLRLLR: Creates a convoluted highway.
        #RRLLLRLLLRRR: Creates a filled triangle shape that grows and moves.
    color_data = dict()
    # Color 0 (Ant)
    antC = 0
    # Color 1
    C_1 = 1
    color_data[C_1] = turnLeft
    # Color 2
    C_2 = 2
    color_data[C_2] = turnLeft
    # Color 3
    C_3 = 3
    color_data[C_3] = turnRight
    # Color 4
    C_4 = 4
    color_data[C_4] = turnRight
    ## Color 5
    #C_5 = 5
    #color_data[C_5] = turnLeft
    ## Color 6
    #C_6 = 6
    #color_data[C_6] = turnRight
    ## Color 7
    #C_7 = 7
    #color_data[C_7] = turnLeft
    ## Color 8
    #C_8 = 8
    #color_data[C_8] = turnLeft
    ## Color 9
    #C_9 = 9
    #color_data[C_9] = turnLeft
    ## Color 10
    #C_10 = 10
    #color_data[C_10] = turnRight
    ## Color 11
    #C_11 = 11
    #color_data[C_11] = turnRight
    ## Color 12
    #C_12 = 12
    #color_data[C_12] = turnRight
#---------Iterations per draw--------
    max_i = 10000
#-------------Value board------------
    max_N = 250
    nextGen_board = np.ones((max_N, max_N))

    # Initialize with position and direction
    def __init__(self):
        # Middle position
        self.y = ant.max_N//2
        self.x = ant.max_N//2
        # Random direction
        self.direction = random.randrange(0, 4)

    # Move ant
    def move(self):
        # Ant board
        currentGen_board = ant.nextGen_board.copy()
        # Limit edges
        if((self.y > 1) and (self.y < ant.max_N-1) and (self.x > 1) and (self.x < ant.max_N-1)):
            # Range through each color until match is found
            for color in range(1, len(ant.color_data)+1):
                if(ant.nextGen_board[self.y, self.x] == color):
                    self.directionColor(color)
        # Return new values
        return currentGen_board

    # Set ant position
    def antPosition(self, currentGen_board):
        # Ant position: ant color
        currentGen_board[self.y, self.x] = ant.antC

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

#----------------Number of ants----------------
ant_1 = ant()
#ant_2 = ant()

# Ant animation
def animate(i):
    ax.cla()
    plt.axis("off")
#-----Range algorithm max_i times per draw-----
    for i in range(0, ant.max_i):
        move = ant_1.move()
        #move = ant_2.move()
#------------------Draw ants-------------------
    ant_1.antPosition(move)
    #ant_2.antPosition(move)
#------------------Set data--------------------
    #Colors:
        #plt.cm.RdYlGn
        #plt.cm.bone
    color = plt.cm.bone
    ax.imshow(move, cmap=color)

# Define subplots
fig, ax = plt.subplots()

# Show drawing
animation = anim.FuncAnimation(fig, animate, frames=100, interval=1, blit=False, repeat=True)
plt.show()
