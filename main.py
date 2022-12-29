#Recursion: the repeated application of the same procedure to a smaller problem. Lets up tackle complex problems by reducing the problem to a simpler one.
#In programming, recursion is a way of doing a repetitive task by having a function call itself.
#Recursion in python can only happen 1000 times in each function when called.

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