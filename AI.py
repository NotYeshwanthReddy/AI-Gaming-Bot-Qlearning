import settings as st
import numpy as np

prev_state = 0
prev_action = 0
Qtable = []
Q_file = "data/qt"+str(st.level)+".npy"


class AI(object):
    # AI initilisation
    def __init__(self):
        pass

    # returns action for the given state, gains experience from the reward
    def agent(self, state, reward):
        global prev_state, prev_action, Qtable, Q_file
        try:                                        # Load the table (Loading prev experience)
            Qtable = np.load(Q_file)
        except:                                     # Create and save a new table with all 0's 
            Qtable = np.zeros((st.states, st.actions))
            np.save(Q_file, Qtable)
        
        # Get and Save Q value (Saving new experience)
        Qtable[prev_state, prev_action] = (1-st.alpha)*Qtable[prev_state, prev_action] + st.alpha*(reward+st.gamma*np.amax(Qtable[state,:]))
        np.save(Q_file, Qtable)
        
        # Take a new action
        action = self.getAction(state)
        
        # Store the vars for further use
        prev_state = state
        prev_action = action

        return action


    # Choses an action based on previous experience
    def getAction(self, state):
        global Qtable
        for action in range(4):
            if Qtable[state, action] == 0:
                return action
        action = np.argmax(Qtable,axis=1)[state]
        return action


# def Agent(state, prev_state, reward, prev_action):
#     # save the reward to q-table
#     # from q-table, get best output for the present state
#     # return the col no (action)
#     try:                                        # Load the table
#         Qtable = np.load("qtt3.npy")
#     except:                                     # Create table
#         # Q_table = np.random.rand(300, 4)
#         Qtable = np.zeros((300, 4))

#     # reward = ((reward+1)/float(20 + 1))
#     # print(prev_state, prev_action, reward)
#     # if prev_state == state:
#         # Q_table[prev_state, prev_action] = -reward
#     # else:
#     # Q_table[prev_state, prev_action] = reward
#     # np.save("data/q_table.npy", Q_table)

#     action = np.argmax(Qtable,axis=1)[state]

#     return action
