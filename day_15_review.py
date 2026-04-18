#good morning today we will review lambda functions and how they work

# you have been used to defining functions by using the def keyword like this

def square(num):
    return num ** 2

print(square(4))

# but when it comes to working with high order functions like map() and filter()

# you can use an anonymous inline function

# this is where lambda functions come in

# heres what the square() function looks like when refactored into a lambda function

lambda num: num ** 2

#as mentioned earlier, lambda functions are anonymous so this function no longer has the name sqaure associated with it

# lambda functions are great when you need to use them in higher order functions like this

numbers = [1,2,3,4,5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#in this example we have a list of numbers and want to create a new list of even numbers 

# so we pass in lambda function as one of the arguements to the filter() functions to get a new list containing the numbers 2 and 4

#when working with lambda functions it is important to be aware of best practices

# for example it is not good practice to assign a lambda function to a variable like this

squared = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers)

#this defeats the whole perpose of using anonymous functions 
#in this case you should use a regular function like this

def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers)

#also you should avoid creating lambda functions that are difficult to read or unnecessarily complicated like this

result = (lambda x: (x**2 + 2*x -1) if x > 0 else (x**3 - x + 4))(3)
print(result)


#while this function runs fine and produces the correct result of 14 it is not easy to read or look at

# in this case it would be better to create a seperate function with an if/else statemnet and then call that function

def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x -1
    else:
        return x**3 - x + 4
    
print(calculate_expression(3))

#now im going to do mini projects associated with lambda and see how it goes

#square list with map()

lis = [1, 2, 3, 4, 5]

power_of_lis = list(map(lambda x : x ** 2, lis))
print(power_of_lis)

# number two : flter even numbers

lis_1 = [3, 10, 15, 20, 25, 30]

filters_10 = list(filter(lambda x : x % 2 == 0 , lis_1))
print(filters_10)

#number 3 multiply all numbers by 3

lis_2 = [2, 4, 6]

multiply_3 = list(map(lambda x : x * 3, lis_2 ))
print(multiply_3)

#number 4 remove empty strings

remove_list = ["hello", "", "world", "", "python"]

remove_empty = list(filter(lambda x : x if x else None , remove_list))
print(remove_empty) 

# im going to try number 8 extract first letter of each word string munipulation

lis_3 = ["apple", "banana", "cherry"]

first_letter_extrac = list(map(lambda x : x[0], lis_3 ))
print(first_letter_extrac)

# ok i did enough for the lambda functions

# now im back with the list comprehension projects

# question number 6 get names longer then 5 letters

lis_4 = ['leo', 'andrew', 'micheal', 'and']
lis_4_etra = []


for x in lis_4:
    if len(x) > 5:
        lis_4_etra.append(x)

print(lis_4_etra)

#ok now to do list comprehension for the same problem

lis_comprehension = [n for n in lis_4 if len(n) > 5 ]
print(lis_comprehension)

#now to do functions this one will use a filter function

def length_str(x):
    return len(x) > 5

lengths_of_string = list(filter(length_str, lis_4))
print(lengths_of_string)

#a little extra i want to do the lambda version of it

len_of_string = list(filter(lambda x : len(x) > 5, lis_4))
print(len_of_string)



