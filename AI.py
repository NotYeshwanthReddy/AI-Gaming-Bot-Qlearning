"""
Created on:
    May 1 2019
Developers:
    Yeshwanth Reddy
    Nikhil Reddy
"""
import settings as st
import numpy as np
import random

prev_state = 0
prev_action = 0
Qtable = []
Q_file = "default"

class AI(object):
    
    # AI initilisation (Loading/Creating  Qtable)
    def __init__(self):
        global Qtable, Q_file
        Q_file = st.Q_file
        
        try:                                        # Load the table (Loading prev experience)
            Qtable = np.load(Q_file)
        except:                                     # Create and save a new table with all 0's 
            Qtable = np.zeros((st.states, st.actions))
            np.save(Q_file, Qtable)


    # returns action for the given state, gains experience from the reward
    def agent(self, state, reward):
        global prev_state, prev_action, Qtable, Q_file

        # Get and Save Q value (Saving new experience)
        Qtable[prev_state, prev_action] = (1-st.alpha)*Qtable[prev_state, prev_action] + st.alpha*(reward+st.gamma*np.amax(Qtable[state,:]))
        np.save(Q_file, Qtable)
        
        # Take a new action
        action = self.getAction(state)
        
        # Store the vars for use in next iteration
        prev_state = state
        prev_action = action

        return action


    # Choses an action based on previous experience
    def getAction(self, state):
        global Qtable
        # If there are actions which it has'nt tried yet, it chooses one of those in random.
        if 0 in Qtable[state,:] :
            action = random.choice(np.where(Qtable[state, :]==0)[0])
        # Choose the maximum value of Q for the current state
        else:
            action = np.argmax(Qtable,axis=1)[state]
        return action
