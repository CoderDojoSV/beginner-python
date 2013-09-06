import random

#print your welcome message here


#pick the numbers to multiply
number1 = 1
number2 = 1
answer = number1 * number2

guess = 0
print "What is", number1, "x", number2, "?"

while guess != answer:
    guess = input("Answer: ")
    if guess != answer:
        print "No, try again"

print "You got it!"
