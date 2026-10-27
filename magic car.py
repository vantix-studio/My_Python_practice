# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:51:29 2026

@author: Albaloo
"""

x = int(input(" input a number"))    
while x != 1 :
    if x %2==0 :
        x = x// 2
        print(x)
    else :
        x = x* 3 + 1
        print(x)
