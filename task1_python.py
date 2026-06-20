# Basic Arithematic and Type Identification

number = [12, 3.55, 4-6j]
print(type[0](number))
print(type(number[1]))
print(type(number[2]))

# Arithmetic with Mixed Types

a = 5
b = 4.7

sum1 = a + b
difference = a - b
product = a * b
quotient = a/b

print(f"Sum1: {sum1}" )
print(type(sum1), "\n")

print(f"Difference: {difference} ")
print(type(difference), "\n")

print(f"Product: {product}")
print(type(product), "\n")

print(f"Quotient: {quotient}")
print(type(quotient))

# Comparison With Mixed Types

x = 10
y = 7

print(x>y) # Output is 'True' because x is greater than y.
print(x<y) # Value of y is not greater than x so it's 'False'
print(x==y) # Output is 'False' because both x,y value are not same.
print(x!=y) # Result is 'True' because both are not equal to each other.

# Boolean Variables

status = True
print(type(status))

status = False
print(type(status))

# String Creation and Length

text = "Hello Universe!"
print(len(text))
print(type(text))

# String Indexing

s = "Python"
print(s)
print(s[0], s[-1])
print(s[0] + s[-1])

# String Slicing

lang = "Programming"
print(lang[0:4])
print(lang[3:])
print(lang[2:-2])

# Exploring len() on Slices

lang = "Programming"
part1 = lang[0:7]

print(part1)
print(len(part1))
print(len(lang))
'''
len(part1) is different from len(lang)
because len(part1) only contains frist 7 character
while len(lang) covers all.

'''
# String Methods-Case Conversion

phrase = "Hello, Python!"
print(phrase.upper())
print(phrase.lower())
print(phrase) # Strings are immutable

# Combining String

str1 = "Data"
str2 = "Science"
com1_2 = f"{str1} {str2}"
print(com1_2)
print(len(com1_2)) #len counts space as well

# In-Place vs. Reassignment with String Methods

word = "example"
word.upper()
print(word)

word = word.upper()
print(word)
'''
Second print is different from the first one because
it created 'Example' but did not change the orginal string.
'''
# Arithmetic Operator Precedence

a = 5
b = 3
c = 2
print(a+b*c)
print((a+b)*c) 
'''
Same like in mathmatics it follows rule
'P(), E(exponents **), MD(Multiplication & Divide), 
AS(additional & Subtraction)

'''
# String Index Out Of Range

# text = "Hello"
# print(text[10])  

'''
IndexError because text has only upto 4th 
index and 10th does not exist.
'''

# Equality vs. Identity Check (Conceptual Explanation)

s1 = "test"
s2 = "test"
print(s1 == s2)
print(s1 is s2)

# Creating and Checking a Complex Number

z = 3 + 4j
print(z.real)
print(z.imag)
print(type(z))

# Comparisons with Floats

f1 = 0.1 + 0.2
f2 = 0.3
print(f1==f2)
print(f1)
print(f2)
# print(math.isclose(f1, f2))




