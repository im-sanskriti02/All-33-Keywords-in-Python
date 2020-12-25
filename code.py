# And
a=8
b=3
if (a>10 and b>10):
    print(a+b)
else:
    print(a-b)

# As 
import calendar as c
print(c.month_name[2])

# Assert 
def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)

mark1 = []
print("Average of mark1:",avg(mark1))

# Break
var = 10                    
while var > 0:              
   print('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print("Good bye!")

# Class
class Person:
      def __init__(self, name, age):
         self.name = name
         self.age = age

p1 = Person("Sanskriti", 24)

print(p1.name)
print(p1.age)

# Continue
var = 10                    
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")

# Def 
def greet(name):
    print("Hello, " + name + ". Good morning!")

# Del 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
del my_list[2]
print(my_list)
del my_list[1:4]
print(my_list)
del my_list[:]
print(my_list)

# Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else
a=20
if a%2==0:
    print(a,"is even")
else:
    print(a,"is odd")

# Except
def divide(x, y): 
    try: 
        result = x // y 
        print("Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
divide(3, 2) 


# False 
a=10
b=9
print(a < b)  # This operation will return False as a result . 

# Finally 
x = 10
try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")

# For
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# From
from datetime import time

x = time(hour=15)

print(x)

# Global
global x
x = "fantastic"

myfunc()

print("Python is " + x)

# If 
x = 10
y = 4
if x > y:
    print("x is greater than y")

# Import 
def greeting(name):
      print("Hello, " + name) # Save this code in a file and name it mymodule.py

import mymodule  # Using the module

mymodule.greeting("Sanskriti")

# In 
""" First Use """
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
  print("yes")

""" Second Use """
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Is
x = ["apple", "banana", "cherry"]
y = x
print(x is y)

 # Lambda 
lambda_cube = lambda y: y*y*y 
print(lambda_cube(5))

# None
"""for checking the type of None """
print(type(None)) 

"""declring a var as None """
var = None
if var is None: 
    print("var has a value of None") 
else: 
    print("var has a value") 

# Nonlocal
def myfunc1():
      x = "Sanskriti"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1())

# Not 
x = False
print(not x)

# Or 
x = 5
print(x > 3 or x < 4)


# Pass
s = "helloworld"

"""Empty loop""" 
for i in s: 
	"""No error will be raised""" 
	pass

"""Empty function"""
def fun(): 
	pass

"""No error will be raised """
fun() 

"""Pass statement """
for i in s: 
	if i == 'd': 
		print('Pass executed') 
		pass
	print(i) 

# True 
a= 10
b= 9
print(a > b) # This operation will return True as a result . 

# Raise
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Return
def add(a, b): 
    return a + b 
result = add(4,5)
print(result())

# True
a = 7
b = 6
print(a > b) """ This will return True as a result"""

# Try
def divide(x, y): 
    try: 
        result = x // y 
        print("Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
divide(3, 2) 


# While
i = 1
while i < 6:
  print(i)
  i += 1

# With
class MessageWriter(object): 
    def __init__(self, file_name): 
        self.file_name = file_name 
      
    def __enter__(self): 
        self.file = open(self.file_name, 'w') 
        return self.file
  
    def __exit__(self): 
        self.file.close() 
  
with MessageWriter('my_file.txt') as xfile: 
    xfile.write('Python is beautiful')      

# Yield
def start():
      yield "Python is beautiful"

output = start()
for i in output:
    print(i)