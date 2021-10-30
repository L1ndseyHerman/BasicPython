# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

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

#   String:
x = "Hello World"

#   Int:
x = 20

#   Float:
x = 20.5

#   Complex?! What even is this? It's not Hexadecimal, so huh?
x = 1j

#  List, which I'm assuming is like an array in Java:
x = ["apple", "banana", "cherry"]

#   Tuple? Is this an Enumeration?
x = ("apple", "banana", "cherry")

# This is a Range... so maybe the ints 1-6 or 0-6?
x = range(6)

#   Dictionary, which is like a HashMap in C# but a JS object here?
x = {"name" : "John", "age" : 36}

#   A Set, so is this a HashSet? Or an array?
x = {"apple", "banana", "cherry"}

#   Frozenset is a read-only set, I'd assume?
x = frozenset({"apple", "banana", "cherry"})

#   Bool:
x = True

#   Bytes:
x = b"Hello"

#   ByteArray:
x = bytearray(5)

#   MemoryView:
x = memoryview(bytes(5))

#   Ints and floats both have the same unlimited byte length,
#   Float just can have decimal places, or powers, like:
#   35 to the power of 10 and a 3 or something:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#   Complex numbers are written with a "j" as the imaginary part:
#   Ah, that makes more sense.
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#   You cannot convert complex numbers into another number type.

#   Don't forget to "import random" up top for this!
print(random.randrange(1, 10))