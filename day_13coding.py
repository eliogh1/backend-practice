#the new concept im learing is what are list comprehensions and what are some usefull functions to work with lists?

#for the past few lessons you have been getting comfortable working with loops like this

even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

#this example creates a new empty list even_numbers and loops through a squence of numbers between 0 and 20 

#inside the loop theres a condition that checks if the current number is even if the condition is true the the current num is appened at the end of the even_numbers list

#while this code works there is a more concise way to write this that uses list comprehension instead list comprehension allows tou to create a new list in a single line by combining a loop
#and condition directly within sqaure brackets.

even_number = [num for num in range(21) if num % 2 == 0]
print(even_number)

#in this refactored example, the even numbers list is created using a single line of code

#lets take a look at another example so we can better understand how list comprehension works:

numbers = [1, 2, 3, 4, 5]

result = [(num, 'even') if num % 2 == 0 else (num, "odd") for num in numbers]
print(result)

#in this example we have a list of numbers and want to create a new list of tuples indicating which numbers are even or odd

# in the first part of the list comprehension we ise an id statement to check if the number is evenly divisible by 2 
#if so then the result is a tuple of that number followed by the word even 
#otherwise the result is a tuple with the number followed by the word odd

#another way to create a list starting from an existing iterable is the filter() function 

#here is an example of creating a new list of just words longer then four characters

words = ["tree", "sky", "mountain", "river", "cloud", "sun"]

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)

# the filter() function is used to select elements from an iterable that meets a specific condition.

#the filter() function accepts a function and an iterable for its arguements.

#in this example, we are passing in an is_long_word function into the filter() function to check if the current word count is greater then 4

# all words that have a character count greater than 4 are added into a new list and assigned to the long_words variable

#aside from the filter() function, there are a few more functions that are helpful when working with lists. another function to be aware of is the map()

# which takes an iterable and applies a function to each of its elements. here is an example of using the map() function to convert a list of temperatures from celsius to fahrenheit

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return(temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)

#just like the filter function() map () accepts a function and an iterable for its arguements

#the to_fahrenheit function takes a temperature and converts it from celcius to fahrenheit

#the last function we will look at is the sum() function

# this function is used to get the sum from an iterabkle like a list ot tuple.

#here is an example of using the sum() function:

list_number = [5, 10, 15, 20]
total = sum(list_number)
print(total)

#you can also pass in an optional start arguement which sets the intial value for the summation

#an example

total_partial  = sum(list_number, 10)
print(total_partial)