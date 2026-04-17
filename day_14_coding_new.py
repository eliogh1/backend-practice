# today im going to learn lambda functions and how they work

#throughout the previous lessons you have been used to defining functions by using the def keyword like this

def square(num):
    return num ** 2

print(square(4))

#but when it comes to working with high order functions like map() and filter() 

#you can use an anonymous inline function this is where lambda functions come in

# heres what the square() functions looks like when refactored into a lambda function

lambda num: num ** 2

# lambda functions are anonymous so this function no longer had the name square associated with it

# lambda functions are great when you need to use them in higher order functions like this

numbers = [1,2,3,4,5]

even_numbers = list(filter(lambda x: x %  2 == 0, numbers))
print(even_numbers)

#in this example we have a list of numbers and want to create a new list of even numbers. 

# so we pass in a lambda function as one of the arguements to the filter() functions to get a new list containing the numbers 2 and 4

# when working with lambda functions it is important to be aware of best practices

# for example it is not a good practice to assign a lambda function to a variable like this

square = lambda x: x ** 2
squared_numbers = list(map(square,numbers))
print(squared_numbers)

#this defeats the purpose of using anonymous functions in this case you should use regular functions like this

def squares(num):
    return num ** 2

squareds_numbers = list(map(squares, numbers))
print(squareds_numbers)

#also you should avoid creating lambda functions that are difficult to read or unneccessarily complicated like this

result = (lambda x: (x ** 2 + 2*x -1) if x > 0 else (x**3 - x + 4))(3)
print(result)

#while this functions runs fine and produces the correct result of 14 it is not easy to read or look at

#it would be better to create a seperate functions with an if else statement and then call that function

def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4
    
print(calculate_expression(3))
