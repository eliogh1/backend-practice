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


import math




def greeting_generator():
    name = input("what is your name: ")

    print(f'hello, {name}! welcome back')

#next is what the age will be next year
def next_year_age():
    age = int(input('how old are you now?:'))

    print(f'next year you will be {age + 1}')

#number 3 favorite things 
def favorite_things():
    favorite_food = input("what is your favorite food?: ")
    favorite_color = input("what is you favorite color?: ")
    favorite_animal = input("what is you favorite animal?: ")

    print(f'your favorite food is {favorite_food}, your favorite color is {favorite_color}, your favorite animal is {favorite_animal}')

#lets try a username generator
def username_generator():
    name_1 = input("what is your name again?: ")
    last_name = input("what is you last name?: ")
    date_of_birth = input("what year where you born?: ")

    print(f'{name_1[0]}{last_name}{date_of_birth[2:]}')




#now we are going to do some numbers and mathematical operations 
def normal_calculator():
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
def area_calculator():
    length = int(input("what is the length of the rectangle?: "))

    width = int(input("what is the width of the rectangle?: "))

    area_rectangle = length * width

    print(area_rectangle)

#now lets do a perimeter calculator 

def perimeter_calculator():

    perimeter_length = int(input("what is the length of the perimeter?: "))

    perimeter_width = int(input("what is the width of the perimeter?: "))

    perimeter_calculator_1 = 2 * (perimeter_length + perimeter_width )

    print(perimeter_calculator_1)

def circle_calculator():
    
    radius = float(input("what is the radius of the circle?: "))
    
    pi = math.pi
    
    diameter = 2 * radius
    circumference = diameter * pi
    area =  pi * radius ** 2

    print(diameter)
    print(circumference)
    print(area)


#BMI calculator

def Bmi_calculator():
    weight_kg = float(input("what is your weight in kg?: "))
    height_meters = float(input("what is you height in meters?: "))

    BMI = weight_kg / (height_meters ** 2)

    print(BMI)


Bmi_calculator()





