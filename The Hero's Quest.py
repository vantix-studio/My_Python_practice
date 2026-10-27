# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:53:29 2026

@author: Albaloo
"""

n = int(input('put number :'))
score = int(input('put number :'))
for level in range (1 , n+1):
    if level % 3 == 0 :
        score*=2
        print(f"hero level is {level} and score is {score}")
    elif level % 2 == 0:
        score+=5
        print(f"hero level is {level} and score is {score}")
    else :
        score-=2
        print(f"hero level is {level} and score is {score}")
        