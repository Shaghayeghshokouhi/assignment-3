# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:13:02 2023

@author: 2022
"""

import random

pc_number = random.randint(0, 20)
num = 0

while True:
    user_number = int(input("enter your guess:"))
    num += 1
    
    if pc_number == user_number:
        print("you won!")
        print("you tried", num , "times")
        break
        
    if pc_number > user_number:
        print("choose a greater number:")
        
    else:
        print("choose a lower number:")    