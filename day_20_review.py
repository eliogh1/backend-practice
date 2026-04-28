#ok so first im going to review what i learned yesterday by first looking at the curriculum and then doing the problems chat gpt gave me 

#to defince a set you just need to write its elements withim curly braces and seperate them with commas

my_set = {1,2,3,4,5,}

# one quirk of working with sets is that if you ever need to define an empty set you must use the set() funciton

set() #set

{} #dictionary

# you can add an element to a set with the . add() method, and pass the new element as arguement

my_set.add(6)

#if you try to add an element that os already in the set, only one will be kept

my_set.add(5)

#to remove an element from the set you have two options

#you can either use the .remove() method or the .discard() method, and pass in the element that you want to remove as arguement

#the .remove() method will raise a keyerror if the element is not found
  
#while the .discard() method will not  

my_set.remove(4)
my_set.discard(4)

#the .clear() method removes all the elements from the set

my_set.clear()

#python also have powerfull methods that perform common mathematical set operations

# the .issubset() and the .issuperset() methods check if a set is a subset or superset of another set

your_set = {2,3,4,6}

print(your_set.issubset(my_set))
print(my_set.issuperset(your_set))

#the .isdisjoint() methods checks if two sets are disjoint, which means they dont have any elements in common

print(my_set.isdisjoint(your_set))

#the union operator | returns a new set with all the elements from both sets

my_set | your_set # {1,2,3,4,5,6}

# the intersection operator & returns a new set with only the elements thath the sets have in common

my_set & your_set # {2,3,4}


#the difference operator - returns a new set with the elements of the first set thath are not in the other sets

my_set - your_set # {1,5}

#the symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set but not in both

my_set ^ your_set # {1,5,6}

#each one of these operators also has its corresponding compound assignment operator if you add the equal sign next to it

#these operators automatically assign the resulting set to the first set in the expression

# |= &= -= ^=

#for example, the -= operator finds the difference between the sets and updates the first set with that result

my_set -= your_set




#ok now for the questions again

# number 1 remove duplicates from a list


list_1 = [1,2,2,3,4,4,5]

list_1_set = set(list_1)

print(list_1_set)

#find unique characters in a string

word = "programming"

new_set = set(word)

print(new_set)

#number 3 check if two list share any common elements

list_2 = [1,2,3,4,5,6,7,8,9,10]
list_3 = [2,4,6,8,10]

list_2_set = set(list_2)
list_3_set = set(list_3)

common_elements = list_2_set & list_3_set
print(common_elements)