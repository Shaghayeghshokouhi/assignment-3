# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:21:01 2023

@author: 2022
"""

import random

while True:
    num1 = random.randint(1,6)
    roll_dice = input("roll the dice? type yes:")
    if roll_dice == "yes":
        print(num1)
    if num1 == 6:
       print("wow 6!!! you can roll again")
       roll_dice2 = input("roll the dice? type yes:")
       if roll_dice2 == "yes":
           print(num1)
    else:
       print("the value is", num1)
       break
       
     