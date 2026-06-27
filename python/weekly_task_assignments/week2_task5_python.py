# Iterate Through a Tuple and Print Types
# •	Task: Create a tuple with at least 5 different types of elements (int, float, string, bool, and complex).
# •	Use a for loop to iterate over the tuple and print each element along with its data type.

data_types = (5, 4.5, 'Bishnu and Ghansu', True, 5 - 6j)
for data_type in data_types:
    print(data_type,type(data_type), '\n')

# Print All Items from a List with a Custom Message
# •	Task: Create a list of 4 different city names.
# •	Use a for loop to print each city name followed by the phrase "is a great place".

city_names = ["Kathmandu", "Amsterdam", "Paris", "Houston"]
for city_name in city_names:
    print(f"{city_name} is a great place!")

# Print Each Character of a String with Its Index
# •	Task: Ask the user to enter a word.
# •	Use a for loop and enumerate() to print each character of the string along with its index.

word = input("Enter a word: ")
for index, character in enumerate(word):
    print(index,character)

# Sum of Elements in a List
# •	Task: Create a list of integers.
# •	Use a for loop to calculate the sum of all the elements and print the total.

lsts = [5, 10, 15, 20]
total = 0
for lst in lsts:
    total = total + lst
print("Total sum:", total)

## Extra :Create a list of integers and use a for loop to calculate the product (multiplication) of all the elements.

multi = [2,3,4]
mul = 1
for i in multi:
    mul = mul * i
print(mul)

# Count Booleans in a Tuple
# •	Task: Create a tuple containing different data types, including multiple True and False values.
# •	Use a for loop to count how many True values are present and print the count.

mixed_data = (True, 5, 7, False, 4 + 2j, True, False, 7.5, True)
count = 0
for mixed in mixed_data:
    if mixed == True:
        count += 1
print(count)

# Check and Print Data Types from a List
# •	Task: Create a list with at least 6 elements of different types (int, float, str, bool, etc.).
# •	Use a for loop to iterate through the list and print the data type of each element.

boxes = [7, 8.9, 'ghansu', True, 3 + 2j]
for box in boxes:
    print(type(box))

# Check for Vowels in a String
# •	Task: Ask the user for a word.
# •	Use a for loop to check each character and print a message if it’s a vowel (a, e, i, o, u).

One_word = input("Enter one word: ")
for word in One_word:
    if word in "aeiou":
     print(f"{word} is a vowel")

## What if user writes world in capital letter. In that case solution is given below:

One_word = input("Enter one word: ")
for word in One_word:
    if word.lower() in "aeiou":
     print(f"{word} is a vowel")


# Print Square of Numbers from a Tuple
# •	Task: Create a tuple of numbers from 1 to 5.
# •	Use a for loop to iterate through the tuple and print the square of each number.

numbers = (1,2,3,4,5)
square = []
for number in numbers:
    square.append(number**2)
print(square)


# Print Elements of a List in Uppercase
# •	Task: Create a list of 5 small letter containing words.
# •	Use a for loop to iterate over the list and print each word in lowercase.

# changes = ['BISHNU', 'GHANSU', 'DALLEY', 'ROHIT', 'RAM']
# final = []
# for change in changes:
#     print(change.lower())

# Count Numbers Greater Than 10 in a List
# •	Task: Create a list of integers.
# •	Use a for loop to count how many numbers in the list are greater than 10.
# •	Print the final count.

numbers = [15,5,2,1,50,70,45,47,48]
count = 0
for number in numbers:
    if number > 10:
        count+=1
print(count)

    











