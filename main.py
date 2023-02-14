#Recursion: the repeated application of the same procedure to a smaller problem. Lets up tackle complex problems by reducing the problem to a simpler one.
#In programming, recursion is a way of doing a repetitive task by having a function call itself.
#Recursion in python can only happen 1000 times in each function when called.

#!usr/bin/python3
#the comment above is needed if you are executing on linux

n = 1
m = 8
string = "I am a genius"
string[n] #this shows the nth character from a string, ofc starting from number 0
string[-1] #when there is a negative number, it starts from the end of the string starting with the number -1

# Slice: the portion of a string that can contain more than one character; also sometimes called a substring.
string[n:m] # it takes the characters from n to m including those ofc
string[:n] # it takes the first n characters
string[n:] # it takes the characters after n characters

# Method: a function associated with a specific class

string.index("A") # finds where the character "A" is in the string, but if it is mentioned more than one time, it will output where it mentioned it first.
"Cats" in string # outputs if the substring "Cats" is in the string.

string.replace("n", "m") # a method that outputs the same string but every "n" character is replaced with "m" (can be used to remove space between words in a sentence).
string.upper() # a method that outputs the string all in uppercase.
string.lower() # a method that outputs the string all in lowercase.
string.strip() # a method that outputs the string without the surrounding spaces (spaces at the end and beginning).
string.lstrip() # a method that outputs the string without the spaces/indents at the left side.
string.rstrip() # a method that outputs the string without the spaces/indents at the right side.
string.count("e") # a method that outputs the number of times the letter "e" was mentioned in the string.
string.endswith("ing") # a method that checks whether the string ends with "ing" or not, output is boolean.
string.isnumeric() # a method that checks if the string is a numerical value.
string.join(["This", "is", "a", "sentence"]) # a method that outputs the list of words with the string between them.
string.split() # a method that outputs a list of all the words in the string.
string[::-1] # a method that outputs the reverse of a string
name, age = "Albraa", 18
print("Your name is {}, and your age is {}.".format(name, age)) # a method that replaces the first "{}" with the first argument in the format operation and so on.
print("Your lucky number is {number}, {name}.".format(name=name, number=number)) # a method for formatting the variables in the string.
price = 98
print("Your total price is ${:.2f}".format(price)) # a method for displaying the variable but with only two decimal places.

# Lists: Sequences of elements of any type, and are mutable.
myList = ["My", "name", "is", "Albraa"] # This is a how a list is made
"My" in myList # This method checks if a certain string is inside a list
myList[0] #How to output a certain string in a list with indexing
# If something is said to be mutable, it means it can be changed.
myList.append("Alsakor") # This method adds the string in quotes to the end of the list.
myList.insert(0, "Alsakor") # This method adds the string in quotes to the specific location without deleting the string that was there, but rather pushes the list
myList.remove("Alsakor") # This method removes the string from the list no matter the position.
myList.pop(3) # This method removes the string in index number 3 (4th string)
myList[n] = "Alsakor" #This method replaces the string at index n with the string in quotes.
myList.sort() #sorts he items in the list
myList.reverse() #reverses the order of the list
myList.clear() #removes all the items of the list
myList.copy() #creates a copy of the list
myList.extend(other_list) #adds/appends all the items in the list in the paranthesis to "myList"

def myFunction():
      print("something")
# Tuples: just like lists but they are immutable (cant be changed).
myTuple = ("cat", "horse", "dog") #tuples are declared the same way except you use paranthesis "()"
# Since a function returns a tuple, you can assign variables to the output the function gives
result = myFunction() # Let's say this function returns a tuple with three values
A, B, C = result # Here you are assigning the variables to the corresponding strings in the returning tuple

for x in myList:
      print(x) #here with a loop you can get every object in the list and do something with it

for num, obj in enumerate(myList):
      print(num + "-" + obj) #here the first variable takes the index number of the object and the second one takes the value of the object itself.

myList = [ x*3 for x in range(1,101)] #here instead of making the loop, it made it shorter, here it takes x*3 of every number from the range.
myList = [ x for x in range(1,101) if x%3 == 0] #here it does the same thing except there is a condition met.

#! Dictionaries

myDictionary = { #This is a dictionary, in a dictionary you access things with their keys/values
      "name": "Albraa",
      "age": 18,
      "phone": 5370623850
}
myDictionary["name"] #This accesses the value of "name" in the dictionary
myDictionary["name"] = "Ahmad" #This changes the value of "name" in dictionary
myDictionary["newKey"] = 18 #here you made a new field with a value in it
"age" in myDictionary #here it sees if there is such a field/key in the dictionary and returns a boolean
del myDictionary["phone"] #this deletes the field in the square brackets
for n in myDictionary:
      print(n) #this prints the name of the field and not its value
      print(myDictionary[n]) #this prints the value of that field in the dictionary

myDictionary.keys() #this method gives you the names of the fields in the dictionary
myDictionary.values() #this method gives you the values only in the dictionary
myDictionary[somekey] = myDictionary.get(somekey, 0) +1 #*this here sets a new key in the dictionary called "somekey" and passes the 0 value to it, but the +1 at the end adds to the value
myDictionary[somekey] = myDictionary.get(somekey, 0) +1 #*this adds again to the value, making the value equal to 2, this is valuable when you have an empty list and you scan through a file
import operator
sorted(myDictionary.items(), key=operator.itemgetter(0)) #sorting the dictionary based on the keys
sorted(fruit.items(), key=operator.itemgetter(1)) #sorting it based on the value, in ascending order
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True) #sroting it based on the value, in descending order
nestedDict = {
      "class1" : {
            "math": 92,
            "english": 80,
            "science": 84
      }
}

nestedDict["class1"]["math"] #how you access nested dictionaries
#Set: Used when you want to store a bunch of elements and be crtain that they're only present once. They are also immutable
#OOP: Stands for Object Oriented Programming and is a way of thinking about and implementing our code.
#It also means a flexible, powerful paradigm where classes represent and define concepts, while objects are instances of classes.
#The attributes are the characteristics associated to a type.
#The methods are the functions associated to a type.
anyobject = ""
dir(anyobject) #this here shows you all the methods associated with this type of data
help(anyobject) #this shows you how to use those methods represented in the dir method for the specific data type

class myClass: #this is how you declare a new class
      pass #it is a good habbit to start a class name with a capital letter
      anyString = ""
      def somefun(self):
            print(self.anyString) #here we put self.anyString to access the string in the class itself
#writing pass in a block just makes python ignore the error of nothing being there
#to access the class, you have to make an instance of it
myClassInstance = myClass()
myClassInstance.anyString #here you have accessessed the string inside the class
myClassInstance.anyString = "green apples" #here I changed the variable value of the instance, not the class itself
#Dot Notation: lets you access any of the abilities the object might have (called methods) or information it might store (called attributes)
#Different instances can have different values
myClassInstance.somefun() #this is how you call a function in a class

class anyClass:
      def __init__(self, name, age): #__init__ is a constructor here, it helps declare variables as soon as you declare an instance
            self.name = name
            self.age = age
anyClassInstance = anyClass( "albraa", 18) #this exaplains comment on line 13

class strClass:
      def __str__(self):
            return "hello" #the __str__ constructor allows us to return a string when someone tries to print the class instance itself

#dont forget to use help(something) to konw about more methods concerning the type
#Docstring: a brief text that explains what something does

def docstr():
      """hello"""#this is a docstring, when someone calls help(docstr) it will show up
      print("Hi everyone")

class Color:
      def __init__(self, color, hex):
            self.color = color
            self.hex = hex

#how to inheret a class
class Red(Color):
      pass

class Blue(Color):
      pass

#the classes Red and BLue both inheret the class Color
#you can make instances of those classes too and use methods just like you would use on normal classes

#modules: used to organize functions, classes, and other data together in a structured way
import random #random module
random.randint(1, 10) #this gives you a random number between 1 and 10

import datetime #datetime module
now = datetime.datetime.now() #this datetime.datetime.now() gives the date and time of today
now #outputs the date and time together
now.year #this shows which year it is
now.month #this shows which month it is

import time
time.sleep(10) #this makes the program wait/sleep 10 secs before doing something

#Event Class: contains the date when the event happened, the name of the machine where it happened, the user involved, and the event type.


#! file section
#File Descriptor: a token generated by the os, that allows programs to do more operations with the file
file = open(r"absolute path of a file") # opens a file to read only, an absolute path is a path like: C:\myfolder\mysubfolder \\ if the file is in the same directory, remove the "r" before the quotes
file.readline() #this outputs a single line from the file, if it is called again, it will read the next one
file.read() #this outputs everything in the file
file.close() #it is a good habbit to close files since it takes ram to keep them open and prevents other programs from using them

file_contents = file.readlines() #this stores every line in a list to access each one individually

for line in file: pass #this does something with every line, maybe print or anything you like

with open(r"C:\Users\ALBARAA.DESKTOP-87EJ24R\Programming\Tests Folder\myTxtFile.txt") as file: #using the "with" here, we don't have to worry about closing the file, it closes it after it does the tasks
      print(file.read().strip())
      lines = file.readlines() #this stores every line in a string in a list called "lines"

#use "with" if you are using the file for a small period, if you want to use it for the whole time, just keep it open

with open(r"C:\Users\ALBARAA.DESKTOP-87EJ24R\Programming\Tests Folder\myTxtFile.txt", "a") as file:
      pass
      file.writeline("my comment") #the writeline function is to write then go to the next line

# "r" in quotes is to only read
#* "w" means it will be write only but it will erase the previous data if you do that , never use this one please
# "a" means it will append the file, meaning you can write but it wont erase everything
# "r+" means read and write

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename() # this opens a file explorer for the user to choose a folder, then selects that folder in file_path

#! OS Section
#* Use "r" before the quotes for paths pretty please
import os
os.remove("my.txt") #this removes the file named "my.txt"
os.rename("name of the file with extension", "new name.txt") #renames the file
os.path.exists("my path or file name") #checks if the file is present
os.path.getsize("name of file / path") #checks for size
os.path.abspath("name of file / path") #outputs the absolute path of the file, can be used if you are using different systems

#! Execute a Command in The Terminal
os.system("the command here")

import datetime
timestamp = os.path.getmtime("any file")
datetime.datetime.fromtimestamp(timestamp) #prints the last time the file was modified in an understandable way :)

os.getcwd() #outputs which directory is selected rn
os.mkdir("new dir name") #makes a new directory in the current directory
os.chdir("folder name or its path") #changes to the following directory
os.chdir('..') #this will go back one driectory
os.rmdir("folder name / path") #removes the directory only if it is empty!!
os.listdir("directory name / path") # outputs all the files and directories in the directory
os.isdir("anything's name / path") # checks if it is a directory

for any in os.listdir("directory name / path"): #this checks for every thing in the directory
      os.path.join("directory name", any) # this outputs the path of "any" from current directory
      pass

#! CSV Files Section

#Parsing: analyzing a file's content to correctly structure the data
#CSV files: there are files, which apps like excel uses to store data, it stores data and separates it by commas

import csv #the module

f = open("any file.txt")
csv_f = csv.reader(f) #parsing the file with csv to be readable by the module

for row in csv_f: # the row here is a list, it has the values all in each row of the file, so you can treat it like a list :)
      name, phone, role = row #here the first colum of that row is stored in name, second in phone, third in role, this is how you unpack the row
      # for this to work, you have to have the same number of elements on both sides
      print(name) #this will print the first column of that row
      pass

#! Creating a New CSV File

myList = [["Name", "Age", "Phone"], ["Albraa", "18", "5370623850"], ["Hanan", "20", "None"]] #using this list, we will make a new csv file

with open("myCsvFile.csv", "w", newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Name", "Age", "Phone"]) #use with lists
      writer.writerow(["Albraa", "18", "5370623850"])
      writer.writerow(["Hanan", "20", "None"])
      writer.writerows(myList) #use for lists nested in other lists

#! Accessing The CSV File as a Dictionary

with open('myCsv.csv') as file:
      reader = csv.DictReader(file) #here the method is called DictReader
      for row in reader:
            print(row["name"]) #here the first row isnt considered, it is rather used as a key to access all the names!

#! Using a Dictioniary to Write a CSV File

MyDictList = [ #the list of dictionaries we are going to use to make a new csv file
      {
            "name": "Albraa",
            "age": "18",
            "phone": "5370623850"
      },
      {
            "name": "Hanan",
            "age": "20",
            "phone": "none"
      }
]

keys = ["name", "age", "phone"] #the first row

with open('myCsvFile.csv', 'w', newline='') as file:
      writer = csv.DictWriter(file, fieldnames = keys) #assigning the file and the first column
      writer.writeheader() #creates first line of the file by using the our fieldnames
      writer.writerows(myDictList) #writes the rows

#! Regular Expressions | Regex
#* They allow us to search a text for strings matching a specific pattern
#* Make sure to go the regular expressions text file to understand how to use them

import re

myText = "here, there, where, stare"

result = re.search(r"ere", myText) #here it searches for only one object
result = re.findall(r"ere", myText) #this outputs a list of every place that this pattern was mentioned
result = re.sub(r"ere", "new replacement", myText) #this subtitutes something for another
result = re.split(r"[,]", "Albraa,18,5370623850") #here split is for spliting the string into a list by using the comma as a splitter, the list will contain "Albraa", "18", and "5370623850"

result = re.search(r"ere", myText, re.IGNORECASE) #here the ignorecase makes it that it doesn't care if the pattern is lowercase or uppercase

#! Capturing the information with regex
#Capturing groups: protions of the pattern that are enclosed in parentheses
result = re.search(r"[[](\d*)[]]", "[12345") #* here the things in the paranthesis will be caught and can be used
result[0] #here it outputs the match only
result.group(1) #here it will output the first captured group if it exists
result.group(2) #here it will output the second captured thing if it exists

#! Managing Data and Processes
#* I/O streams: the basic mechanism for performing input and output operations in your programs
#* Standard input: STDIN
#* Standard output: STDOUT
#* Standard error: STDERR
#* Shell: a command-line interface used to interact with your operating system, it is also where the python programs get executed
#* Command-line arguments: parameters that are passed to a program when it's started
#* Exit status: the value returned by a program to the shell
import sys
os.environ.get("HOME", "") #accessing environment variables, if the variable doesnt have a value, it will print nothing, the "get" method works with dictionaries too

print(sys.argv) #this will output list of all arguments that are passed when executing the file
#*in linux when you execute this file, put parameters after it like this: ./myfile.py Albraa Alsakor 18 "argument in quotes because it has spaces"
#*in windows you can execute it like this: python myfile.py "argument, doesnt have to be in quotes unless it has spaces" "another argument"
#the parameters are separated by spaces :)

#! Running System Commands in Python
import subprocess
subprocess.run(["the command here"]) #the first quotations is for the commands, if you wanna pass things into it, put a comma then another quotations
subprocess.run(["some command"], capture_output=True) #here the capture_output will return the reply of the system
print(result.STDOUT) #this is where the capture_output stores the reply, make sure to pass the decode().split() to decode it in utf8
print(result.STDERR) #this is where the error is stored when using the capture_output
subprocess.run(['date']) #gives the date
result = subprocess.run(["some command"])
result.returncode #this outputs the exit status

#! Testing in Python
#* Software testing: the process of evaluating computer code to determine whether or not it does what you expect it to do
#* Tests can help make good code better
#* Unit tests: used to verify that small, isolated parts of a program are correct
#* Edge cases: inputs to our code that produce unexpected results found at the extreme ends of ranges of input the programs will work with
#* On the other hand, integration tests verify that the interactions between the different pieces
#*    of code in integrated environments are working the way we expect them to

from myfile import something #this here imports "something" if it is a variable, class, or function from "myfile"

import unittest #module for testing scripts

class TestSomething(unittest.TestCase):
      def test_basic(self):
            testcase = "something to test" #the input
            expected = "the expected output" #the output you expect out of the function
            self.assertEqual(some_function(testcase), expected) #running the test
      #? note: you can write another function, which will be considered as another test :)
      def test_another(self):
            self.assertRaises(ValueError, some_function, "value to pass", "second argument if there is one")
            #this here expects an error when giving this arguments, if there is no error, it will give a fail

unittest.main() #this is how you run the test

#* White-Box Testing: sometimes called clear-box or transparent testing relies on the
#*    test creator's knowledge of the software being tested to construct the test cases

#* Black-Box Testing: written with an awareness of what the program
#*    is supposed to do - its requirements or specifications - but not how it does it

try: #the try block tries executing the code in it
      pass
except: #the except block is run if the "try" block gives an error
      pass

raise Exception("text to output") #this outputs an exception to the user
raise TypeError("text to output") #this outputs a typeerror to the user
raise ValueError("text to output") #this outputs a valueerror to the user

assert {condition}, "text to output"
#this assertion is like an if statement, if the condition is true, it will continue with the code
#if not true, then it will output that text in an AssertionError

#! THREADS! PARALLEL PROCESSING!
#? Importig the module
#* notice that this module doesnt need downloading
import concurrent.futures

#? Any function
def my_function():
      print("This is a print from my function")

#? Using ThreadPoolExecutor to do the tasks in the background and with multiple threads, this makes this so fast
#* notice that here we used "with" so that when it is done, it shuts down the executor variable
with concurrent.futures.ThreadPoolExecutor() as executor:
      executor.submit(my_function, argument_here_if_needed) #* used if you have one argument to pass or run the function
      executor.map(my_function, list) #* used if you have a list of arguments to pass

#* when calling ThreadPoolExecutor(), in the brackets you can set the max workers, basically max cpu cores to use
#* like this: ThreadPoolExecutor(max_workers=5)
#* if it is left empty, then it will use as much as the number of cores the cpu has

#! Python debugging and troubleshooting
#? Memory Profiler: write the following in terminal
#* python3 -m memory profiler <name of the python file>

#? Debugging:
#* pdb3 <python file> <any parameters that the file expects>
#* in pdb now
#* continue #if you found no error yet