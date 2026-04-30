#ok so taoday im going to review a little bit of strings and stuff from loops and conditionals

# number 5 remove spaces  

spaced_word = "h e l l o"

print(spaced_word.replace(" ", ""))

#now lets do the same thing with loops 

for x in spaced_word.split():
    if x == " ":
        x.replace(" ", '')
    print(x,end= "")


#ok now lets do number 6 capatilize each word no .title()

sentence = "hello world"

upper_sentaence = ""

for x in sentence.split():
    upper_sentaence += x.upper() + " "

print(upper_sentaence)


#now im going to refresh myself in booleans and condtioanals

#first is even or odd checker

for x in range(1, 100):
    if x % 2 == 0:
        print(x ,"even")
    else:
        print(x ,"odd")

#now for a password strength checker

password = input("Enter a passwrod:")


length_ok = len(password) >= 8
has_number = any(x.isdigit for x in password)
has_upper = any(x.isupper for x in password)

if length_ok and has_number and has_number:
    print("strong password")
else:
    print("weak password")

    #ok im done witht this for now 

#now im back and im going to review what i learned

#i went over classes and objects so for example 


class car:


    def __init__(self,model,year,mileage):
        self.model = model
        self.year = year
        self.mileage = mileage

    def add_mileage(self, mileage):
        self.mileage += mileage

    def display_info(self):
        print(f"all the car information like the model is {self.model} and like the year {self.year} and like the mileage{ self.mileage}")





car1 = car("toyota", 2026, 20200)

car1.add_mileage(10000)

car1.display_info()








        
        

   


