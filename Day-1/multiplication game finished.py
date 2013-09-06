import random

#print your welcome message here
print "Welcome to the multiplication game."
print "How well do you know your 2-12 multiplication tables?"

for num in range(0,10):
    #pick the numbers to multiply
    number1 = random.randint(2,12)
    number2 = random.randint(2,12)
    answer = number1 * number2

    guess = 0
    print "What is", number1, "x", number2, "?"

    while guess != answer:
        guess = input("Answer: ")
        if guess != answer:
            print "No, try again"

    print "You got it!"

print "That's it, good work!"
