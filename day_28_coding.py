#lets talk about string concatenation and string interpolation

#in python you can combine nmultiple strings together with the plus '+' operator


#this is called string concatenation


my_str_1 = 'hellop'
my_str_2 = 'world'

str_plus_str = my_str_1 + ' ' + my_str_2

print(str_plus_str)

#but note that this only works with strings if you try to concatenate a string with a number you'll get a typeerror



#this happens because python does not automatically convert other data types like intergers into string

#best way to practice is by actually doing not by writing things down

#ok lets do a bunch of mini projects 

# greeting generator

name = input("what is your name: ")

print(f'hello, {name}! welcome back')

#next is what the age will be next year

age = int(input('how old are you now?:'))

print(f'next year you will be {age + 1}')

#number 3 favorite things 

favorite_food = input("what is your favorite food?: ")
favorite_color = input("what is you favorite color?: ")
favorite_animal = input("what is you favorite animal?: ")

print(f'your favorite food is {favorite_food}, your favorite color is {favorite_color}, your favorite animal is {favorite_animal}')

#lets try a username generator

name_1 = input("what is your name again?: ")
last_name = input("what is you last name?: ")
date_of_birth = input("what year where you born?: ")

print(f'{name_1[0]}{last_name}{date_of_birth[2:]}')




#now we are going to do some numbers and mathematical operations 

num_1 = 25

num_2 = 10

sum_of_nums = num_1 + num_2

print(sum_of_nums)

difference_of_nums = num_1 - num_2

print(difference_of_nums)

product_of_nums = num_1 * num_2

print(product_of_nums)

division_of_nums = num_1 / num_2

print(difference_of_nums)

#area of a rectangle

length = int(input("what is the length of the rectangle?: "))

width = int(input("what is the width of the rectangle?: "))

area_rectangle = length * width

print(area_rectangle)

