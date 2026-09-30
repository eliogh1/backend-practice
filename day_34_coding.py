# so today we are going to work with tuples they are immutable data types and they have a few common methods that we can use to get more information about
#so lets do some problems with them to get used to useing them on a computer



#number 1; Student details: Create a tuple containing a student’s name, age, and grade. Print each item separately.

def students():
    
    student = ("Elio leon", 21, "not enrolled")
    
    print(student[0])
    print(student[1])
    print(student[2])
    
#number 2 Single-item tuple: Create a tuple containing only "apple". Use type() to check that it is a tuple.

def single_item_tuple():
    
    tuples = ("apple")
    
    print(type(tuples))
    
#number 3 Indexing: Print the first and last items:

def indexing():
    
    colors = ("red", "blue", "green", "yellow", "purple")
    
    print(colors[0])
    print(colors[-1])
    
#number 4 Slicing: Using the tuple above, get:
# The first three colors.
# The last two colors.
# The tuple in reverse order.

def slicing():
    
    colors = ("red", "blue", "green", "yellow", "purple")
    
    print(colors[0:3])
    print(colors[-2:])
    print(colors[-1::-1])
    


#number 5: Membership: Ask the user for a fruit and check whether it appears in:
#fruits = ("apple", "banana", "orange", "mango")

def membership():
    
    fruits = ("apple", "banana", "orange", "mango")
    
    name_fruit = input("what is the name of your favorite fruit?: ")
    
    if name_fruit in fruits:
        print("thats my favorite fruits as well!!!!!")
    
    else:
        print("i dont know that fruit")
        
# number 6: Looping: Print each item alongside its position:
# animals = ("cat", "dog", "rabbit", "bird")
# Example: 0 cat
        
def looping():
    
    animals = ("cat", "dog", "rabbit", "bird")

    for index, animal in enumerate(animals):
        print(index, animal)
        
#number 7: Count a number: Find how many times 3 appears:
#numbers = (3, 1, 3, 5, 3, 2, 1)

def count_a_number():
    
             
    numbers = (3, 1, 3, 5, 3, 2, 1,3)
    
    print(numbers.count(3))
    
#number 8: Count user input: Ask the user for a color and print how many times it appears:
# colors = ("red", "blue", "red", "green", "blue", "red")

def count_user_input():
    
    colors = ("red", "blue", "red", "green", "blue", "red")
    
    count_colors = input("what color from the list would you like me to count?: ")
    
    if count_colors in colors:
        
        print(colors.count(count_colors))
        


#number 9: Find a position: Use index() to find the position of "orange":
#fruits = ("apple", "banana", "orange", "mango")

def find_a_position():
    
    fruits = ("apple", "banana", "orange", "mango")
    
    print(fruits.index("apple"))
    
#number 10: First occurrence: Use index() to find the position of 7. Which occurrence does it return?
#numbers = (4, 7, 2, 7, 9, 7)

def first_occurance():
    
    
    numbers = (4, 7, 2, 7, 9, 7)
    
    print(numbers.index(7))
    


#number 11: Safe search: Ask the user for an animal. Print its index if it exists; otherwise, print "Animal not found".
# animals = ("cat", "dog", "rabbit", "bird")

def safe_search():
    
    animals = ("cat", "dog", "rabbit", "bird")
    
    favorite_bird = input("what is your favorite bird?: ")
    
    if favorite_bird in animals:
        print(animals.index(favorite_bird))
    
    else:
        print("animal not found")
        
# number 12: Search from a position: Use index(value, start) to find the next occurrence of "red" after index 0:
# colors = ("red", "blue", "green", "red", "yellow", "red")




        



    
    
    

    
    
    


    
