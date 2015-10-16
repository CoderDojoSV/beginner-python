##Installation

Go to http://helloworldbookblog.com/tools/ and download the installer for your operating system. This will include everything you need. We will be using Python version 2.X.

If there are installation issues, http://repl.it/ can be used for the first few sessions (before graphics are required). 


##First Intro to Python

Open Python IDLE. This opens the output window - we will write our code in a new file. Click File -> New Window.  This will open up a new window to type Python code.

In the new window, type this to print something:

```python
print "hello world"
```

Save the project as a .py extension (you can hit CTRL/CMD + S to save). Hit F5 to run your program.

Create your first variable and print it.  In computer language, a variable is what lets the computer remember something.  In this case, we want the computer to remember our name.  

Below that is a `print` statement that shows you how to print a variable.

```python
print "hello world"
name = "Brian"
print "my name is", name
```

The next task is to ask the user for something.  That's what `raw_input` does.

We can have the user type in something and store it in a variable.

```python
print "hello world"
name = "Brian"
print "my name is", name
    
your_name = raw_input("What is your name?")
```

If you run this, you'll see that there's no space between the `?` and the user's input.  We can fix this by adding a space in.

When you use `raw_input`, it stores what the user typed in in a variable.  We can print the info the user typed in:

```python
print "hello world"
name = "Brian"
print "my name is", name
    
your_name = raw_input("What is your name? ")
print "your name is", your_name
```

You can use `raw_input` to ask the user for strings - things like names and sentences.  
If you use `input`, Python will try to change what the user typed into a number.

```python
print "hello world"
name = "Brian"
print "my name is", name
    
your_name = raw_input("What is your name? ")
print "your name is", your_name
your_age = input("How old are you? ")
print "in a year you will be", your_age+1, "years old"
```

If you try to type "nine" when it asks for the age, it won't work.  Python doesn't know what "nine" is, it only know the digit "9".

There are two types of variables we'll be using today: strings (things like words, sentences), and integers (whole numbers).  Python thinks "nine" is a string, and can't change it to a number.

**Bonus challenge**: In the example above, we added 1 to your age and told you how old you will be in a year. Can you set a new variable years_to_100 that will calculate how many years until you turn 100? Then print out the variable with a message.

##Reading and Altering Code - Number Guess Game

Grab the file [number guess game.py](number guess game.py) and copy it into a new Python window. This is a complete game that came out of a book.  Save it, and play the game!

Then, we'll start looking through the code, and start making changes to it.

Let's read through the code to see how it does it!

It uses three variables:
 * `secret`, which stores the number you have to guess
 * `guess`, which is what the player guesses
 * `tries`, which is how many times the player has guessed.
 
Look at those comments, with the `#` before them.  This doesn't mean anything to the computer, but they can help when you come back to your code and need to understand it again.
 
Look at this while:
 
```python
while guess != secret and tries < 6:
```

This is saying, "While the player has guessed wrong, and they have tries, do this over and over again."  **After the `while`, several lines of code are indented (with the Tab key), which indicate which code gets repeated. Indents matter in Python!**

Some other things to point out:
* Random is a module that was imported so you will be able to pick a random number
* **if/else branches the code so that it only happens if the condition is met. The code that gets run if the condition is met is under it indented one space.**
* != (check if not equal), == (check if equal)

Let's make some changes! Can you:
* Give the pirate your name
* Change the game to be guessing between 1-200
* Give 8 guesses


## Multiplication Game

We are going to take what we learned in the Number Guess Game and create a new game - a multiplication quiz. The finished project will ask you a series of 10 random multiplication questions, you have to get each one right to go on to the next one.

###Getting started
* Grab the starter file [multiplication game.py](multiplication game.py) and copy it into a new window.
* Run it to see what it does
* Read the code to see how it was done

We'll be making a lot more changes to this program to get it to do what we want.

###Finish the project
* Print a welcome message introducing the game
* Use random so it doesn't ask 1 x 1 every time (look at the number guessing game for an example)
* How can you repeat the code so it asks 10 questions in a row?

    You could use a for loop that repeats code a specific number of times. This line will repeat the indented code 10 times:

    ```python
    for num in range(0,10):
    ```

    You could also use a while loop and count yourself. See how the number guess game counted the number of tries.
    
    What code would you want to repeat? Highlight all of it and hit tab to indent it one space.
    
* Print a message at the end of the game

* Finished example (no peeking early): [multiplication game.py](finished/multiplication game.py)

### You Finished, Now What?
Congrats on finishing your very first game in Python! I'm going to guess that it's not very fun to play though. Computer programming is not just about finishing the basic requirements, it's about being creative and making the game your own! Always ask yourself, what would make this game more fun? What would make it cool?

Here are some ideas to get you started:

* Can you count how many times they got questions wrong and tell them at the end of the game?
* Can you add another level with a harder num range?
* Can you add division problems as well?
* Can you ask to multiply 3 numbers instead of 2?
* Can you time the player?
* What other games can you do with user input?  
