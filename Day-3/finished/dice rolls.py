# Listing_23-2.py
# Copyright Warren Sande, 2009
# Released under MIT license http://www.opensource.org/licenses/mit-license.php
# Version 61 ----------------------------
# Changes by Brian Skinner - Sept, 2013

# Rolling two six-sided dice 1000 times.

import random

totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#function that rolls 2 dice and returns the sum of their rolls
def roll_dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    total = roll1 + roll2
    return total

for i in range(1000):
    dice_total = roll_dice()
    totals[dice_total] = totals[dice_total]+ 1

#why did we skip spots 0 and 1?
print "2 was rolled", totals[2], "times"
print "3 was rolled", totals[3], "times"
print "4 was rolled", totals[4], "times"
print "5 was rolled", totals[5], "times"
print "6 was rolled", totals[6], "times"
print "7 was rolled", totals[7], "times"
print "8 was rolled", totals[8], "times"
print "9 was rolled", totals[9], "times"
print "10 was rolled", totals[10], "times"
print "11 was rolled", totals[11], "times"
print "12 was rolled", totals[12], "times"
