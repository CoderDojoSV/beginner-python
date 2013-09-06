# Listing_1-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Number Guess game

import random

secret = random.randint(1, 99)     # pick a secret number
guess = 0
tries = 0

print "AHOY!  I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99.  I'll give you 6 tries. "

# try until they guess it or run out of turns
while guess != secret and tries < 6:
    guess = input("What's yer guess? ")       # get the player's guess
    if guess < secret:
        print "Too low, ye scurvy dog!"
    elif guess > secret:
        print "Too high, landlubber!"
    tries = tries + 1                         # used up one try

# print message at end of game    
if guess == secret:
    print "Avast! Ye got it!  Found my secret, ye did!"
else:
    print "No more guesses!  Better luck next time, matey!"
    print "The secret number was", secret
