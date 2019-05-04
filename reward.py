import settings as st
import win, checkpoint
import player
import math

prev_loc = (0, 0)

class Reward(object):

    # Reward initilisation
    def __init__(self):
        pass


    def getReward(self, playerObj):
        global prev_loc
        
        winsPos = player.winsPos
        checkpointsPos = player.checkpointsPos
        location = playerObj.locate()

        prev_dist = abs(math.sqrt(math.pow(prev_loc[0] - winsPos[0][0], 2) + math.pow(prev_loc[1] - winsPos[0][1], 2) * 1.0))
        current_dist = abs(math.sqrt(math.pow(location[0] - winsPos[0][0], 2) + math.pow(location[1] - winsPos[0][1], 2) * 1.0))
        
        if (current_dist < prev_dist):
            reward = 1
        elif (current_dist > prev_dist):
            reward = -1
        else:
            reward = 0

        prev_loc = location

        for _ in win.wins:
            if playerObj.rect.colliderect(_.rect):
                reward = 2
                return reward, False

        return reward, False


# def getReward(location):
#     global prev_loc
#     done = False
#     Win_loc = (360, 260)
#     unreached_checkpoints = 0
#     prev_dist = abs(math.sqrt(math.pow(prev_loc[0] - Win_loc[0], 2) + math.pow(prev_loc[1] - Win_loc[1], 2) * 1.0))
#     current_dist = abs(math.sqrt(math.pow(location[0] - Win_loc[0], 2) + math.pow(location[1] - Win_loc[1], 2) * 1.0))
#     prev_loc = location

#     for _ in checkpoint.checkpoints:
#         if playerObj.rect.colliderect(_.rect):
#             unreached_checkpoints = 0
#             pass
# #           Some puchki code to count no of unreached checkpoints
#             # unreached_checkpoints = xxx

#     for _ in win.wins:
#         if playerObj.rect.colliderect(_.rect):
#             # pygame.time.delay(100)
#             reward = 20 - (5*unreached_checkpoints)
#             st.level += 1
#             if st.level <= st.noOfLevels:
#                 playerObj.__init__()
#             else:
#                 sys.exit()
#             return reward, True

#     if (current_dist < prev_dist):
#         reward = 1
#     elif (current_dist > prev_dist):
#         reward = -1
#     else:
#         reward = 0

#     return reward, False