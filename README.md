# AI Gaming Bot
Reinforcement learning using Q learn algorithm.

This is a Gaming bot which can learn and play a maze game. It learns based on the +ve and -ve rewards received for doing some action. Currently, it's capable of reaching some checkpoints, overcoming obstacles and reaching given destination.
<br><br>
Below are the level maps on which I have trained the bot.
## Level Maps:
<p>
  <img src="./images/stage1.png" alt="Stage1" width="250"/>
  <img src="./images/stage2.png" alt="Stage2" width="250"/>
  <img src="./images/stage3.png" alt="Stage3" width="250"/>
</p>
<br>

### Level 1:
This level is to test if the bot can reach a particular destination in the shortest path possible or not. In time, it learns how to do it and always try to reach a particular location in the shortest path possible.<br>
As we can see, it's trying to find it's way to the destination by wandering around the area and checking where the reward is more.
<br><img src="./images/stage1_learning.gif" alt="Stage-1 Learning" width="200"/><br>
Now, it has found the shortest path from it's location to the destination.
<br><img src="./images/stage1_working.gif" alt="Stage-1 Working" width="200"/><br>
Once it understood how to reach a destination, we can try with different starting and ending points to test it's limitations.
<p>
  <img src="./images/stage1_working_1.gif" alt="Stage1" width="200"/>
  <img src="./images/stage1_working_2.gif" alt="Stage2" width="200"/>
  <img src="./images/stage1_working_3.gif" alt="Stage3" width="200"/>
</p>
I have only changed the starting location of the player and it works fine with any initial location. 
<br>Now let's go to level 2.
<br>

### Level 2:
In level 2, we'll make it learn how to reach certain checkpoints using the experience in the previous level.
<br><img src="./images/stage2_working.gif" alt="Stage-2 Working" width="200"/><br>
Finally, the agent has learnt to pass through all the checkpoints and reach the goal.
<br>let's take the game to level 3 now.
<br>

### Level 3:
Here, there is a new challenge. The obstacles are in between the path to the checkpoints and the agent is unable to find a way around it.<br>
Its stuck in a position where it gets a negative reward for deviating from it's path and a neutral reward for trying the same path again and again.<br>
<img src="./images/stage3_learning.gif" alt="Stage-3 Learning" width="200"/><br>
To overcome this kinda problem, we have to tell the agent that "It's OK to try some different path if no positive reward is awarded for a period of time."<br>
This can be done by tuning the alpha value (learning rate or randomness rate). Increasing this will help it find a solution by trying different paths than its regular path.<br>
<img src="./images/stage3_working.gif" alt="Stage-3 Working" width="200"/><br>
Finally, It's able to reach the destination by overcoming the obstacles and covering all the check points.<br>

## Final Result:
<img src="./images/stage3_working.gif" alt="Stage-3 Working"/><br>
