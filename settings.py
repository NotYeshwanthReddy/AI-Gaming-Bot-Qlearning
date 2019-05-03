# Game variables
noOfLevels = 3
timeLimit = {
    1: 10,
    2: 20,
    3: 20
}
lives = 3
level = 1

# UI variables
windowWidth = 400
windowHeight = int(windowWidth*3/4)
playerLength = 20
blockLength = 20

# AI variables
states = (windowWidth/playerLength)*(windowHeight/playerLength)
actions = 4
alpha = 0.4
gamma = 0.2
