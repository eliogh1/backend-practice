


def password_accepter():
    
    password = input("please type your password?: ")
    
    
    if len(password) >= 8:
        print("password accepted")
    
    else:
        print("password not accepted")
        
def even_or_odd():
    
    number = int(input("please enter a number?: "))
    
    if number % 2 == 0:
        print("that is an even number")
     
    else:
        print("that number is odd")
        
def temperture_advisor():
    
    temperture = int(input("what is the temperture outside?: "))
    
    if temperture >= 75:
        print("its probably best to put on a t-shirt")
    
    else:
        print("its probably best to but on a hoodie or jacket")
        
def letter_grade_calculator():
    
    grade_percentage = int(input("what percentage did the kid get?: "))
    
    if grade_percentage >= 90:
        print("congradulation you got an A !!")
        
    elif grade_percentage <= 89 and grade_percentage >= 80:
        print("congradulation you got an B !!")
        
    elif grade_percentage <= 79 and grade_percentage >= 70:
        print("good job you got an C ")
    
    elif grade_percentage <= 69 and grade_percentage >= 60:
        print("Better luck next time you got a D !!")
        
    else:
        print("Better luck next time you got a f !!")
        


#ok so im going to build a number pattern generator

def number_pattern(n):
    
    if not isinstance(n, int):
        return " argument needs to be an integer"
    
    if n < 1:
        return "arguement needs to be a positive number"
    
    result = ""
    
    for x in range(1, n + 1):
        result += str(x)
        
        if x != n:
            result += " "
    
    return result

print(number_pattern("lol"))        
    
    