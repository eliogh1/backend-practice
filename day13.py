#ok im going to review what i lerned yesterday and then ill learn something new

for row in range(1, 11):
    for col in range(1,11):
        print(row * col, end= " ")
    print()

#this is the second thing that was taught to me now i more or less understand it

for row in range(1, 11):
    for col in range(1, row +1):
        print(col, end= " ")
    print()

# this onme is the evnen and odd counter

even_counter = 0
odd_counter = 0


for x in range(1, 101):
    if x % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print(even_counter)
print(odd_counter)

# now to a classic fizzbuzz 

for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        print(x)
        print("fizzbuzz")
    elif x % 3 == 0:
        print(x)
        print('fizz')
    elif x % 5 == 0:
        print(x)
        print("buzz")
    

# ok now im reviewing what are the enumerate and zip functions and how do they work

languages = ["spanish", 'english', 'russian', 'chinese']

for language in languages:
    print(language)

# but what if you needed to keep track of the index for each element well, one option is to create an index variable and increment it

index = 0

for language in languages:
    print(f'index {index} and language {language}')
    index += 1

#while that works an easier way to do that is by using the enumerate() function
#the enumerate function keeps track of the index for an iterable and returns an enumerate object

#if we pass the languages list to the enumerate() function and convert its returned value into a list with the list() function, it looks like this

print(list(enumerate(languages)))

#each entry in the enumerate object(now a list) is a tuple containing a count,
# followed by a value from the iterable passed to the enumerate() function

#now lets refactor the example from earlier to use the enumerate() function

for index, language in enumerate(languages):
    print(f"index {index} and language {language}")

#we unpack the count and value for each tuple in the enumerate object into variables named index and language, respectively.

#finally, both those variables are used in a f-string thats printed to the console in each iteration of the loop

#this removes the need for manually creating and updating an index variable

# the enumerate() function also accepts an optional start arguement that specifies the starting value for the count. if the arguement is omitted, then the count will begin at 0

# an example

for index, language in enumerate(languages, 1):
    print(f'index {index} and language {language}')

#so far weve only been iterating over one list. but what if you need to iterate over multiple iterables in parallel

# well you can use the zip() function for that, which combines lists into pairs of elementss and returns an iterator of tuples

#if we pass a list of developers and ids to the zip() function and convert its returned value into a list with the list() function

developers = ['naomi', 'dario', 'jessica', 'tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))

#and heres an example of using the zip() function with a for loop to iterate over developers and ids:

for name, id in zip(developers, ids):
    print(f'name {name}')
    print(f'id {id}')

#in this example, zip() combines the twp lists into pairs of elements and returns an iterator of tuples. the for loop then unpacks each tuple into name and id. finally, for each print statment, we are printing each name 
#and id from the ids and developers lists respectively. here is what the result looks like in the console
