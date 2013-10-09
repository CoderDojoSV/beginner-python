#More Text-Based Programs To Try

Days 1, 2, and 3 have focus on text-based games and programs. Here are some more fun text-based programs to try. 

###Hailstone Pattern

The hailstone pattern is a cool number pattern that for any positive whole number, it will always end in one. It repeats the following steps until it gets to one: if the number is even, it will divide by two. If the number is odd, it will multiply by three and add one.

Here is an example that starts with the number 7:

    7
    22
    11
    34
    17
    52
    26
    13
    40
    20
    10
    5
    16
    8
    4
    2
    1
    
It took 16 steps!

How can you make this into a program? It should ask the user to enter a number, output the number at every step, and count how many steps it took to finish. 

This will require one thing that you likely haven't seen before: mod (%). This is how you can determine if a number is even or odd. Mod is similar to division, but just worries about the remainder. So if you said 7 mod 2, it is asking what the remainder is when you divide 7 by 2. The answer is 1. This is how you can program this in Python:

    if number % 2 == 0:
      #code for even
    else:
      #code for odd

What happens when you enter a really big number? How many steps does it take?

Refer to the finished folder for a complete example.

###Tic-Tac-Toe

The San Francisco CoderDojo has done a really fun Tic-Tac-Toe Python project that you can go through. Head to https://github.com/CoderDojoSF/tic-tac-toe and follow the links for Lesson 1 and Lesson 2!

###Invent With Python - Dragon Realm

[Invent With Python](http://inventwithpython.com/) is a free online Python book with some great projects.

Chapter 6 (page 84) in the book shows how to create a text-adventure game called Dragon Realm. [Here is the online pdf version of the book](http://inventwithpython.com/IYOCGwP_book1.pdf). 

###Invent With Python - Hangman

[Invent With Python](http://inventwithpython.com/) is a free online Python book with some great projects.

Chapter 9 (page 132) in the book shows how to create the letter and word guessing game Hangman. [Here is the online pdf version of the book](http://inventwithpython.com/IYOCGwP_book1.pdf). 





