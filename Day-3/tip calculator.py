# Listing_13-4
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------
#Significant changes by Brian Skinner - Sept, 2013

#Explain the program
print "This is a tax calculator. Enter in the price of your item"
print "and the program will calculate how much it costs with tax."

#Create tax function that takes price and tax_rate as imputs and returns the total price
def calculate_tax(price, tax_rate):
    total = price + (price * tax_rate)
    total = round(total, 2)             #round it to 2 decimal places
    return total

#float is a variable type for decimals
my_price = float(raw_input("Price $"))
my_price_with_tax = calculate_tax(my_price,.0875)
print "The price with tax: $", my_price_with_tax

