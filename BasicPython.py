# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

#   This indentation is fine.
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
        
#   This indentation throws an error: 
#if 5 > 2:
 #print("Five is greater than two!")
        #print("Five is greater than two!")
        
# Variables are loosely-typed same as in JavaScript:
x = 5
y = "Hello, World!"

"""
This is a comment
written in
more than just one line
"""

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#   Do this if u need a variable to be a certain type:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

#   Can have single or double quotes for strings same as JS:
x = "John"
x = 'John'
#   Variable names are case-sensitive, "A" won't overwrite "a".
a = 4
A = "Sally"

""" Good variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""

""" Bad variable names:
2myvar = "John"
my-var = "John"
my var = "John"
"""

#   Snake-case:
my_variable_name = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#   This is an easy way to turn a list (array) into 
#   3 seperate variables!
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)

#   Ok:
x = 5
y = 10
print(x + y)

#   An error bec 1 string 1 number:
""" x = 5
y = "John"
print(x + y) """

#   A function that uses a global variable:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Now a local function variable overrides the global one:
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

