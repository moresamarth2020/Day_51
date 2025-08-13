#!/usr/bin/env python
# coding: utf-8

# # Snake Water Gun Game in Python - Exercise 5
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

# In[7]:


import random

def check(comp, user):
    if comp == user:
        return 0
    
    if (comp ==0,  user == 1):
        return -1
    
    if (comp ==1,  user == 2):
        return -1 
    
    if (comp ==2,  user == 0):
        return -1
    
    return 1
        
comp = random.randint(0,2)
user = int(input(" 0 for Snake, 1 for Water and 2 for Gun:\n"))


score = check(comp, user)
print("You:", user)
print("Computer:", comp)

if score == 0:
    print("Its a Draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")


# In[ ]:




