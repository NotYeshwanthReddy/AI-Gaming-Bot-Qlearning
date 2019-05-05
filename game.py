"""
Created on:
    May 1 2019
Developers:
    Yeshwanth Reddy
    Nikhil Reddy
"""
import pygame
import os
import sys

import settings as st
import colors, player, wall, checkpoint, win
import AI as ai
import reward as rwd

# creating global variables for objects
playerObj= aiObj = rewardObj = 0
screen = 0

# Initilizing Pygame screen and required Objects (called once an episode)
def init():
    global playerObj, aiObj, rewardObj
    global screen
    os.environ["SDL_VIDEO_CENTERED"] = '1'
    pygame.init()
    screen = pygame.display.set_mode((st.windowWidth, st.windowHeight))
    playerObj = player.Player()
    aiObj = ai.AI()
    rewardObj = rwd.Reward()

# Update the game window (called at every interation)
def update_window():
    pygame.Surface.fill(screen, colors.white)

    for _ in wall.walls:
        pygame.draw.rect(screen, colors.black, _)

    for _ in win.wins:
        pygame.draw.rect(screen, colors.green, _)

    for _ in checkpoint.checkpoints:
        pygame.draw.rect(screen, colors.yellow, _)

    pygame.draw.rect(screen, colors.blue, playerObj)
    pygame.display.flip()

# Resets th player to initial location
def reset_player():
    with open(st.level_map, 'r') as f:
        level_map = f.read().split('\n')

    x = y = 0
    for row in level_map:
        for col in row:
            if col == 'O' or col == 'o':
                playerObj.rect = pygame.Rect(x + st.blockLength / 4, y + st.blockLength / 4,
                                             st.playerLength, st.playerLength)
            x += st.blockLength
        y += st.blockLength
        x = 0

# User controls the player
def user_control():
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        playerObj.move(-st.playerLength, 0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        playerObj.move(st.playerLength, 0)
    if key[pygame.K_UP] or key[pygame.K_w]:
        playerObj.move(0, -st.playerLength)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        playerObj.move(0, st.playerLength)

    for _ in win.wins:
        if playerObj.rect.colliderect(_.rect):
            pygame.time.delay(100)
            st.level += 1
            if st.level <= st.noOfLevels:
                playerObj.__init__()
            else:
                sys.exit()

# AI controls the player
def agent_control(key):
    if key == 0:
        playerObj.move(0, -st.playerLength)     # move up
    if key == 1:
        playerObj.move(0, st.playerLength)      # move down
    if key == 2:
        playerObj.move(-st.playerLength, 0)      # move left
    if key == 3:
        playerObj.move(st.playerLength, 0)     # move right

    for _ in win.wins:
        if playerObj.rect.colliderect(_.rect):
            print("Win...!")
            pygame.time.delay(100)
            st.level += 1
            if st.level <= st.noOfLevels:
                playerObj.__init__()
            else:
                sys.exit()

# Get the state number from players location
def getState(location):
    # stateTable = {(0,0):1, 
    #               (0,20):2,
    #               ...
    #               ...
    #               (380,280):300}
    state = (location[0]/20)+location[1]
    return state


# Main code starts here
running = True
state = 0
action = 0
observation, reward, done, info = [], 0, False, []

for episode in range(st.episodes):
    init()
    while running:
    # IF user wants to play
      #   user_control()
      #   location = playerObj.locate()
      #   print(location[0]/20+location[1])

    # Play with the Agent
        state = getState(playerObj.locate())
        action = aiObj.agent(state, reward)
        agent_control(action)
        # obv, reward, done, info = step(action)
        reward, done = rewardObj.getReward(playerObj)

        for _ in pygame.event.get():
            if _.type == pygame.QUIT:
                running = False
            elif _.type == pygame.KEYDOWN and _.key == pygame.K_ESCAPE:
                running = False
            elif done == True:
                running = False
        update_window()
        pygame.time.delay(130)
