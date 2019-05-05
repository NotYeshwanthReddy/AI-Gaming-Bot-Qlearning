"""
Created on:
    May 1 2019
Developers:
    Yeshwanth Reddy
    Nikhil Reddy
"""

# Game variables
noOfLevels = 3
timeLimit = {
    1: 10,
    2: 20,
    3: 20
}
lives = 3
level = 3
episodes = 3

# UI variables
playerLength = 20
blockLength = 20
rows = 20
col = 15
windowWidth = blockLength*rows
windowHeight = blockLength*col

# AI variables
states = (windowWidth/playerLength)*(windowHeight/playerLength)
actions = 4
alpha = 0.7
gamma = 0.2

# I/O File locations
level_map = 'levels/level_' + str(level)
Q_file = "data/qt"+str(level)+".npy"
