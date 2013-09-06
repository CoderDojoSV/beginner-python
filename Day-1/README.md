##Installation

Go to http://helloworldbookblog.com/tools/ and download the installer for your operating system. This will include everything you need. We will be using Python version 2.X.

If there are installation issues, http://repl.it/ can be used for the first few sessions (before graphics are required). 


##First Intro to Python

Open Python IDLE. This opens the output window - we will write our code in a new file. Click File -> New Window.

In the new window, type this to print something:

    print "hello world"

Save the project as a .py extension (you can hit CTRL/CMD + S to save). Hit F5 to run your program.

Create your first variable and print it

    print "hello world"
    name = "Brian"
    print "my name is", name

Have the user type in something and store it in a variable.

    print "hello world"
    name = "Brian"
    print "my name is", name
    
    your_name = raw_input("What is your name?")
    your_age = input("How old are you?")
    
Print the info the user typed in.

    print "hello world"
    name = "Brian"
    print "my name is", name
    
    your_name = raw_input("What is your name? ")
    your_age = input("How old are you? ")
    print "your name is", your_name, "and you are", your_age


##Reading and Altering Code - Number Guess Game

Grab the file [number guess game.py](number guess game.py) and copy it into a new Python window. Play the game!

Let's read through the code to see how it does it!

Some new things to point out:
* Random is a module that was imported so you will be able to pick a random number
* While is a loop that repeats code as long as the condition is met. All the code that is repeated is under it indented one space.
* if/else branches the code so that it only happens if the condition is met. The code that gets run if the condition is met is under it indented one space.
* != (check if not equal), == (check if equal)

Let's make some changes! Can you:
* Give the pirate your name
* Change the game to be guessing between 1-200
* Give 8 guesses


## Multiplication Game

We are going to take what we learned in the Number Guess Game and create a new game - a multiplication quiz. The finished project will ask you a series of 10 random multiplication questions, you have to get each one right to go on to the next one.

* Grab the starter file [multiplication game.py](multiplication game.py) and copy it into a new window.
* 
* Print a welcome message introducing the game
* Use random so
