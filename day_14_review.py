#ok so lets start by reviewing some of what we learned yesterday

languages = ["spanish", 'English', "russian", "chinese"]

for language in languages:
    print(language)

#that was an example of using a for loop to print each language from the languages list to the console:

#but what if you wanted to keep track of the index for each element 

#well one option is to create an index variable and increment it by 1 for each iteration of the loop

index = 0 

for language in languages:
    print(f'index {index} and languages {language}')
    index += 1

#while that works an easier way to do that is by using the enumerate() function the enumerate function keeps track of the index

# for an iterable and returns an enumerate object

#if we pass the languages list to the enumerate() function and convert its returned value into a list with the list() function, it looks like this

print(list(enumerate(languages)))

#each entry in the enumerate object(now a list) is a tuple containing a count, followed by a value from the iterable passed to the enumerate() funciton

#now lets refactor the example from earlier to use the enumerate() function

for index, language in enumerate(languages):
    print(f'index {index} and languages {language}')

#well i just did an opss im reviewing what i learned two days ago now lets review what i learned yesteraday

even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers) 

#this example creates a new empty list called even_numbers and loops through a sequence of numbers between 0 and 20

# inside the loop there is a  condition that checks if the current number has a remainder of 0 when divided by 2 this is used to determime if the number

#is even, if the condition is True then the current num is appended at the end of the even_numbers list

#finally we print the even_numbers list to the console

# list comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets

#this makes the code shorter and often easier to read

# here is a refactored example from earlier using square brackets

even_number = [num for num in range(21) if num % 2 == 0]
print(even_number)

# lets take a look at another example se we can better understand how list comprehension works

numbers = [1, 2, 3, 4, 5]
result = [(num, 'even') if num % 2 == 0 else (num, 'odd') for num in numbers]
print(result)

#in this example we have a list of numbers and want to create a new list of tuples indicating which numbers are even or odd

#in the first part of the list comprehension we ise an if statement to check if the number is evenly divisible by 2

# if so the the result is a tuple of that number followed by the word even 

# otherwise the result is tuple with the number followed by the word odd

#another way to create a list starting from an existing iterable is the filer() function

# here is an example of creating a new list of just words longer than four characters

words = ['tree', 'world', 'life', 'range', 'have', 'locomotive', 'flame', 'motorcase', 'popcorn']

def is_long_word(word):
    return len(word) > 4

list_words = list(filter(is_long_word, words))
print(list_words)


#the filter function is used to select elementsfrom an iterable that meets a specific condition

# the filter function accepts a function and an iterable for its arguements

#in this example we are passing in an "is_long_word" function into the filter() function to check if the current word count is greater than 4

# all words that have a character count greater than 4 are added into a new list and assigned to the long_words variable

#aside from the filter function there are a few more functions that are helpful when working with list

# another function to be aware og is the map() function

#which takes an iterable and applies a function to each of its elements

#here is an example of using the map() functionn to convert a list of temperatures from celsius to fahrenheit

celsius = [0, 10, 20, 30, 40, 50]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)
