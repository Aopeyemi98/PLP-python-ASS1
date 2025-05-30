"""
🔹 Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

📌 Task Requirements:
Create a file called input.txt and write at least five lines of text into it.
Write a Python script to:
Read the contents of input.txt.
Count the number of words in the file.
Convert all text to uppercase.
Write the processed text and the word count to a new file called output.txt.
Print a success message once the new file is created.
"""
try:
    with open("input.txt", "r") as file:
        content = file.read()
        alphabet_counter = len(content)
        words_counter = len(content.split())
        print(f"Number of alphabet is: {alphabet_counter}")
        print(f"Number of each word is: {words_counter}")

        upper_case = content.upper()
        print(upper_case)
except FileNotFoundError:
    print("file not found!!!..Or check the spellings well")

    with open("output.txt", "w") as output_file:
        output_file.write(f"Number of alphabet is: {alphabet_counter}\n\n")
        output_file.write(f"Number of each word is: {words_counter}\n\n")
        output_file.write(upper_case)

print("New file output.txt has been successfully created with the processed text!!!")



"""
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
Outcomes 🎉

By the end of this module, you’ll be skilled in managing files efficiently in Python, ensuring error-free code that 
gracefully handles unexpected issues. Mastering files and exception handling will allow you to build strong, 
robust applications!
"""

try:
    # prompt user to enter the file they want to work with!
    with open(input("Enter a file name: "), "r") as input_file:
        file = input_file.read()

    # prompt user to enter or create a new file to save the modified work
    with open(input("Enter a new File name!!: "), "w") as output_file:
        output_file.write(file)
        print("🎉 File read and modified successfully!")

except FileExistsError and FileNotFoundError:
    print("🚫 Error: File not found. Please check the filename and try again.")

except PermissionError:
    print("🚫 Error: You don't have permission to read or write this file.")

    