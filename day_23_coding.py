#so now im going to learn classes and objects and im going to review modules after 

#im going to do mini practice projects for both

#how do classes work and how do they differ from objects

#in python classes and objects work hand in hand to orginize and manage data you build a class to define shared behavior, then create objects that use those behaviors

#in other words, a class is like a blueprint or template you ise to create objects with

#to create a class, you use the class keyword followed by the name of the class and a colon

#then within the class, you can add anninitializer along with any attributes and methods

#attributes are like variables within a class, and are used to store data

#methods are functions defined within a class, and are the actions created with a class can perform

#basic syntax

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! {self.age} years old!")

#with this dog class, you can create an object. here the basic syntax for creating objects from a class:

# object_1 = classname(attribute_1, attriubute_2)
 
# object_2 = classname(attribute_1, attriubute_2)

#you can also call any of the methods defined in the class from each object

# object_1.method_name()
# object_2.method_name()

dog_1 = dog("Jack", 3)
dog_2 = dog("thacher", 5)

dog_1.bark()
dog_2.bark()

#as you can see we create two dog objects using the dog class. when initializing dog_1, the string jack and the number 3 are passed, which sets the name and age attribute for that instance

#and dog_2 is initialized with the string thatcher and number 5 as its name and age

#then when you call the .bark() method on dog_1 and dog_2, you can see how both out outs differ and ise the unique name and age attributes you passed in when creating each object

#ok now with the next lesson 

#what are methods and attributes, and how do they work?

#in the last lesseon you learned about classes and how they act as blueprints for creating objects

#here we will dive deeper into attributes and methods

#attributes are variables that belong to an object, so they hold data

#there are two kinds of attributes: instance attributes and class attributes

#instance attributes are unique to each onbject created from a class, and you usually use them with the __init__ method

#class attributes, on the other hand, belong to the class itself and are shared by all instances of that class

#to access an attribute, you use dot notation

#here are examples of both instance and class attributes, and how to access them from objects

class dogs:
    species = 'french bulldog' # class attribute

    def __init__(self,name):
        self.name = name #instance attribute

print(dogs.species)

dog1 = dogs("jack")
print(dog1.name)
print(dog1.species)


dog2 = dogs("tom")

print(dog2.name)
print(dog2.species)

# note that you can access class attributes directly from the class itself, but you need to create an object and pass its data first before you can access instance attributes

#cars are another good example, since cars have a model and color:

class car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

car_1 = car("red", "bmw m4")
car_2 = car("yellow", "ferrari spider")

print(car_1.model)
print(car_2.model)

print(car_1.color)
print(car_2.color)


