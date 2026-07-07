print("fourth")

print("fifth")

print("sixth")

#what are strings

my_str_1 = 'hello'

my_str_2 = 'world'

#some times you may need to check if a string contains one or more characters

#for that python provides the in operator, which returns a boolean that specifies whether the character ot characters exist in the string or not

#here is an example 

my_str = "hello world"

print('hello' in my_str)
print('hey' in my_str)
print('hi' in my_str)
print('e' in my_str)

print("f" in my_str)

#now lets look at how you can get the length of a string and work witht the individual characters in a string, a process called indexing.

#to gert thte length of a string you can use the build in len() function 

print(len(my_str))

#each character in a string has a position called an index the index is zero based meaning that the index of the first character of a string is 0


print(my_str[0])
print(my_str[6])


#negative indexing is also allowed, so youj can get the last character of any string

print(my_str[-1])
print(my_str[-2])

#strings are immutable data types in python

#this means that you can reassign a different string to a variable 

greetiug = 'hi'

greeting = 'hello'

print(greeting)