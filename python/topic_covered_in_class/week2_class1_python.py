# Conditional statement: if, elif, else

marks = 80
if marks >= 80:
    print("You have passed with Distinction")

b = int(input("Enter a number: "))
print(type(b))

age = int(input("Enter your age: ")) 
print(type(age)) 

# Checking eligibility using condition.

age = int(input("Enter your age: "))
if age >= 18:
    print("Welcome!! Your are allowed to enter the club 🙂🙂.")
else:
    print("Sorry!! you are not eligible to enter the club 😭😢.")

## using if, elif

# marks = int(input("Enter your marks: "))

if marks >= 80:
    print("You have passed the exam with Distinction!!")
elif marks >= 60:
    print("You have passed the exam with First Division!!")
elif marks >= 40:
    print("You have passed the exam!!")

a = 3
a += 3
print(a)

a = 3
a = a + 3
print(a)


a = 3
if a == 4:
    print('The value of a is 4')

# we can write if and else only once and elif we can write as much as we want.
 
# marks = int(input("Enter Your Marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("zero")

## Temprature warning message:

temprature = int(input("Enter the Temprature: "))

if temprature > 30:
    print("It's very hot outside")
elif temprature > 20:
    print("Temprature is moderate")
elif temprature > 5:
    print("Temprature is very cold outside")
else:
    print("Stay warm and stay at home!")


## Nested Loop (Loop inside loop):

marks = int(input("Enter your marks: "))

if marks > 100:
    print("Marks should not be more than 100!!!")
elif marks < 0:
    print("Marks should not be negative!!!")
else:
    if marks >= 80:
        print("Distinction")
    elif marks >= 70:
        print("First Division")
    elif marks >= 40:
        print("Third Division")
    else:
        print("Fail")

## Using logical operator for clarity:

marks = int(input("Enter the marks: "))

if marks >= 80:
    print("Distinction")
elif marks >= 70 and marks < 80:
    print("First Division")
elif marks >= 60 and marks < 70:
    print("Second Division")
else:
    print("Fail")

## Marking Product level According to price (Cheap, expensive, buy)

price = int(input("Enter the price of the product:"))

if price > 2000:
    print("I don't want to buy the item")
    if price > 3000:
        print("Super Expensive")
    else:
        print("Not Expensive")
else:
    print("I want to but the item")
    if price > 1000:
        print("The item is very cheap")
    else:
        print("Stock the item")

'''Question: Movie Ticket Pricing

Write a program that asks the user's age.

Rules:

If age is 18 or older:
Print "Adult Ticket"
If age is 60 or older:
Print "Senior Discount Available"
Otherwise:
Print "No Discount"
Otherwise:
Print "Child Ticket"
If age is 12 or younger:
Print "Kids Discount Available"
Otherwise:
Print "Regular Child Price"
'''

# age = int(input("Enter Your Current Age: "))
    
if age >= 18:
    print("Adult Ticket")
    if age >= 60:
        print("Senior Disount Available! ")
    else:
        print("No Discount")
else:
    print("Child Ticket")
    if age <= 12:
        print("Kids Discount Available")
    else:
        print("Regular Child Price")

## Indentation

price = 200

if price > 200:
    print("Buy")
else:
    print("Don't Buy")
    print("Have a Great Day")

## f String is used to connect multiple variables.

a = int(input("Enter the first number: "))
b = int(input("Enter the seconf number: "))

print(f"The Sum of {a} and {b} is {a+b}")

## Loop

l = [1,2,3,4,5,6,7,8]
# add one to all list items
l1 = l[0] + 1
print(l1)
l2 =l[1] + 1
print(l2)
l3 = l[2] + 1
print(l3)

## Using for loop
numbers = [1,2,3,4,5,6,7,8]
for number in numbers:
    adding = number + 1
    subtracting = number - 1
    print(f"Add: {adding}, Subtract: {subtracting}")
print("\nAdded Sucessfully!")

## Better ways to use loop

numbers = [5,10,15,20]
added = []
subtracted = []
for number in numbers:
    added.append(number + 1)
    subtracted.append(number - 1)
print(added)
print(subtracted)
print("\nCalculation completed")


