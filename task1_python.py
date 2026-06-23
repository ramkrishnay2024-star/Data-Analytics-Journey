# Basic Arithmetic and Type Identification
#	Create three variables: one integer, one float, and one complex number.
#	Print each variable and use the type() function to confirm their data types.


number = [12, 3.55, 4-6j]
print(type[0](number))
print(type(number[1]))
print(type(number[2]))

# Arithmetic with Mixed Types
#	Create one int variable (a) and one float variable (b).
#	Print the sum, difference, product, and quotient of a and b.
#	Print the type() of each result (notice how types may change).


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

#Comparison Operators
#	Let x = 10 and y = 7.
#	Print the results of x > y, x < y, x == y, and x != y.
#	After observing the output, explain why each result is True or False in comments.


x = 10
y = 7

print(x>y) # Output is 'True' because x is greater than y.
print(x<y) # Value of y is not greater than x so it's 'False'
print(x==y) # Output is 'False' because both x,y value are not same.
print(x!=y) # Result is 'True' because both are not equal to each other.

# Boolean Variables
#	Define a variable status = True.
#	Print the value of status and confirm it is a boolean using type(status).
#	Reassign status to False and confirm its type again.


status = True
print(type(status))

status = False
print(type(status))

# String Creation and Length
# Create a string variable, for example text = "Hello World".
# Use len(text) to print its length.
# Use type(text) to verify it is a string.


text = "Hello Universe!"
print(len(text))
print(type(text))

# String Indexing
#	With the string s = "Python", print each character. Then print just the first and last characters using negative indexing.


s = "Python"
print(s)
print(s[0], s[-1])
print(s[0] + s[-1])

# String Slicing
	# Let lang = "Programming".
	# Print the substring from index 0 to index 4.
	# Print the substring from index 3 to the end.
	# Print the substring that omits the first 2 and last 2 characters.


lang = "Programming"
print(lang[0:4])
print(lang[3:])
print(lang[2:-2])

# Exploring len() on Slices
#	Continue using lang = "Programming".
#	Slice lang to get "Program" and store it in a variable part1.
#	Print len(part1) and comment how it differs from len(lang).


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
# String Methods – Case Conversion
	# Let phrase = "Hello, Python!".
	# Print phrase.upper() and phrase.lower().
	# Print the original phrase to show it remains unchanged (strings are immutable).



phrase = "Hello, Python!"
print(phrase.upper())
print(phrase.lower())
print(phrase) # Strings are immutable

# Combining Strings
	# Create two strings, str1 = "Data" and str2 = "Science".
	# Combine them into a single string with a space in between and print it.
	# Print the length of the combined string.


str1 = "Data"
str2 = "Science"
com1_2 = f"{str1} {str2}"
print(com1_2)
print(len(com1_2)) #len counts space as well

# In-Place vs. Reassignment with String Methods
	# Let word = "example".
	# Call word.upper() but do not store it, then print word.
	# Now set word = word.upper(), then print word.
	# Comment on why the second print is different from the first


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
# •	Define a = 5, b = 3, c = 2.
# •	Print the result of the expression a + b * c.
# •	Print the result of (a + b) * c.
# •	In comments, explain how operator precedence affects the outcome.


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
# String Index Out of Range
# •	Let text = "Hello".
# •	Attempt to access an index that doesn’t exist, like text[10].
# •	Observe the error message (IndexError) and explain why it happens in comments.


# text = "Hello"
# print(text[10])  

'''
IndexError because text has only upto 4th 
index and 10th does not exist.
'''

# Equality vs. Identity Check (Conceptual Explanation)
# •	Create two variables with the same string value, s1 = "test" and s2 = "test".
# •	Use the == operator to compare them, then use the is operator.
# •	Explain in comments what each comparison checks.

s1 = "test"
s2 = "test"
print(s1 == s2)
print(s1 is s2)

# Creating and Checking a Complex Number
# •	Define z = 3 + 4j.
# •	Print the real part (z.real) and the imaginary part (z.imag).
# •	Confirm that its type is complex using type(z).

z = 3 + 4j
print(z.real)
print(z.imag)
print(type(z))

# Comparisons with Floats
# •	Let f1 = 0.1 + 0.2 and f2 = 0.3.
# •	Print f1 == f2.
# •	Print the actual values of f1 and f2 to explain any difference in the comparison outcome (floating-point precision).

f1 = 0.1 + 0.2
f2 = 0.3
print(f1==f2)
print(f1)
print(f2)
# print(math.isclose(f1, f2))




