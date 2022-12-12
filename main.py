#Recursion: the repeated application of the same procedure to a smaller problem. Lets up tackle complex problems by reducing the problem to a simpler one.
#In programming, recursion is a way of doing a repetitive task by having a function call itself.
#Recursion in python can only happen 1000 times in each function when called.

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
print("Your name is {}, and your age is {}.".format(name, age)) # a method that replaces the first "{}" with the first argument in the format operation and so on.
print("Your lucky number is {number}, {name}.".format(name=name, number=number)) # a method for formatting the variables in the string.
print("Your total price is ${:.2f}".format(price) # a method for displaying the variable but with only two decimal places.

x = ["My", "name", "is", "Albraa"] # This is a how a list is made
"My" in x # This method checks if a certain string is inside a list
x[0] #How to output a certain string in a list with indexing
