#today is less of a review and more like learing something new so basically no review

# what are dictionaires, and how do they work

#in python, dictionaries are built-in data structures that store collections of key value pairs
#they work veryy similarly to real dictionaries, where you search for a word to find its corresponding meaning

#with python dictionaries, you use a key to find its corresponding value

#you should use dictionaries when you need to associate values to unique keys.

#this is helpfull when you need to find a value fast based on the key and when you need to represent structured data

#this is the general syntax

dictionary = {
    'key1': 'value1',
    'key2': 'value2'

}

#first we find the variable that holds the dictionary

# you dont necessarily need to assign the dictionary to a variable

#but its very common to do this to keep it in memory and use it for later in the code

#then thats followed by curly braces, which are somethimes called curly brackets and within the curly braces there are key_value pairs

#each key is associated with a value so you can use the key to access that value

#each key is accociated with a value, so you can use the key to access that value

#after each value, except the last one there a comma to seperate the different key-value pairts

#keys must be umique in the dictionary, and they must be an immutable data type. however the value can be repeated and they can be of any data type

#here we have an example of dictionry that stores inforamtion about a margherita pizza recipe

pizza = {
    'name': 'margherita pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']

}

#the dicitonary is assigned to the pizza variabele. it has four key-value pairs:
# name,price,calories_per_slice, and toppings

#another alternative would be using the dict() constructor, which builds the dictionary from squence of key-value pairs.

#this would be the equivalent syntax for our pizza example. we pass a list of tuples as arguements to the dict() constructor

#these tuples contain the keys as athe first element and the value as the second element.

pizza = dict([('name', 'margherita pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozarella', 'basil'])])

#to access the value of a key-valuepair, you can use this syntax, known as bracket notation. its name of the variable that holds the dictionary, followed
#by square brackets, and the key you want to access within the square brackets

dictionary['key1']

#in our pizza example if you want to access the value of name, you would write the name of the variable, pizza, followed by square brackets and the key, name, within quotes

pizza['name']