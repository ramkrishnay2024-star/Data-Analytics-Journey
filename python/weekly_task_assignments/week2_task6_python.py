# Print Numbers from 10 to 30
# •	Use a while loop to print numbers from 10 to 30.

num = 10
while num <= 30:
    print(num)
    num+=1

# Print Odd Numbers from 1 to 20
# •	Use a while loop to print all odd numbers from 1 to 20.

odd = 1
while odd <= 20:
    print(odd)
    odd+=2

# Print a Word 5 Times
# •	Use a while loop to print the word "Hello" five times.

word = "Hello"
count = 0
while count < 5:
     print(word)
     count+=1
print("Done")

# Countdown from 5
# •	Use a while loop to print numbers from 5 to 1.

num = 5

while num >= 1:
    print(num)
    num-=1

# Print All Multiples of 3 up to 30
# •	Use a while loop to print 3, 6, 9, ..., up to 30.

multiple = 3

while multiple <= 30:
    print(multiple)
    multiple+=3
    
# Keep Asking for a Number Until It's Positive
# •	Keep asking the user to enter a number until they enter a positive number.

numbers = int(input("Enter a number: "))

while numbers <= 0:
    print("Please enter a positive number")
    numbers = int(input("Enter a number: "))
print("Thank You!")

# Print Even Numbers Between 10 and 20
# •	Use a while loop to print even numbers from 10 to 20.

number = 10

while number <= 20:
    print(number)
    number+=2

# Guess the Secret Number using while loop
# •	Secret number = 7.
# •	Ask the user to guess the number until it's correct.

secret_number = 7

guess = int(input("Guess the correct number: "))

while guess != secret_number:
    print("Incorrect Guess, Try Again!😭")
    guess = int(input("Guess the correct number again: "))

print("Congratulation you guessed it! 😎")

## I want to have more fun with the code and guessing game 🙂

secret_number = 9
attempt = 0

while attempt < 3:
    guess = int(input("Guesst the secret number or get fired👺: "))

    if guess == secret_number:
        print("Congratulation you guessed it right mate😄")

        break

    print("You Gussed it wrong and fired!")
    attempt+=1

if attempt == 3:
    print("Game Over! You Used All Your 3 attempts")

# Function to Add Two Numbers
# •	Create a function add(a, b) that returns the sum.

def add(a, b):
    return(a + b)

result = add(5, 2)   
print(result)


# Function to Multiply Two Numbers
# •	Create a function multiply(x, y) that returns the product.

def multiply(x, y):
    return(x * y)
result = multiply(5, 10)
print(result)

# Function to Check Even or Odd
# •	Create a function check_even(num) that prints "Even" or "Odd".

def largest(a, b):
    if a > b:
        return "a is the largest"
    elif a < b:
        return "b is the largest"
    else:
        return "Both are equal"

print(largest(10, 5))



    


    










    



     




