##Simulating Coin Flips

Grab the starter file [coin flip.py](coin flip.py) and copy it into a new Python window.

The goal of the program is to simulate flipping a coin 1000 times. It uses a function flip_coin() that is incomplete. It's your job to finish it.

Here is another example program that uses a function: [tax calculator.py](tax calculator.py)

Here is one approach to building your function:
* Pick a random number between 1 and 2 (where have you done this before?)
* If the random number is 1 return heads. Else return tails. (where have you done an if/else?)

This line of code is how you can return heads:

    return "heads"

That's it! Test it out and see how many times can your program flip a coin a second.

##Simulating Dice Rolls

Grab the starter file [dice rolls.py](dice rolls.py) and copy it into a new Python window.

This program uses an array named totals. An array is a variable that remembers a list of info in specific slots (the slots start counting at 0). 

This is how you can set a specific slot in the array. In this example we are setting spot 5 (remember it counts starting at zero) to be 99.

        totals[5] = 99

This is how we can look up what the number is in a spot and print it out. This would print 99

        print totals[5]
        
Your job is to complete the dice_roll() function. It should roll two 6-sided dice and add the rolls together. It should return their total.

That's it! Test it and see if it is faster or slower than the coin flip program. 

Take home challenge: can you change the program to roll 3 dice? How many slots would you have to add to the array? How about 5 dice?

##Bonus Text Based Programs

In Day 4 we will begin doing some graphics. There are a couple more fun text based programs that you can try before then. Go to https://github.com/CoderDojoSV/beginner-python/tree/master/Extras and check them out!
