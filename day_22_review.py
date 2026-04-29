#today im going back ito strings to fill in some gaps because i dont feel to comforatble yet with them

#first lesson again is what are strings and what is string immutablility

#both single quote and double quoteation marks are treated the same in python

my_str = 'hello'

my_str_1 = "world"

#if you need a multi_line string, you can use triple double qoutes or single qoutes

my_str_2 = """Mulitline
string"""

my_str_3 = '''another
multiline
string'''

#use the opposite kind of qoutes that is if your string contains single qoutes, use double qoutes to wrap the string and vice versa

msg = "it's a sunny day"
qoute = 'she said, "hello world!'

#escape the single or double qoutation mark in the string with a backslash (\)

#with this method you can either use single or double qoutation marks to wrap the string itself

msgs = 'it\'s a sunny day'

qoutes = "she said, \"hello!"

#you may need to check if a string contains one or more characters

#python provides the in operator, which returns a boolean that specifies whether the character or characters exist in the string or not


my_str_4 = "hello world"

print("hello" in my_str_4)
print("hey" in my_str_4)
print("hi" in my_str_4)
print("e" in my_str_4)
print("f" in my_str_4)

#to get the length of a string, you can use the bulit in len() function

print(len(my_str_4))

#each string has a position called an index this index is zero based meaning that the index of the first character of a string is 0

#to access a character by its index you use square brackets([])

#with the index of the character you want to access inside

print(my_str_4[0])
print(my_str_4[6])

#negative indexing is also allowed, so you can get the last character of any string with -1, the second-to-last character with -2 and so on

print(my_str_4[-1])
print(my_str_4[-7])

#now some what are string concatenation and string interpolation?

# you can combine multiple strings together with the (+) operator this is called string concatenation

word = "hello"
word_2 = "world"

word_plus_word = word + " " + word_2

print(word_plus_word)

#if you try to concatrnate a string with a number, youll get a typeerror

name = 'john doe'
age = 23

name_and_age = name + "" + str(age)
print(name_and_age)

# to fix that you can convert the number into a string with the built in str() function, which returns the string representation of the given object without modifing the original object

name_and_str = name + str(age)

print(name_and_str)


#you can also use the augmented assignment operator for concatenation this is represented by a plus and equals sign (+=) and perforn both concatenation and assignment in one step


#f-strings start with f(either lowercase or uppercase) before the qoutes, and allow you to embef variables or expressions inside replacement fields indicated by curly braces{}

f_string = f"my name is {name} and i am {age} years old"
print(f_string)

num1 = 5 
num2 = 10

print(f'the sum of {num1} and {num2} is {num1 + num2} ')