"""Write a program that accepts user input to create a list of integers. 
Then, compute the sum of all the integers in the list.
"""
integers = []

user_prompt = (input("Enter an int: "))

for each_prompt in user_prompt:
    num = int(each_prompt)
    integers.append(num)
print(integers) 

total = 0
for number in integers:
    total += number
print(total)


"""
Create a tuple containing the names of five of your favorite books.
Then, use a for loop to print each book name on a separate line
"""
fav_book = ("Rich dad", "Think and grow rich", "Open heaven", "The Bible", "War and Peace")
for book in fav_book:
    print(book)


"""Write a program that uses a dictionary to store information about a person, 
such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. 
Then, print the dictionary to the console.
"""

my_info = {}

my_info['name'] = input('Enter your Name: ')
my_info['age'] = input('Enter your age: ')
my_info['sex'] = input('Enter your sex: ')
my_info['favorite color'] = input('Enter your favorite color: ')
my_info['favorite quote'] = input('Enter your favorite quote: ')

print(my_info)



"""Write a program that accepts user input to create two sets of integers. 
Then, create a new set that contains only the elements that are common to both sets.
"""

input1 = input("Enter integers for the first set: ")
setA = set()
for each_input in input1.split():
    setA.add(int(each_input))

input2 = input("Enter integers for the second set: ")
setB = set()
for each_input in input2.split():
    setB.add(int(each_input))

common_elements = setA & setB

print("Common elements:", common_elements)



"""Create a program that stores a list of words. 
Then, use list comprehension to create a new list that contains only the words that have an odd number of characters."""

words = ['apple', 'banana', 'baba', 'orange', 'cherry', 'date', 'fig', 'grape', 'kiwi']

odd_character = [word for word in words if len(word) % 2 != 0]

print("Words with odd lengths of character:", odd_character)