class dog:
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name.upper()} says woof")
        
dog_1 = dog("thatcher", 5)

dog_2 = dog("karly", 6)

class student:
    
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        
    def average(self):
        if not self.grades:
            return None

        return sum(self.grades) / len(self.grades)        
        
        
class Rectangele:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.width * self.height
        
    
    
    def perimeter(self):
        return 2 * (self.height * self.width)
    
    
    def is_square(self):
        return self.height == self.width
    
    
    
    
    
    
