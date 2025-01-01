
# Comments start with a pound, hash or octothorpe------------------------------------------------------------

# print("Hello World\n")

# if 1>0 :
#     print("d")
# else:
#     print("e")


# print("whatever")

# print("Hens",25+30/6)   # prints Hens and 30

# print("something",3+2 < 5-7)

# print("Hens",(25+30)/6.0)

# print(7/4)

# Variables-----------------------------------------------------------------------------------------------------

# cat_alive = True
# dog_ate_food = True
# phone_no = 98036
# food = "pasta"
# roll_no = "CR24332"
# floating_num = 3.2
# integer_num = 3838

# floating_no = floating_num * integer_num

# print(floating_num," multiplied by ",integer_num, " is ",floating_no)

# Format string--------------------------------------------------------------------------------------------------

# height = 73
# name = "Barry"
# num = 23.5
# weight = 75
# print("I am %d inches tall and I weigh %d kg and my name is %s.\nA float num is %f " %(height,weight,name,num))

# print("%d + %d = %d"%(height,num,height+num))

# f strings

# print(f"I just watched {name}")
# print(f'Barry is {height} inches tall')

# print("cheeseburger "+"is tasty"), print("but its not healthy"), print("wow you can add commas btw function calls")

# multiple function calls can be made with separation by ','

# print(""" writing on multiple
#         lines like
#         this is actually
#         fun""")

# print("\\backslash")

# print("\' \" ")

# print("\a")

# Taking input--------------------------------------------------------------------------------------------------------

# Name = input("Enter name: ")
# Age = int(input("Enter Age: ")) # input function always returns string  # so we typecast string to int
# print("Your name is %s and age is %d."%(Name,Age))

# Unpacking argv (argument variable)----------------------------------------------------------------------------------

# from sys import argv

# script,first,second,third = argv

# print("The script is called",script),print("1st arg: ",first),print("2nd arg: ",second),print("3rd arg: ",third)

# in terminal type: python Hello_world.py skibidi ohio rizz

#---------------------------------------------------------------------------------------------------------------------
# using arguments in script

# from sys import argv

# script,user_name = argv

# prompt = '> '

# print("Hi %s , you just ran a script called %s"%(user_name,script))

# Donuts = input(("%s,do you like donuts? "%user_name))

# Workout = input("%s,do you like an intense workout session? "%user_name)

# RAM = int(input("How much ram does your PC have, %s ?"%user_name))

# print("How tall are you in inches? ")
# Height = input(prompt)
# print("OUTPUT:- Donuts: %s , RAM: %d GB, Workout: %s"%(Donuts,RAM,Workout))

# type in terminal: python Hello_world.py Max

# READING FILES---------------------------------------------------------------------------------------------------

# from sys import argv

# script,filename = argv # unpacks argv into script and filename

# file1 = open(filename,"r") # open file in read mode

# print("Here's your file %s"%filename)
# print(file1.read(-1)) # if size is negative or omitted, read until EOF.

# print(file1.readline()) # Read until newline or EOF.

# print("Type the filename again:")
# file_name = input("> ")

# file2 = open(file_name,"r") # opens the file input by the user in read mode

# print(file2.read(-1)) #prints all the text till EOF(end_of_file) , read from the file

# file1.close() # close the file
# file2.close()
# type in terminal:  python Hello_world.py rickroll.txt

#----------------------------------------------------------------------------------------------------------

# Reading and writing files

# from sys import argv

# script, filename = argv

# print("Lets erase the file called %s"%filename)

# file = open(filename,"w") # open file in write mode

# file.truncate() # If the size is not specified, 
# # it truncates the file to the current position

# print("FIle erased successfully!!\n\nLets write something else in the file: ")

# line1 = input("Enter line1: ")
# line2 = input("Enter line2: ")
# line3 = input("Enter line3: ")

# # lets write this into the file
# file.writelines([line1,"\n",line2]),file.write("\n"),file.write(line3)

# # finally close the file
# file.close()

# file = open(filename,'a') # open file in append mode

# file.write("\nThis is the appended text--> this file was written by Anonymous")

# The truncate() method in Python is used to resize a file to a specified size.

#----> type in terminal:  python Hello_world.py rickroll.txt

# COPYING ONE FILE TO ANOTHER-----------------------------------------------------------------------------------------------------

# from sys import argv
# from os.path import exists

# script,file_dest,file_src = argv

# print("Copying from %s to %s"%(file_src,file_dest))

# Src_file = open(file_src,"r")
# Data_frm_src = Src_file.read() # read everything till EOF by default

# print("The data from input file is %d bytes long"%len(Data_frm_src))

# print("Does the destination file exist? %r"%exists(file_dest))

# Des_file = open(file_dest,"w")
# Des_file.write(Data_frm_src)

# print("Alright! Done!")

# Des_file.close()
# Src_file.close()

#>>>>terminal command: python Hello_world.py rickroll.txt read_me.txt

# Functions-------------------------------------------------------------


def print_two(*args):
    a,b = args
    print("arg1: %s and arg2: %s"%(a,b))
    
# print_two(1,2)

def fun():
    print("No parameters")
    
# fun()

def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    
# cheese_and_crackers(10,20)

# Test to confirm if values can be switched by call by value method of passing variables
# a = 3
# b = 2
def switch(a,b):
    temp = b
    b = a
    a = temp

# switch(a,b) # calling the function
# print("a = ",a,"b = ",b) # prints a = 3 b = 2


# More about functions-------------------------------------------------------------------------


# from sys import argv

# script,input_file = argv

# def print_all(f):
#     print(f.read())

# def rewind(f):
#     f.seek(0)

# def print_a_line(line_count,f):
#     print(line_count,f.readline())

# current_file = open(input_file,"r")

# print("Lets print the whole file: ")

# print_all(current_file)

# print("\nNow lets rewind and go back to the beginning of the file.\n")

# rewind(current_file)

# print("Lets print three lines: ")

# current_line = 1 # 1    # all it does is mark the line index nothing else 
# print_a_line(current_line,current_file)

# current_line = current_line + 1 # 2
# print_a_line(current_line,current_file)

# current_line += 1 # current_line = current_line + 1
# print_a_line(current_line,current_file)

#>> terminal cmd: python Hello_world.py rickroll.txt


def add(a,b):
    return (a+b)

def multiply(a,b):
    return a*b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def remainder(a,b):
    return a%b


#---------------------------------------------------------------------------------------------------------------

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# refer to the output from the txt file called "OUTPUT"


#---------------------------------IF - ELSE AND ELIF(else if)----------------------------

# A = 2
# B = 3
# C = 7

# if A > B :
#     print(A)

# elif B > C:
#     print(B)

# else:
#     print(C)


# buses = 10
# cars = 10

# if buses > cars:
#     print("That's too many buses.")
# elif buses < cars:
#     print("Maybe we could take the buses.")
# else:
#     print("We still can't decide.")


#------------------------------LOOPS & LISTS---------------------------------

# Fruits = ['apple','banana','orange'] # list

# for fruit in Fruits:
#     print(fruit)

# Days = ['Mon','Tue','Wed'] 
# Days.append('Thu'), Days.append('Fri'), Days.append('Sat'), Days.append('Sun') # appending to list or adding elements from the end

# print(Days)

# Number_list = [] # empty list

# for i in range(0,8): # range(start,stop,step)
#     Number_list.append(i+1)

# print(Number_list)

# for number in Number_list:
#     if (number%2) == 0: # even numbers
#         print(number)


# Odd_num = []

# for i in range(1,20,2): # numbers with a step of 2 aka odd numbers
#     Odd_num.append(i) # append odd numbers to Odd_num

# print(Odd_num)

# while loops---------------------------------------------------------------------------

# i = 0
# num_lis = []
# while i < 10:
#     num_lis.append(i+1)
#     i+=1

# # print(num_lis)

# while i < 11: # i = 10
#     while i < 15: # i never goes above 15 and hence its an infinite loop
#         for i in range(10): # here i resets to 0 and finally becomes 10 
#             print("%d\t"%(i+1))
#         i+=1 # i = 10 + 1


# Accessing elements of a list using index-----------------------------------------------

# some_list = [1,2,3,4,5,6]

# first = some_list[0] # 1
# second = some_list[1] # 2
# third = some_list[2]  # 3
# fourth = some_list[3]  # 4 

# print(first,second,third,fourth)


#--------------------EXIT FUNCTION----------------------------------------------------------

# from sys import exit

# def type_exit():
#     text = input("Type exit: ")
#     if text == "exit":
#         exit(0)
#     else: 
#         for i in range(10):
#             print("crazy")

# type_exit()

#--------------------------------------------------------------------------------------------


# Some python keywords and their use---------------------------------------------------------

#//*-------------del keyword------------------------------------------------------
# list1 = [1,2,2,3,4,5]
# del list1 # delete list1
# print(list1) # NameError: name 'list1' is not defined. Did you mean: 'list'?

# Name = "Barry"
# del Name # delete Name
# print(Name) # NameError: name 'Name' is not defined
#/*********************************************************************************/

#---------------------with keyword-------------------------------------------------

# with open("read_me.txt","r") as file: # with opens and closes the file itself
#     print(file.read())
    
# with open("rickroll.txt","a") as file2: # with opens and closes the file itself
#     file2.write("\nTake this beach")
    
#----------------------------------------------------------------------------------

#------------------------assert keyword--------------------------------------------

"""The assert keyword in Python is a powerful debugging tool that 
helps ensure the smooth flow of code by verifying assumptions made by the programmer. 
Assertions are boolean expressions that check if a statement is true or false. 
If the statement is true, the program continues execution; if false, it raises an AssertionError and stops execution."""

# a = 100
# b = 1
# print("The value of a/b is : ")
# assert b > 10 , "b is less than 10"
# print(a/b)

#-------------------------------------------------------------------------------------


"""In Python, the 'is' keyword is used to test object identity. 
This means it checks whether two variables point to the same object in memory. 
It is different from the == operator, which checks if the values of two variables are equal.
"""
# a = 3
# b = 5

# print("Is a, b? ",a is b) # False
# print("Is a, a?",a is a)  # True

# joey = "human"
# mark = "humane"

# print(joey is mark)
# print(mark is mark)

#-------------------------------------------------------------------------------------

# yield keyword-----------------------------------------------------------------------

#In Python, yield is a keyword used in a function to make it a generator, 
# allowing it to produce a sequence of values lazily, 
# one at a time, and maintain its state between calls.

def gen_func(x):
    for i in range(1,x):
        yield i 

# Using the generator function
# gen = gen_func(5)
# print(next(gen))
# print(next(gen))

#--------------------------------------------------------------------------------------

#pass keyword

def func():
    pass

#--------------------------------------------------------------------------------------

#lambda functions

sum = lambda a,b: a + b
product = lambda a,b: a * b
# print(sum(1,2))
# print(product(3,4))


#--------------------------------------------------------------------------------------
# try, except and finally-------------------------------------------------------------

# a , b = 200,0

# try:
#     result = a/b
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print("Execution of divide_numbers completed.")


# fileNotFoundError--------------------------------------------------------------------

# filename = "myfile.txt"

# try:      # open file in read mode for reading
#     with open(filename,"r") as file:
#         print(file.read())

# except FileNotFoundError as e:
#     print(e)

# finally:
#     with open(filename,"w") as file:     # if file doesn't exist then write it to existence
#         file.write("null")

#---------------------------------------------------------------------------------------

# exponentiation operator (**)

b = 2**4 # b = 16
c = 3**4 # c = 81

#---------------------------------------------------------------------------------------
# The exec keyword in Python is used to execute Python code dynamically. 
# It takes a string containing valid Python code and executes it as if it were part of the program.

# code = 'a = 5\nb = 10\nprint("Sum:", a + b)'  
# exec(code)  # Executes the code string; output will be "Sum: 15"
#---------------------------------------------------------------------------------------

# something bout lists------------------------------------------------------------------

# ten_things = "apple banana orange kiwi kale gale punisher"

# stuff = ten_things.split(' ')
# extra_stuff = ["momo","Pennywise","Art"]

# while len(stuff) != 10:
#     item = extra_stuff.pop()
#     stuff.append(item)
    
# print(stuff)

#-------------------------DICTIONARIES----------------------------------------------

# Abbr = {
#     'brb' : "be right back",
#     'np': "no problem",
#     'gtg': "got to go",
#     'pov': "point of view",
#     'ifykyk': "if you know you know"
# }

# print(Abbr["brb"])
# print(Abbr["ifykyk"])
# del Abbr['np']

#----------------------------Object-Oriented-Programming----------------------------

# class Draw():
#     def __init__(self,char,num):
#         self.char = char
#         self.num = num
        
#     def draw_line(self):
#         for i in range(self.num):
#             print(self.char,end=" ")

# star_drawing_tool = Draw('*',5)

# star_drawing_tool.draw_line()

# dollar_drawing_tool = Draw('$',100)

# dollar_drawing_tool.draw_line()

#--------------------------------------------------------------------------------------

#--program to calculate roots of a quadratic-----------------------------------------
# import math 

# def roots_of_quad(a,b,c):
#     det = b**2 - 4*a*c
#     x1 = (-b + math.sqrt(det))/ 2*a
#     x2 = (-b - math.sqrt(det))/ 2*a
#     roots = [x1,x2]
#     return roots

# a,b,c = int(input("Enter a: ")),int(input("Enter b: ")),int(input("Enter c: "))
# print(roots_of_quad(a,b,c))

#-------------------------------------------------------------------------------------


#--------------------------Inheritance------------------------------------------------

# class Parent(object):
    
#     def implicit(self):
#         print("Parent implicit()")


# class Child(Parent): # syntax for inheriting  # Child is a parent
#     pass

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit() # same function is called from the class which inherits from parent


# overriding parent function

# class GrandChild(Child):
#     def implicit(self): # overriding the original function
#         print("I am the grandchild")

# grand_child = GrandChild()
# grand_child.implicit()

#-------------------------------------------------------------
# super function

# class Dad(object):
#     def dialogue(self):
#         print("Say my name.")

# class Son(Dad):
#     def dialogue(self):
#         super(Son,self).dialogue()
#         print("You're Heisenberg")
        
# dad = Dad()
# son = Son()

# dad.dialogue()
# son.dialogue()

# more on using super()

# class Parent(object):
#     def __init__(self):
#         print("This is parent's property.")

# class Child(Parent):
#     def __init__(self,age):
#         self.age = age
#         print("I am %s."%self.age)
#         super(Child,self).__init__()

# son = Child("10 yrs old")

#------------------------------------------------------------------
# Composition over Inheritance------------------------------------

# class Other(object):
#     def override(self):
#         print("OTHER override()")

#     def implicit(self):
#         print("OTHER implicit()")

#     def altered(self):
#         print("OTHER altered()")

# class Child(object):
#     def __init__(self):
#         self.other = Other()

#     def implicit(self):
#         self.other.implicit()

#     def override(self):
#         print("CHILD override()")

#     def altered(self):
#         print("CHILD, BEFORE OTHER altered()")
#         self.other.altered()
#         print("CHILD, AFTER OTHER altered()")

# son = Child()

# son.implicit()
# son.override()
# son.altered()

