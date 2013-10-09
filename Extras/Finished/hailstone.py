print "This is a cool number pattern!"
print "For any positive whole number, it will always end in one."
print "If the number is even, it will divide by two."
print "If the number is odd, it will multiply by three and add one."
print "It repeats these steps until the number is one!"

number = input("Please enter a number: ")
steps = 0

while number != 1:
    if number % 2 == 0:
        number = number / 2
    else:
        number = number*3 + 1
    steps = steps + 1
    print number

print "It took", steps, "steps to reach one!"
