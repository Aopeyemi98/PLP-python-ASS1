
"""
Write an if/elif/else statement for a college with a grading system as shown below:

If grade is 90 or higher, print "A"
Else if grade is 80 or higher, print "B"
Else if grade is 70 or higher, print "C"
Else if grade is 60 or higher, print "D"
Else, print "F"
"""

grade = int(input("Enter an Integer "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


"""
Coding Challenges for basic control flows and functions

1. Large Power

Create a method that tests whether the result of taking the power of one number to 
another number provides an answer which is greater than 5000. We will use a conditional 
statement to return True if the result is greater than 5000 or return False if it is not. 
In order to accomplish this, we will need the following steps:

Define the function to accept two input parameters called base and exponent
Calculate the result of base to the power of exponent
Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False

Coding Question

Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False
"""

def large_power(base, exponent):
    result = base**exponent
    if result > 5000:
        print("True")
        return True
    else:
        print("False")
        return False
    
large_power(base = int(input("Enter any number ")),
        exponent = int(input("Enter any number ")))


"""
2.Divisible By Ten
Create a function that determines whether or not a number is divisible by ten. 
A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, 
we can complete this function in a few steps:

Define the function header to accept one input num
Calculate the remainder of the input divided by 10 (use modulus)
Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False

Coding question

Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. 
Consider using modulo operator % to check for divisibility.
"""

def divisible_by_ten(num):
    result = num % 10
    if result == 0:
        print("True")
        return True
    else:
        print("False")

divisible_by_ten(num=int(input("Enter any integer ")))


"""
Create a function named calculate_discount(price, discount_percent) that calculates the final price after 
applying a discount. The function should take the original price (price) and the discount percentage 
(discount_percent) as parameters. If the discount is 20% or higher, apply the discount; 
otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the 
discount percentage. Print the final price after applying the discount, or if no discount was applied, 
print the original price.
"""

def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    if discount_percent >= 20:
        print(f"Your discounted price of {discount_percent}% is: {discount_amount}")
        return discount_amount
    else:
        print(f"Your price is: {price}..NO Discount!!!")
        return price
    
calculate_discount(price = int(input("Enter your total price ")), 
                   discount_percent = int(input("Input your discount ")))