#what are sets amd how do they work

#sets are a build in data structure one of the core characteristics of sets is that they dont store duplicate values

# sets are mutable and unordered, which means that their elements are not stored in any specific order, so you cannot use indices or keys to access them

#they can only contain values of immutable data types like numbers, strings, and tuples

#to define a set you need to write its elements within curly braces and seperate them with commas

my_set = {1,2,3,4,5}

#one quirk of working with sets is that, if you ever need to define an empty set, you must use the set() function.

#if you just write empty curly braces like this{}

#python will automatically create a dictionary

set()
{}

#you can add an element to a set with the. add() method, and pass in the new element as arguement

my_set.add(6)

#in our example, the new set would be:

{1,2,3,4,5,6}

#if you try to add an element thta is already in the set, only one will be kept. in this case, we already have the number 5 in the set

my_set.add(5)

#to remove an element from the set, you have two options. you can either use the .remove()m method or the .discard() method, and pass in the element that you want to remove as arguement


#the remove() method will raise a keyerror if the element is not found, while the .discard() method will not:

my_set.remove(4)
my_set.discard(4)

#the clear() method removes all the elements from the set:

my_set.clear()

#python sets also have powerfull methods that perform common mathematical set operations

# the .issuvset() and the .issuperset() methods chech if a set is a subset or superset of another set, respectively

#The .issubset() and the .issuperset() methods check if a set is a subset or superset of another set, respectively.

#Here, we are checking if your_set is a subset of my_set, which is False because not all the elements of your_set are in my_set.

#We are also checking if my_set is a superset of your_set. This is also False because my_set does not have all the elements of your_set:


my_set = {1,2,3,4,5,6}
your_set = {2,3,4,6}

#The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common. In this case, that's False because my_set and your_set do have common elements – 2, 3, and 4:

print(my_set.isdisjoint(your_set))

#The union operator | returns a new set with all the elements from both sets:

print(my_set | your_set)

#The intersection operator & returns a new set with only the elements that the sets have in common:

print(my_set & your_set)

#The difference operator - returns a new set with the elements of the first set that are not in the other sets. In this example, the numbers 1 and 5 are in my_set but NOT in your_set:


print(my_set - your_set)

#the symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both

#in this case 1 and 5 are in my_set but not in your_set, so they are included

#and the number 6 is in your_set but not in my set, so its included as well

print(my_set ^ your_set)


#Each one of these operators also has its corresponding compound assignment operator if you add the equal sign next to it. These operators automatically assign the resulting set to the first set in the expression:

# |= , &= , -= , ^= 


#for example the -= operator finds the difference between the sets and updates the first set with that result:

my_set -= your_set

#after this, my_set will be updated to {1,5}

print(my_set)








