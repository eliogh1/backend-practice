#number 1 a bank account system

class bankaccount:
    


    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough money")
        else:
            self.balance -= amount
    
    def display_balance(self):
        print(f"{self.owner} has ${self.balance}")



acc1 = bankaccount("Elio", 100)

acc1.deposit(50)
acc1.withdraw(30)
acc1.withdraw(200)


acc1.display_balance()


#ok number 2 now

class car:
    

    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def drive(self, mileage):
        self.mileage += mileage

    def display_info(self):
        print(F"the name of the brand is {self.brand} and the model is {self.model} the mileage is also pretty low at {self.mileage} miles")

car1 = car("toyota", "camry", 100000)

car1.drive(10000)
car1.display_info()

#ok now im on number 3 student grade tracker

class Student:



    def __init__(self, name, grades):
        self.name = name
        self.grades = grades 

    
    def add_grade(self, score):
        self.grades.append(score)


    def average_grade(self):
        return sum(self.grades) / len(self.grades)




    def highest_grade(self):
        return max(self.grades)



s1 = Student("Elio", [85,71,31,90,70])

print(s1.average_grade())
print(s1.highest_grade())


              




