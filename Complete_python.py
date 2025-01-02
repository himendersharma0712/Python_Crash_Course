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


#---------decorators------------------------------------------
from time import sleep,time

# def f():
#     sleep(0.3)

# def g():
#     sleep(0.5)

# t = time() # start timer
# f()  # wait for 0.3 seconds
# print("f took : %r"%(time() - t)) # current time - start time

# t = time() # start timer
# g() # wait for 0.5 seconds

# print("g took : %r"%(time() - t))

# Now, lets use decorator to implement above code ->>

# def measure(func): # takes function as argument
#     t = time()
#     func()
#     print(func.__name__,"took:",time()-t)

# measure(f)
# measure(g)

# Another way--->

# def custom_f(sleep_time=0.1):
#     sleep(sleep_time)

# def measure(func,*args, **kwargs):
#     t = time() # start_time
#     func(*args, **kwargs)
#     print(func.__name__,"took:",time()-t) # current_time[aka time()] - start_time[aka t]

# measure(custom_f,sleep_time = 3)
# measure(custom_f,2)

# import math as m

# def fact(n):
#     return m.factorial(n)

# measure(fact,2147422)  # fact took: 29.568504571914673

# ONE MORE WAY!!!!

# from time import sleep, time

# def f(sleep_time=0.1):
#     sleep(sleep_time)
    
# def measure(func):
#     def wrapper(*args, **kwargs):
#         t = time()
#         func(*args, **kwargs)
#         print(func.__name__, "took:", time() - t)
    # return wrapper

# f = measure(f)  # decoration point
# f(0.2)  # f took: 0.20128178596496582
# f(sleep_time=0.3)  # f took: 0.30509519577026367
# print(f.__name__)  # wrapper  <- ouch!


# One decorator 
# wht follows is pseudocode (don't try to run it):-->

"""
def func(arg1, arg2, ...):
    pass
func = decorator(func)

---- is equivalent to the following:---

@decorator
def func(arg1, arg2, ...):
    pass

"""

# multiple decorators-->

"""
def func(arg1, arg2, ...):
    pass
func = deco1(deco2(func))

# is equivalent to the following:
@deco1
@deco2
def func(arg1, arg2, ...):
    pass


When applying multiple decorators, it is important to pay attention to the order. In the preceding example, func()
is decorated with deco2() first, and the result is decorated with deco1(). A good rule of thumb is the closer the
decorator is to the function, the sooner it is applied.

"""


# lets fix the previous function where it printed wrapper instead
# of the function name

# from time import sleep, time
# from functools import wraps

# def measure(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         t = time()
#         func(*args, **kwargs)
#         print(func.__name__, "took:", time() - t)
#     return wrapper

# @measure
# def f(sleep_time=0.1):
#     """I'm a cat. I love to sleep!"""
#     sleep(sleep_time)
# f(sleep_time=0.3)  # f took: 0.30042004585266113
# print(f.__name__)  # f
# print(f.__doc__ )  # I'm a cat. I love to sleep!


#-----------------------------------------------------------------------------
# Python OOP---------------------------------------

class Person:
    species = "Human"   # Any name defined in the body of a class
                        # becomes an attribute that belongs to that class

# print(Person.species)
# Person.alive = True  # added dynamically
# print(Person.alive)

# man = Person() # creating an object
# man.name = 'John'       #  The man instance also has two attributes that belong to its own namespace 
# man.surname = 'Doe'     #  and are therefore called instance attributes: name and surname.
# print(man.name,man.surname)   


#----What happens if class and object have same attributes ??

# Instance attrib overshadow class attributes----
# this is similar to local variables being preferred over global if both have the same name
class Coordinate:
    x,y = 1,2

A = Coordinate()
# print(A.x)  # 1 (from class attrib)
# print(A.y)  # 2 (from class attrib)
# A.x = 12    # A gets its own 'x' attrib
# A.y = 24    # A gets its own 'y' attrib
# print((A.x,A.y))   # prints (12, 24) 

A.z = 23 # A is a 3-d point now !
# print(A.z) 

# print(Coordinate.z) # z is an instance attrib  
                    # specific to A
# AttributeError: type object 'Coordinate' has no attribute 'z'

# class Square:
#     side = 8
#     def area(self):  #  # self is a reference to an instance
#         return self.side**2

# sq = Square()

# print(sq.area())
# print(Square.area(sq)) # 64(side is found on class)
# sq.side = 10
# print(sq.area())  # 100 (side is found on the instance)

"""

# From within a class method, we can refer to an instance by means of a special argument, called self by convention

Either you pass the instance to the method call ( Square.area(sq) ), which
within the method will take the name self, or you can use a more comfortable syntax, sq.area(), and Python will
translate that for you behind the scenes.

"""
# class Price:
#     def final_price(self,vat,discount=0):
#         """Returns price after applying vat and fixed discount"""  # docstring
#         return (self.net_price * (100 + vat) / 100) - discount

# p1 = Price()
# p1.net_price = 100 # instance attribute
# print(Price.final_price(p1,20,10)) # 110 
# # we pass the instance to self, 20 to vat and 10 to discount

# print(p1.final_price(20,10)) # self = p1 behind the scenes
#                             # and self.net_price yields 100


# Instead of assigning net_price to p1, we can ->

class Rectangle:
    def __init__(self,side_a:float,side_b:float) -> float:
        self.side_a = side_a
        self.side_b = side_b
        
    def area(self):
        return self.side_a * self.side_b

# r1 = Rectangle(12,5)
# print(r1.side_a,r1.side_b,r1.area())

# Rectangle.__init__(r1,side_a=12,side_b=5) # Initializing manually using class 
# print(Rectangle.area(r1)) # passing object to method 

# r2 = Rectangle(13,7)
# print(r2.area(),r2.side_a,r2.side_b)

"""
Inheritance means that two objects are related by means of an Is-A type of relationship. On the other hand,
composition means that two objects are related by means of a Has-A relationship
"""

class Engine:
    def start(self):
        pass
    def stop(self):
        pass

class ElectricEngine(Engine): # Is-A Engine
    pass

class V8Engine(Engine):  # Is-A Engine
    pass

class Car:
    engine_cls = Engine
    def __init__(self):
        self.engine = self.engine_cls()
    def start(self):
        print(
            f"Starting {self.engine.__class__.__name__} for",
            f"{self.__class__.__name__}...Wroom"
        )
    def stop(self):
        self.engine.stop()

class RaceCar(Car): # Is-a car 
    engine_cls = V8Engine	

class CityCar(Car): # Is-a car  
    engine_cls = ElectricEngine

class F1Car(Car): # Is-a car 
    pass

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()

cars = [car,racecar,citycar,f1car]

for car in cars:
    car.start()

"""
When we define class A(B): pass, we say A is the child of B, and B is the parent of A. The parent and base
classes are synonyms, and so are child of and derived from. Also, we say that a class inherits from another class, or
that it extends it
"""

# isinstance() method Returns True/False based on whether 
# an object is an instance of a class or of a subclass thereof

# print("car is an instance of Car: " ,isinstance(car,Car))
# print("f1car is a car: ",isinstance(f1car,Car))
# print("racecar is a F1Car: ",isinstance(racecar,F1Car))


car_classes = [Car, RaceCar, F1Car]

# for class1 in car_classes:
#     for class2 in car_classes:
#         is_subclass = issubclass(class1, class2)
#         msg = "{0} a subclass of".format(
#         "is" if is_subclass else "is not"
#         )
#         print(class1.__name__, msg, class2.__name__)

"""
Also, if you want to use a name in your code that clashes with a Python-reserved keyword 
or a built-in function or class, the
convention is to add a trailing underscore to the name. 

Please remember that, if you do not
specify a base class, brackets are optional 
and in practice are never used.
Therefore, writing class A: pass or class A(): pass 
or class A(object): pass are all equivalent. 
The object class is a special class in that 
it hosts the methods that are common 
to all Python classes, and it does not
allow you to set any attributes on it.


"""
class A(object):
    pass

class A:
    pass

class A():
    pass 

# are all equivalent


# Let us see how we can access a base class from within a class---->

# class Book:
#     def __init__(self, title, publisher, pages):
#         self.title = title
#         self.publisher = publisher
#         self.pages = pages
# class Ebook(Book):
#     def __init__(self, title, publisher, pages, format_):
#         Book.__init__(self, title, publisher, pages)
#         self.format_ = format_
        
# ebook = Ebook("Learn Python Programming", "Packt Publishing", 500, "PDF")
# print(ebook.title)  # Learn Python Programming
# print(ebook.publisher)  # Packt Publishing
# print(ebook.pages)  # 500
# print(ebook.format_)  # PDF

"""
In this example, we tell Python to call the __init__()
method of the Book class; we feed self to that call, making sure that we bind it to the present instance.
If we modify the logic within the __init__() method of Book, we do not need to touch Ebook; the change will
transfer automatically.
"""

# Instead of the above approach , we can use super() method to call the 
# parent class's init method
# class Book:
#     def __init__(self, title, publisher, pages):
#         self.title = title
#         self.publisher = publisher
#         self.pages = pages
# class Ebook(Book):
#     def __init__(self, title, publisher, pages, format_):
#         super().__init__(title,publisher,pages)
#         # Another way to do the same thing is:
#         # super(Ebook, self).__init__(title, publisher, pages)
#         self.format_ = format_
# ebook = Ebook(
#     "Learn Python Programming", "Packt Publishing", 500, "PDF"
# )

# print(ebook.title)  # Learn Python Programming
# print(ebook.publisher)  # Packt Publishing
# print(ebook.pages)  # 500
# print(ebook.format_)  # PDF

# Method Resolution Order(MRO)-------------------------------------------------

#  Python provides a way to always know the order in which classes are 
#  searched on attribute lookup: the method resolution order (MRO).

"""
we know that when we ask for someobject.attribute and attribute is not found on that object,
Python starts searching in the class that someobject was created from. If it is not there either, Python searches up
the inheritance chain until either attribute is found or the object class is reached.

"""

class A:
    label = "a"
class B(A):
    label = "b"
class C(A):
    label = "c"
class D(B,C):
    pass

d = D()
print(d.label) # hypothetically, could be 'b' or 'c'
# but it prints 'b'
#  since B is the leftmost among the base classes of D aka (B,C)
# if it was (C,B) then C would be printed

print(d.__class__.mro())

# lookup order : D -> B -> C -> A -> object

#===============================================================================

# CLASS AND STATIC METHODS======>

#  When you create a class object, Python assigns a name to it. That name acts as a namespace, and sometimes it
#  makes sense to group functionalities under it.  Static methods are perfect for this use case.
# . Unlike instance methods, they do not need to be passed an instance when called.
class RDR:
    @staticmethod
    def print_protag():
        print("John Marston")
        
    @staticmethod
    def print_allies():
        print("Marshal")
        print("Bonnie McFarlane")
        print("West Nigel Dickens")
    
    @staticmethod
    def print_enemies():
        print("Bill Williamson")


# RDR.print_allies()
# RDR.print_enemies()
# RDR.print_protag()


class MathUtil:
    @staticmethod
    def factorial_(n):
        if n != 0 and n != 1:
            return n * MathUtil.factorial_(n-1)
        else:
            return 1
    
    @staticmethod
    def sum_of_numbers_till_n(n):
        return (n * (n + 1)) / 2

    @staticmethod
    def sum_of_squares_of_n_num(n):
        return (n*(n+1)*(2*n+1))/6
    
    @staticmethod
    def sum_of_cubes_till_n(n):
        return ((n * (n + 1)) / 2)**2
    

# print(MathUtil.sum_of_cubes_till_n(3))
# print(MathUtil.factorial_(10))
# print(MathUtil.sum_of_numbers_till_n(10))
# print(MathUtil.sum_of_squares_of_n_num(10))


#----CLASS Methods---->

"""
Class methods are slightly different from static methods in that, like instance methods, they also receive a special
first argument. In their case, it is the class object itself, rather than the instance. A very common use case for class
methods is to provide factory capability to a class, which means to have alternative ways to create instances of the
class.
"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @classmethod
    def from_tuple(cls,coords):   # cls is Point
        return cls(*coords)
    
    @classmethod
    def from_point(cls,point):   # cls is Point
        return cls(point.x,point.y)
    
p = Point.from_tuple((3,7))
# print(p.x,p.y) # 3 7

# q = Point.from_point(p)
# print(q.x,q.y) # 3 7

# Within each class method, the cls argument refers to the Point class. As with the instance method, which takes
#  self as the first argument, the class method takes a cls argument. 