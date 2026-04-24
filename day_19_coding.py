#so now that im done reviewing

#im going to start with the new lesson

#what are sets and how do they work

#first i need to understand what im working with

#sets are one of pythons built in data structures 

#one of the core characterisitcs of sets is that they dont store duplicate values

#sets are mutable and unordered, which means that their elements are not stored in any specific order, so you cannot use unduces ot keys to access them

#they can only contain values of immutable data types like numbers, strings and tuples

#to define a set you just need to write its elements within curly braces and seperate them with commas

my_set = {1,2,3,4,5,}

#if you ever need to define an empty set you must use the set() function

set() #set
{} #dictionary

#you can add an element to a set with the .add() method

my_set.add(6)

#the new set would be

{1,2,3,4,5,6,}

#if you try to add an element that is already in the set, only one will be kept

my_set.add(5)

#to remove an element from the set you can either use the .remove() method or the .discard() method, and pass in the element that you want to remove as arguement

my_set.remove(4)
my_set.discard(4)

#the .clear() method removes all the elemnts from the set

my_set.clear()


#python sets also have powerfull methods that perform common mathematical set operations

#the .issubset() and the .issuperset() methods check if a set is a subset or superset of another set, respectively

#here we are checking if your_set is a subset of my_set, which is false because not all the elements of your_set are in my_set

# We are also checking if my_set is a superset of your_set. This is also False because my_set does not have all the elements of your_set:

my_set = {1,2,3,4,5}
your_set = {2,3,4,6}

print(your_set.issubset(my_set))
print(my_set.issuperset(your_set))

#the .isdisjoint() method checks if two sets are disjoint, which means they dont have any elements in common.

print(my_set.isdisjoint(your_set))

#the union operator | returns a new set with all the elements from both sets:

my_set | your_set #{1,2,3,4,5,6}

#the intersection operator & returns a new set with only the elements that the sers have in common

my_set & your_set #{2,3,4}

#the difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both

my_set ^ your_set # {1,5,6}

#each one of these operators also has its corresponding compound assignment operator if you add the equal sign next to it

#  |= &= -= ^=

#For example, the -= operator finds the difference between the sets and updates the first set with that result: my_set -= your_set

print(my_set) # {1, 5}








#ok now its time for the actual coding

#number 1

set_1 = [1,2,2,3,4,4,5]

print(set(set_1))

#number 2 find unique characters in a string

word = "programming"

unique_letters = set(word)

print(f"{unique_letters}")


#number three check if two lists share any common elements

list_1 = [1,2,3,4,5,6,7,10,20]

list_2 = [2,3,5,7,9]

list_1_set = set(list_1)

list_2_set = set(list_2)

print(list_1_set & list_2_set) 

#number 4 count unique words in a sentence

sentence = "this is a test is only a test"

unique_sentence = set(sentence.split())

sentence_new = ""

for x in unique_sentence:
    if x not in sentence_new:
        sentence_new += x

print(sentence_new)

print(unique_sentence)

#number 5 find elemts that only apper once

list_3 = [1,2,2,3,4,4,5]

seen = set()
duplicates = set()

for x in list_3:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

result = [x for x in list_3 if x not in duplicates] 

print(result)














