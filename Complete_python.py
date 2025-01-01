# Creating a virtual environment-----------------------

#    mkdir pseudoProj
#    cd pseudoProj
#    py -3.12 -m venv dependencies
#    .\dependencies\Scripts\activate
#    Now virtual env has been activated
#    type python to enter python shell in cmd
#    type exit() to return to cmd
#    deactivate // to deactivate the environment

# Installing libraries-----------------------------------

# pip install (library name)

# pip uninstall (library name)

""" So, what are n, address, and employee? They are names, and these can be used to retrieve data from within our
code. They need to be kept somewhere so that whenever we need to retrieve those objects, we can use their names to
fetch them. We need some space to hold them, hence: namespaces!

A namespace is a mapping from names to objects. Examples are the set of built-in names (containing functions that
are always accessible in any Python program), the global names in a module, and the local names in a function.
Even the set of attributes of an object can be considered a namespace.


"A scope is a textual region of a Python program, where a namespace is directly accessible."
"""

# MUTABILITY----------------------------------------------------------------------------------------

# If the value can change, the object is called mutable, otherwise the object is called immutable.#

# integers are immutable in python
# age = 42                
# print(id(age))   # id() function to print the IDs.
# age = 43
# print(id(age))

# When we type age = 43, what happens is that another int object is created,
# with the value 43 (also, the id will be different), and the name age
# is set to point to it. So, in fact, we did not change that 42 to 43—we just pointed the name age to a different
# location, which is the new int object whose value is 43.

## NOTE:-
# Python: Integers are immutable. You can’t change their value directly; you create new ones instead.
# C: Integers are mutable. You can modify them directly, but you’re in charge of memory management.


class Person:
    def __init__(self,age):
        self.age = age

# Barry = Person(42)

# print("Current mem address of Barry : ",id(Barry))

# print(Barry.age),print("Current mem address of age : ",id(Barry.age))
# Barry.age = 25
# print("Current mem address of age : ",id(Barry.age))
# print("Current mem address of Barry : ",id(Barry))

# print("Hence, object Barry is mutable and age is immutable as its an integer object.")
# print("Every time you make a change to age , the age variable is created fresh and the value is assigned somewhere else with the same name.")
# print("The previous value of 42 is still present at its memory address with no name.")

# True Division (/)
# Truncated/Floored division (//)
# Exponentiation(**)
#------------------------------------------------------------------------------------------------------------

# Boolean 

"""
>>> int(True)  # True behaves like 1
1
>>> int(False)  # False behaves like 0
0
>>> bool(1)  # 1 evaluates to True in a Boolean context
True
>>> bool(-42)  # and so does every non-zero number
True
>>> bool(0)  # 0 evaluates to False
False

"""

#  Upcasting is a type conversion operation that goes from a subclass to its parent.

# Complex numbers in Python-----------------------------------------------------------------

# c = 1 + 2j  # complex num = a + ib where i = sqrt(-1)
# print(c.conjugate()),print(c.imag),print(c.real)

# Fractions in python-----------------------------------------------------------------------
# from fractions import Fraction

# f = Fraction(0.125)
# print(f.numerator,"/",f.denominator)
# print(f.as_integer_ratio())  # Return a pair of integers(as a tuple), whose ratio is equal to the original Fraction

#----------------------------------------------------------------------------------------------------------

# from decimal import Decimal

# print(Decimal('0.3') - Decimal('0.1') * Decimal(3)) # this solves our previous problem where the result
                                                    # wasn't 0
# For accurate results, the input should be a string or integer

#------------------------------------------------------------------------------------------------------------

# STRING DataType--------------------------------------------------------------------------------------------

name = 'Max'
poem = """
        Errors are red,
        problems are blue,
        Comments are green,
        This is an orange multiline comment,
        enjoy the view...
        """
name = "John Marston"

# print(name.removeprefix("John "))
# print(name.removesuffix("Marston"))

punchline = "You sir, are a fish"

# indexing and slicing 
# my_sequence[start:stop:step]

# sliced = punchline[9:]
# sliced2 = punchline[:8]
# slice3 = punchline[1:16:2] # steps of 2
# print(sliced,"\n",sliced2,"\n",slice3)


# print(f"hi my name is {name}") # f-string
# print("My name is %s , here's a poem : \n %s"%(name,poem)) # format string 


#------------------------------TUPLES--------------------------------------------------

empTup = ()  # empty tuple
a,b,c = 1,2,3   # tuple for multiple assignment
one_elem_tup = (2,) # comma is needed 

# print(2 in one_elem_tup) # membership test using "in"

#swapping using tuples
a,b = 1,2
a,b = b,a
# print(a,b)

# LISTS---------------------------------------------------------------------------------

# Python lists are similar to tuples, but they do not have the restrictions of immutability.

list1 = list("Hello") # list from a string
lis2 = list((1,2,3,4)) # list from a tuple 
lis3 = [1,2,3,4,5]

# lis3.append(78)
# lis3.pop() # remove and return last element frm the list # 78
# lis3.pop(3) # remove the element at index 3  # 4
# lis3.sort(reverse=True) # reverse sort
# print(lis3) 
# lis3.sort() # normal sort
# print(lis3) 
# lis3.clear() # remove all elements
# print(lis3)
# lis3.extend([1,2])
# print(lis3)

# list4 = lis3 + lis2 # adding two lists to make a bigger list
# print(list4)

# lis2_double = lis2 * 2
# print(lis2_double)


#-------------------------SORTING ALGORITHM-----------------------------------------------  	
from operator import itemgetter

a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)] # In this case, the
                                            # sorting on a 2-tuple works by sorting them on the first item in the tuple, 
                                            # and on the second when the first one is the same.
# print(sorted(a))

# print(sorted(a,key=itemgetter(0))) # sort on the basis of first element in tuple
# print(sorted(a,key=itemgetter(0,1)))  # sort on the basis of both first and second elements in tuple
# print(sorted(a,key=itemgetter(1))) # sort on the basis of second element in tuple

# sorting is a mixture of merge and insertion sort
#------------------------------------------------------------------------------------------

# Sets and frozen Sets---------------------------------------------------------------------

small_primes = set()
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)

bigger_primes = set([7,11,13])
# print(small_primes | bigger_primes) #union operator
# print(small_primes & bigger_primes) #intersection operator
# print(small_primes - bigger_primes) # difference operator

small_frozen = frozenset([1,2,3,5])
# no add method available


#-------------------------------------Dictionaries-----------------------------------------

a = dict(A = 1, B = 3)
dic = {'1':'apple','2':'banana'}
currency = {'USA':'Dollar','Japan':'Yen','India':'Rupee'}
# print(currency['India'])
# print(a["A"])

# the is operator, and checks whether the two objects are the same (that is, that they have the
#  same ID, not just the same value)

# print(a is a, currency is currency)

# zip() function to map values---------------------------------------------------------------------------------

Some_dict = dict(zip("ArtTheClown",range(11)))
# print(Some_dict)  # {'A': 0, 'r': 1, 't': 2, 'T': 3, 'h': 4, 'e': 5, 'C': 6, 'l': 7, 'o': 8, 'w': 9, 'n': 10}


lis5 = list(zip("HELLO",range(5)))
# print(lis5)


# keys, values and items of a dictionary

# print(Some_dict.keys())
# print(Some_dict.values())
# print(Some_dict.items())

#--------------------------------------------------------------------------------------------------------------

# Dates and time-----------------------------------------------------------------------------------------------

from datetime import date,datetime,timedelta,timezone,UTC
import time
import calendar as cal
from zoneinfo import ZoneInfo

today = date.today()
# print(today.isoformat())
# print(today.weekday())
# print(today.day,today.month,today.year)
# print(today.timetuple())

# print(time.ctime())
# print(time.localtime())

# print(cal.day_name[today.weekday()])

#--------------------------------------------------------------------------
# ENUMERATIONS
from enum import Enum

list2 = ['apple','banana','orange','guava','cherry']
enum_list2 = list(enumerate(list2))

# print(list(enumerate(list2)))


class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 4

# print(TrafficLight.GREEN)

#-----------------------------------------------------------------------------
## if elif else 

if True:
    pass
else:
    pass

if True:
    pass
elif True:
    pass
else:
    pass

# ternary operator
order_total = 900
discount = 25 if order_total>500 else 0
discount = 200 if order_total > 700 else 0

#---------------------------------------------------------------------------------
# Match - case (aka switch case of Python)

# calculator-------------------------------------------------

# a,b = int(input("Enter num1: ")),int(input("Enter num2: "))
# operator = input("Enter operation: ")

# print("calculating......")

# match operator:
#     case '+':
#         print(a + b)
#     case '-':
#         print(a - b)
#     case '/':
#         print(a / b)
#     case '*':
#         print(a * b)
#     case '**':
#         print(a ** b)
#     case _: # wildcard case 
#         print("Warning: undefined operator detected!")


#-------------------------------------------------------------------------------
# Looping -----for,while--------------------------------------------------------

guns = ['Desert Eagle','AK-47','Colt 1911','Sawed-off shotgun','Thompson 1928']

# for gun in guns:
#     print(gun)

# iterating over a range 
# range(start,stop,end) stop is exclusive and start begins from 0 by default

# for i in range(10):
#     print(i)

even_num_list = list(range(2,21,2))
# print(even_num_list)

names = ['arthur','john','micah']

# for position,name in enumerate(names,start=1):
#     print(position,name)

#  An iterable is: An object capable of returning its members one at a time.
#  Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, 
#  and objects of any classes you
#  define with an __iter__() method or with a __getitem__() method that implements sequence semantics.

people = ['a','b','c','d']
ages = [19,20,18,10]

# lets iterate over both in a pythonic way
# for person,age in zip(people,ages): # zip together elements of people and ages (i.e. link them to each other)
#     print(person,age)

songs = ["Don't Dream its over,","If AND/OR When,","Beanie,"]
artists = ['Crowded House,','Ruel,','Chezile,']
duration_in_min = [4,3,2]

# for song,artist,duration in zip(songs,artists,duration_in_min):
#     print(song,artist,duration)

list7 = [1,2,3,4]
i = 0
# while i < 4:
#     print(list7[i])
#     i += 1

#------------------------------continue and break statements------------------------------------------

# for i in range(10):
#     if i == 6:
#         break    # breaks out of the loop
#     print(i)

# for i in range(10):  # skips the current iteration
#     if i%2 == 0:
#         continue
#     print(i)

#-----------------------------------------------------------------------------------------------------
# exception in else statement

# class DriverException(Exception):
#     pass

# people = [("James", 17), ("Kirk", 9), ("Lars", 13), ("Robert", 8)]
# for person, age in people:
#     if age >= 18:
#         driver = (person, age)
#         break
# else:
#     raise DriverException("Driver not found.")

#----------------------------------------------------------------------------------------------------
# WALRUS(:=) Operator--------------------------------------------------------------------------------



flavors = ["pistachio", "malaga", "vanilla", "chocolate"]
prompt = "Choose your flavor: "
# print(flavors)
# while (choice := input(prompt)) not in flavors:
#     print(f"Sorry,{choice} is not available.")
# print(f"You chose {choice}.")


#---------------------------------------------------------------------------------------------------

# prime number generator 

# primes = []
# upto = 100 # the limit, inclusive
# for n in range(2,upto + 1): # 2 to 101 (101 exclusive)
#     is_prime = True
#     for divisor in range(2,n):
#         if n % divisor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(n)

# print(primes)


# customers = [
#     dict(id=1, total=200, coupon_code="F20"),  # F20: fixed, £20
#     dict(id=2, total=150, coupon_code="P30"),  # P30: percent, 30%
#     dict(id=3, total=100, coupon_code="P50"),  # P50: percent, 50%
#     dict(id=4, total=110, coupon_code="F15"),  # F15: fixed, £15
# ]
# discounts = {
#     "F20": (0.0, 20.0),  # each value is (percent, fixed)
#     "P30": (0.3, 0.0),
#     "P50": (0.5, 0.0),
#     "F15": (0.0, 15.0),
# }
# for customer in customers:
#     code = customer["coupon_code"]
    # percent, fixed = discounts.get(code, (0.0, 0.0))
#     customer["discount"] = percent * customer["total"] + fixed
    
# for customer in customers:
#     print(customer["id"], customer["total"], customer["discount"])


#-----------------------------------------------------------------------------------------------------
# Infinite Iterators

# from itertools import count

# for n in count(2,2):   # count(start,step) # notice how there is no stop parameter 
#     if n > 20:      # stopping it manually
#         break
#     print(n,end=', ')


"""
1. `compress()` combines values from multiple iterators based on logic.
2. It handles unequal lengths gracefully.
3. Example: Filtering even and odd numbers from a data sequence using selectors. 

"""

# from itertools import compress

# data = range(10)
# even_selector = [1,0] * 10 # [1,0,1,0,1,0,1,0....]
# odd_selector = [0,1] * 10 # [0,1,0,1,0,1,0,1.....]
# even_numbers = list(compress(data,even_selector))
# odd_numbers = list(compress(data,odd_selector))
# print(odd_numbers)
# print(even_numbers)
# print(even_selector,odd_selector)


# Permutation-------------------------------------------------------

# from itertools import permutations
# print(list(permutations([1,2,3]))) # 3 factorial is 6
# print(list(permutations("PYTHON"))) # 6 factorial is 720

#------------------------------------------------------------------------------------------------
# non-local variable

# Imagine you have a function within another function.
# If you want to modify a variable from the outer function within the inner function, you use nonlocal.
# Without it, Python would treat that variable as a new local variable within the inner function.


# def change():
#     x = 10
#     def big_change():
#         nonlocal x  # this directly links to the outer x
#         x += 1000
#     big_change()
#     print(x)

# change()


# The global keyword is used within functions to indicate that a variable should not be 
# considered local to that function but rather belongs to the outer (enclosing) scope.

# name = "Dexter"

# def change_name():
#     name = "bruh"

# change_name()
# print(name)  # the name doesn't change as python creates a new variable 
#             # of same name locally for the change_name function

# # to change a global variable----> do this

# def update_name():
#     global name
#     name = "John"

# update_name()
# print(name)

#---------------------------------------------------------------------------------
# functions-----------------------------------------------------------------------

# x = [1, 2, 3]
# def func(x):
#     x[1] = 42  # this changes the original `x` argument!
#     x = "something else"  # this points x to a new string object
# func(x)
# print(x)  # still prints: [1, 42, 3]


# https://pythontutor.com/render.html#mode=display 

# Passing arguments to functions--------------------------------------------------
#  Positional arguments
#  Keyword arguments
#  Iterable unpacking
#  Dictionary unpacking


# pos arg >>  When we call a function, each positional argument is assigned to the parameter 
# in the corresponding position in the function definition

# a,b,c = 1,2,3
# def fun(a,b,c):
#     print(a,b,c)
# fun(a,b,c)

# keyword arg >> Keyword arguments in a function call are assigned to parameters using the name=value syntax

# def func(a,b,c):
#     print(a,b,c)

# func(a = 1,b = 3, c= 5)

# iterable unpacking >>  Iterable unpacking uses the syntax *iterable_name to pass 
# the elements of an iterable as positional arguments to a function

# values = (9,9,9)
# func(*values)

# dictionary unpacking >> Dictionary unpacking is to keyword arguments what iterable unpacking is to positional arguments. We use the
#  syntax **dictionary_name to pass keyword arguments, constructed from the keys and values of a dictionary, to a
#  function

# values = {'a':32,'b':66,'c':4}
# func(**values)

# remember : positional arguments always have to be listed before any keyword arguments

#  First, positional arguments: both ordinary ( name ) and iterable unpacking ( *name )
#  Next come keyword arguments (name=value), which can be mixed with iterable unpacking (*name)
#  Finally, there is dictionary unpacking ( **name ), which can be mixed with keyword arguments ( name=value )

def func(a,b,c,d,e,f):
    print(a,b,c,d,e,f)

# func(1,*(2,3),f = 6,*(4,5))
# func(1, **{"b": 2, "c": 3}, d=4, **{"e": 5, "f": 6})

#-----------------------------------------------------------------------------------
# Optional parameters 

# def add(a=0,b=0):
#     return a + b

# print(add())
# print(add(1,2))

#-----------------------------------------------------------------------------------

# variable positional parameters

# when we define a parameter with an asterisk, *, prepended to its name, we are telling Python that
#  this parameter will collect a variable number of positional arguments when the function is called. Within the
#  function, n is a tuple.

def ECHO_NUM(*n):  
    print(n)

# ECHO_NUM(1,2,3,4,5,6,7,8,9)


#  Variable keyword parameters are very similar to variable positional parameters. The only difference is the syntax
#  (** instead of *) and the fact that they are collected in a dictionary

def funky(**kwargs):
    print(kwargs)

# funky(a=1,b=2,c="funky town")


# The syntax for get() is dictionary.get(keyname, default_value). If the specified key exists, 
# it returns the corresponding value; otherwise, it returns the provided
# default value (or None if no default value is given).


# parameters.variable.db.py
# def connect(**options):
#     conn_params = {
#         "host": options.get("host", "127.0.0.1"),
#         "port": options.get("port", 5432),
#         "user": options.get("user", ""),
#         "pwd": options.get("pwd", ""),
#     }
#     print(conn_params)
#     # we then connect to the db (commented out)
#     # db.connect(**conn_params)
# connect()
# connect(host="127.0.0.42", port=5433)
# connect(port=5431, user="fab", pwd="gandalf")

#------------------------------------------------------------------------------------

# There is a new function parameter syntax, /, indicating that a set of the function parameters must be specified
#  positionally and cannot be passed as keyword arguments.

def func(a, b, /, c):
    print(a, b, c)

# func(1, b=2, c=3) # TypeError: func() got some positional-only arguments passed as keyword arguments: 'b'
# func(1, 2, c=3)  # prints 1 2 3
# func(1,2,3)


def kwo(*a, c):
    print(a, c)

# kwo(1, 2, 3, c=17)  # prints: (1, 2, 3) 7
# kwo(1,2,3,7)        # kwo() missing 1 required keyword-only argument: 'c'

#  Combining input parameters

#Rules
"""
Positional-only parameters come first, followed by a / .
Normal parameters go after any positional-only parameters.
Variable positional parameters go after normal parameters.
Keyword-only parameters go after variable positional parameters.
Variable keyword parameters always go last.
For positional-only and normal parameters, any required parameters must be defined before any optional
parameters. This means that if you have an optional positional-only parameter, all your normal parameters must
be optional too. This rule does not affect keyword-only parameters.

"""

# parameters.all.py
# def func(a, b, c=7, *args, **kwargs):
#     print("a, b, c:", a, b, c)
#     print("args:", args)
#     print("kwargs:", kwargs)
    
# func(1, 2, 3, 5, 7, 9, A="a", B="b")


# return.none.py
def func():
    pass
# func()  # the return of this call won't be collected. It's lost.
# a = func()  # the return of this one instead is collected into `a`
# print(a)  # prints: None


#  When a function calls itself to produce a result, it is said to be recursive.

def fact(n):
    if n in (0,1):
        return 1
    return fact(n-1) * n

# print(fact(15))

#-----------------------------------------------------------------------------------

def moddiv(a, b):
    return a // b, a % b

# print(moddiv(20, 7))  # prints (2, 6)

# lambda function-------------------------------------------------------------------

sum = lambda a,b : a + b
product = lambda a,b : a * b
# print("98 + 76 =",sum(98,76))
# print("23 x 69 = ",product(23,69))

#-----------------------------------------------------------------------------------

# Importing libraries

# import math as m      # importing math library
# from math import *                 # from math import all functions
# from math import sqrt,factorial # importing two functions
# from math import (
#     sqrt,           # multiline import
#     factorial,
#     tan,
#     atan
# )

#-----------------------------------------------------------------------------------

# When defining a function, you can annotate its arguments and return type using the -> syntax.
# (edge_length: float) means edge length takes a float value.
# -> str ---- means it returns a str value
def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."

surface_area_of_cube(2.0)  # (edge_length: float) -> str    
                        # edge_length should be a float 
                        # the return value is str

# having difficulty processing?

import math 
math.factorial(3) # (x: SupportsIndex, /) -> int
# SupportsIndex is Python’s friendly nod to anything that behaves like it supports indexing—whether it’s a list, a tuple, or even just a plain integer.
# factorial returns an int value   (-> int )



#--------------------------------------------------------------------------------------


# A note about !SupportsIndex!
# It represents any type that can be used as an index.
# In other words, it’s useful for hinting that a function or method requires an indexable argument—such as a list, tuple, or string.

#--------------------------------------------------------------------------------------

# map function

#  map(func, *iterables) Returns an iterator that applies 
#  function to every item of iterable, yielding the results.

# print(map(lambda *a:a,range(1,10))) # <map object at 0x00000276ADA416F0> (mem address)
lis_of_sing_tup = list(map(lambda *a:a,range(1,10))) # returns a list of singular tuples
# print(lis_of_sing_tup)  

list_2 = list(map(lambda *a: a,range(4),"bruh")) # [(0, 'b'), (1, 'r'), (2, 'u'), (3, 'h')]

# print(list_2)

# map() is especially useful when you have to apply the same function to one or more collections of objects

#--------------------------------------------------------------------------------------

# zip function

#  zip(*iterables, strict=False)... returns an iterator of tuples, where the i-th tuple contains the i-th element from
#  each of the argument iterables.

# students = ['Mark','Shelly','Vince']
# grades = ['A','B','C']
# print(dict(zip(students,grades,strict=False)))

# students1 = ['Mark','Shelly','Vince','Masuka']
# grade = ['A','B','C']
# print(dict(zip(students1,grade,strict=True))) # ValueError: zip() argument 2 is shorter than argument 1

# If zip() receives strict=True as an argument, 
# it raises an exception if the iterables do not all have the same length

#--------------------------------------------------------------------------------------

# filter() ->  filter(function, iterable) Construct an iterator from those elements of iterable for which function is true. iterable
#  may be either a sequence, a container which supports iteration, or an iterator.

cal_scores = [12,23,13,16,18,34]
fil_list = list(filter(lambda x : x < 20 , cal_scores))  # The lambda function checks whether the value of x is less than 20.
# If x is less than 20, it returns True; otherwise, it returns False
# print(fil_list)

liss = [1,0,1,0,1,0]
# print(list(filter(None,liss))) 

#---------------------------------------------------------------------------------------

# Comprehensions

#  Python offers several types of comprehensions: list, dictionary, and set. 

# 1. List Comprehension

#  A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more
#  for or if clauses.

# squares of natural numbers

# first way
sq = []
for i in range(1,11):
    sq.append(i**2)
# print(sq)

# Second way---using map-------------

# print(list(map(lambda x: x**2,range(1,11))))

# third way---using comprehension------------

squares = [x**2 for x in range(1,11)]
# print(squares)

# filtering out odd squares

#1 using map and filter

squair = list(map(lambda x: x**2,filter(lambda x: x % 2 != 0, range(1,11))))
# print(squair)

#2 using list comprehension

sq_lis = [n**2 for n in range(1,11) if n % 2 != 0]
# print(sq_lis)

#---------------------------------------------------------------------------------------------
# NESTED COMPREHENSIONS-----
# squ = [(x**2,y**3) for x in range(1,5) for y in range(1,5)]
# print(squ,len(squ),"\n\n\n")

# squ2 = []
# for x in range(1,5):
#     for y in range(1,5):
#             squ2.append((x**2,y**3))
            
# print(squ2,len(squ2))


# matrix = [[x for x in range(3)] for _ in range(3)]
# print(matrix)
# Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


# items = "ABCD"
# pairs = [ (items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]
# print(pairs)



#--------------------------------------------------------------------------------

# DICTIONARY Comprehension

from string import ascii_lowercase
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
# print(lettermap)

#  {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
#  'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
#  'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
#  'w': 23, 'x': 24, 'y': 25, 'z': 26}

# it reads like : c is mapped to k for k and c in enumerate(create iterator) (a,1), (b,2), (c,3) and so on..

#---------------------------------------------------------------------------------

# Set Comprehensions

word = "ART"
letters1 = {c for c in word}
# print(letters1)

word2 = "PYTHONISFUN"
letters2 = set(c for c in word2)
# print(letters2)

#----------------------------------------------------------------------------------

"""
Generators are of two types:

Generator functions: These are similar to regular functions, but instead of returning results through return
statements, they use yield , which allows them to suspend and resume their state between each call.

Generator expressions: These are similar to the list comprehensions we have seen in this chapter, but
instead of returning a list, they return an object that produces results one by one

"""


# gen functions

def get_square_gen(n):
    for x in range(n):
        yield x**2

squares = get_square_gen(4) # creates a generator object

# print(squares) # <generator object get_square_gen at 0x000002CCF5A4A670>
# print(next(squares)) # 0
# print(next(squares)) # 1
# print(next(squares)) # 4
# print(next(squares)) # 9

# any further call to next will keep raising StopIteration
# print(next(squares))

"""
What Is yield?
yield is used in Python to create generator functions.
Instead of returning a result immediately, a generator function yields values one at a time.

When to Use yield?
Use yield when processing large data sets or streams.
It’s perfect for scenarios where you don’t want to load everything into memory at once.

"""


def fibonacci(N):
    """Return all fibonacci numbers up to N."""
    yield 0
    if N == 0:
        return
    a = 0
    b = 1
    while b <= N:
        yield b
        a, b = b, a + b

# print(list(fibonacci(10)))
# print(list(fibonacci(50)))


#-----"yield from" expression---


def print_squares(start, end):
    yield from (n**2 for n in range(start, end))
    
# for n in print_squares(2, 5):
#     print(n)


"""
This explains how a for loop works. When you call for k in range(n), what happens under the hood is that the
for loop gets an iterator out of range(n) and starts calling next on it, until StopIteration is raised, which tells
the for loop that the iteration has reached its end.

"""


# Generator expression-------------------
cubes = (k**3 for k in range(1,11))
# print(type(cubes)) # <class 'generator'>
# print(list(cubes)) # this will exhaust the generator
# print(list(cubes)) # nothing more to give

#-------------------------------------------------------------------------

# Object Oriented Programming in Python

