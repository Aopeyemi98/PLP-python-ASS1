# This line of code prompt a user to enter their first number
# stores the number into num1 variable
num1 = int(input("Please, Enter the first number!"))

# This line of code prompt a user to enter their second number
# stores the number into num2 variable
num2 = int(input("Please, Enter the second number!"))

# This line of code prompt a user to enter the operator
# stores the number into operator variable
operator = input("Please, operator!")
if operator == "+":
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "**":
    result = num1 ** num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "//":
    result = num1 // num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "%":
    result = num1 % num2
    print(f"{num1} {operator} {num2} = {result}")
else:
    print("NOT APPLICABLE")