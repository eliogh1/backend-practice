#ok lets just get straight into coding first thing first is im going to do a coding pyramid

def number_pyramid():
    
    number = int(input("enter a number: "))
    
    
    for x in range(1, number + 1):
        for y in range(1 , x + 1):
            print(y ,end="")
        print()
        
     



def reverse_number_pyramid():
    
    number = int(input("enter a number "))
    
    for x in range(number, 0, -1):
        for y in range(1, x +1):
            print(y, end="")
        print()
    


def multiplication_table():
    
    num = int(input("enter a number: "))
    
    for x in range (1, 11):
        print(num , "x", x,"=", x*num)
        
def count_vowels():
    
    word = input("tell me a word you like?: ")
    
    count = 0
    
    for x in word.lower():
        if x in "aeiou":
            count += 1
            
    print(f"vowels:{count}")
    
def count_lower_Case_and_upper_case():
    
    
    word = input("give me a word: ")
    
    uppercase = 0
    lowercase = 0 
    
    
    for x in word:
        if x.islower():
            lowercase += 1
        elif x.isupper:
            uppercase += 1
    print("uppercase", uppercase)
    print("lowercase", lowercase)
count_lower_Case_and_upper_case()

