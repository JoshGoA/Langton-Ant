import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.colors as mcolors
import random

class langton:
    max_N = 100  #Board area
    board = np.zeros((max_N, max_N))
    #Initialize initial position to a partialy random value more or less located in the middle of the board
    def __init__(self):
        #random.randrange(langton.max_N//3, 2*(langton.max_N+1)//3)
        self.y = random.randrange(langton.max_N//3, 2*(langton.max_N+1)//3)
        self.x = random.randrange(langton.max_N//3, 2*(langton.max_N+1)//3)
        #random.randrange(1, 5)   #1: up, 2: down, 3: left, 4: right
        self.direction = 1
    def move(self):
        langton.temp_board = langton.board.copy()
        langton.temp_board[self.y, self.x] = 2
        if((self.y > 1) and (self.y < langton.max_N-1) and (self.x > 1) and (self.x < langton.max_N-1)):
            if(langton.board[self.y, self.x] == 0):
                langton.board[self.y, self.x] = 1
                if(self.direction == 1):
                    self.direction = 4
                    self.x += 1
                elif(self.direction == 2):
                    self.direction = 3
                    self.x += -1
                elif(self.direction == 3):
                    self.direction = 1
                    self.y += 1
                else:
                    self.direction = 2
                    self.y += -1
            else:
                langton.board[self.y, self.x] = 0
                if(self.direction == 1):
                    self.direction = 3
                    self.x += -1
                elif(self.direction == 2):
                    self.direction = 4
                    self.x += 1
                elif(self.direction == 3):
                    self.direction = 2
                    self.y += -1
                else:
                    self.direction = 1
                    self.y += 1
        return langton.temp_board

ant = langton()
figsize_N = 5
fig, ax = plt.subplots(1, figsize = (figsize_N, figsize_N))
im = ax.imshow(ant.move(), cmap = mcolors.ListedColormap(['White', 'Black', 'Red']))
plt.axis("on")

def animate(i):
    for i in range(0, 10):
        im.set_data(ant.move())

animation = anim.FuncAnimation(fig, animate, frames = 100, interval = 10, blit = False, repeat = True)
plt.show()
#At a white square, turn 90° right, flip the color of the square, move forward one unit
#At a black square, turn 90° left, flip the color of the square, move forward one unit
