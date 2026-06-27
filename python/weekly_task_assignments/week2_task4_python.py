# Even or Odd Checker
# •	Task: Write a program that prompts the user for an integer.
# o	Use if/else to check whether the number is even or odd.
# o	Print "Even" or "Odd" accordingly.

users = int(input("Enter a number:"))
if users//2:
    print("You entered an even number")
else:
    print("You entered odd number")

# Positive, Negative, or Zero
# •	Task: Write a program that prompts the user for a number.
# o	Use if/elif/else to determine if the number is positive, negative, or zero.
# o	Print a message such as "The number is positive.".

users = int(input("Enter a number:"))
if users > 0:
    print("Positive Number")
elif users == 0:
    print("Zero")
else:
    print("Negative Number")

# Grade Categorizer
# •	Task: Prompt the user for a number between 0 and 100 (the score).
# o	Use if/elif/else to categorize the score:
# 	90–100: "Grade A"
# 	80–89: "Grade B"
# 	70–79: "Grade C"
# 	< 70: "Fail"

score = int(input("Enter the score betweeen 0 and 100: "))
if score >= 90:
    print("Grade A")
elif score > 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail")


# Multiples of 3 and 5
# •	Task: Prompt the user for a single integer n.
# o	Use a for loop to iterate from 1 up to n (inclusive).
# o	For each value i, print:
# 	"Multiple of both" if i is divisible by 3 and 5.
# 	"Multiple of 3" if i is divisible by 3 but not 5.
# 	"Multiple of 5" if i is divisible by 5 but not 3.
# 	The number i itself otherwise.

numbers = int(input("Enter a single number: "))
for i in range(numbers + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Multiple of both 3 and 5")
    elif i % 3 == 0:
        print("Multiple of 3")
    elif i % 5 == 0:
        print("Multiple of 5")
    else:
        print(i)


## If you want to run code which prints only output of divisible by both numbers.

numbers = int(input("Enter a single number: "))
for i in range(1,numbers+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by 3 and 5")

# Simple Password Check
# •	Task: Prompt the user for a password (e.g., "secret").
# o	Use if to check if the user’s input matches the correct password.
# o	If correct, print "Access granted", otherwise print "Access denied".

password = input("Enter your password: ")
if password == 'secret':
    print("Access Granted")
else:
    print("Access Denied") 

# Mistake that i did:

password = input("Enter your password: ")
if 'secret' == 'secret':
    print("Access Granted")
else:
    print("Access Denied") 

'''
In this user password case, the password will always be True 
because it does not check with variable "password" what user entered 
instade it checks if the 'secret'=='secret' is True and prints the output. Basically, it ignores 
whatever the user typed.
'''

# Count Vowels in a String
# •	Task: Ask the user for a string.
# o	Use a for loop to iterate over each character.
# o	Use if conditions to check if it’s a vowel ("a", "e", "i", "o", "u").
# o	Count the total number of vowels and print the result.

letters = input("Enter a letter to count vowels contain in your text: ")
count = 0
for letter in letters:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        count = count + 1
print(count) 

## Seacond easy method:

letters = input("Enter a letter to count vowels contain in your text: ")
count = 0
for letter in letters:
    if letter in "aeiou":
        count += 1

print(count) 

# Smallest of Three Numbers
# •	Task: Prompt the user for three different numbers.
# o	Use if/elif/else to find and print which one is smallest.

num1 = int(input("Type First Number: "))
num2 = int(input("Type Second Number: "))
num3 = int(input("Type Third Number: "))
if num1 < num2 and num1 < num3:
    print("num1 is the smallest")
elif num2 < num1 and num2 < num3:
    print("num2 is the smallest")
else:
    print("num3 is the smallest")

## Incase user enters same both numbers

num1 = int(input("Type First Number: "))
num2 = int(input("Type Second Number: "))
num3 = int(input("Type Third  Number: "))
if num1 == num2 or num1 == num3 or num3 == num2 or num3 == num1:
    print(" Both input can not be the same")
elif num1 < num2 and num1 < num3:
    print("num1 is the smallest")
elif num2 < num1 and num2 < num3:
    print("num2 is the smallest")
else:
    print("num3 is the smallest")

# Simple Menu Selection
# •	Task: Prompt the user to choose an option (e.g., 1 for "Start", 2 for "Settings", 3 for "Exit").
# o	Use if/elif/else to print a response based on which option is chosen.
# o	Example:
# 	If user enters 1: print "Game starting..."
# 	If user enters 2: print "Opening settings..."
# 	If user enters 3 or any other: print "Exiting..."

choice = int(input("Choose an options(1-start, 2-setting, 3-exit): "))
if choice == 1:
    print("Game starting")
elif choice == 2:
    print("Game setting")
else:
    print("Game exiting")

## Incase user enters other numbers rather than just 1,2 and 3

choice = int(input("Choose an options(1-start, 2-setting, 3-exit): "))
if choice == 1:
    print("Game starting")
elif choice == 2:
    print("Game setting")
elif choice == 3:
    print("Game exiting")
else:
    print("Invalid Option")
                   












