import pygame
import math
import numpy as np
import os
import sys
import settings as st
import colors, player, wall, checkpoint, win

os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()
screen = pygame.display.set_mode((st.windowWidth, st.windowHeight))
playerObj = player.Player()


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


def reset_player():
    with open('level_maps/level_' + str(st.level), 'r') as f:
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


def agent_control(key):
    if key == 0:
        playerObj.move(0, st.playerLength)      # move down
    if key == 1:
        playerObj.move(st.playerLength, 0)     # move right
    if key == 2:
        playerObj.move(0, -st.playerLength)     # move up
    if key == 3:
        playerObj.move(-st.playerLength, 0)      # move left
    

def Agent(state, prev_state, reward, prev_action):
    # save the reward to q-table
    # from q-table, get best output for the present state
    # return the col no (action)
    try:                                        # Load the table
        Qtable = np.load("qtt3.npy")
    except:                                     # Create table
        # Q_table = np.random.rand(300, 4)
        Qtable = np.zeros((300, 4))

    # reward = ((reward+1)/float(20 + 1))
    # print(prev_state, prev_action, reward)
    # if prev_state == state:
        # Q_table[prev_state, prev_action] = -reward
    # else:
    # Q_table[prev_state, prev_action] = reward
    # np.save("data/q_table.npy", Q_table)

    action = np.argmax(Qtable,axis=1)[state]



    return action


def getState(location):
    # stateTable = {(0,0):1, 
    #               (0,20):2,
    #               (0,40):3,
    #               ...
    #               ...
    #               (380,280):300}
    state = (location[0]/20)+location[1]
    return state

def getReward(location):
    global prev_loc
    done = False
    Win_loc = (360, 260)
    unreached_checkpoints = 0
    prev_dist = abs(math.sqrt(math.pow(prev_loc[0] - Win_loc[0], 2) + math.pow(prev_loc[1] - Win_loc[1], 2) * 1.0))
    current_dist = abs(math.sqrt(math.pow(location[0] - Win_loc[0], 2) + math.pow(location[1] - Win_loc[1], 2) * 1.0))
    prev_loc = location

    for _ in checkpoint.checkpoints:
        if playerObj.rect.colliderect(_.rect):
            unreached_checkpoints = 0
            pass
#           Some puchki code to count no of unreached checkpoints
            # unreached_checkpoints = xxx

    for _ in win.wins:
        if playerObj.rect.colliderect(_.rect):
            # pygame.time.delay(100)
            reward = 20 - (5*unreached_checkpoints)
            st.level += 1
            if st.level <= st.noOfLevels:
                playerObj.__init__()
            else:
                sys.exit()
            return reward, True

    if (current_dist < prev_dist):
        reward = 1
    elif (current_dist > prev_dist):
        reward = -1
    else:
        reward = 0

    return reward, False


running = True
state = 0
action = 0
observation, reward, done, info = [], 0, False, []
prev_state = 0
prev_action = 0
prev_loc = (20,20)

while running:
  # IF user wants to play
    user_control()
    location = playerObj.locate()
    print(location[0]/20+location[1])

# #   If Agent needs to be trained
#     action = prev_action = Agent(state, prev_state, reward, prev_action)
#     agent_control(action)
#     # obv, reward, done, info = step(action)
#     state = prev_state = getState(playerObj.locate())
#     reward, done = getReward(playerObj.locate())
#     location = playerObj.locate()
#     print(location[0]/20+location[1], action, reward)

    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            running = False
        elif _.type == pygame.KEYDOWN and _.key == pygame.K_ESCAPE:
            running = False
        elif done == True:
            running = False
    update_window()
    pygame.time.delay(100)
