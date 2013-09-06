# Listing_23-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------
# Changes by Brian Skinner - Sept, 2013

# Rolling two six-sided dice 1000 times.

import random

totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#function that rolls 2 dice and returns the sum of their rolls
def roll_dice():
    return 2

for i in range(1000):
    dice_total = roll_dice()
    totals[dice_total] += 1
    
for i in range (2, 13): 
    print "total", i, "came up", totals[i], "times"
