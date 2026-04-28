#what is the python standard library and how do you impory a module 

#in software development a library is like a tool for developers 

#instead of having to impleament every single part of code youself from scratch a library gives you pre-wrtiiten code

#some examples of popular built in modules are math, random, re(short for regular expressions), and date and time

#the math module has helpfull functions for performing more complex mathematical operations

#the random module is used for working woth regular expressions


#you use an import statment 
#these statements are generally written at the top if the file. also you can customizr them based on your needs

#first you use the import statment, followed by the name of the module

import math 

#then  if you need to call a function from that module in opu python script, you would use dot notaion, with the name of the module followed by th name of the function

math.sqrt(36)

#this is the most basic versionm of an import statement, but there are other alternatives

#if you need to import the module with a different name (also known as an "alias")

#you can use the syntax, with "as" followed by the alias at the end of the import statement

# import random as ran

#this is often used to shorten long module names, or to avoid naming conflicts

# import math as m

#then you can access the elements of the module using the alias

math.sqrt(366)

#but sometimes you dont need to import everything from the module

#perhaps you only need one or two specific functions or classes

#now the import statmenent starts with from, followed by the name of the module, and then the import keytword followed by the name of the elements that you want to import

# from module_name import name1, name2


#then you can use these names without the module prefiux in you python script

#if you want to assign to these names, you can do that by using the as keyword after each followed by the alias you want to use:

# from module_name import name1 as alias1, name2 as alias2

#lets say that you only want to import the radians, sine and cosine functions from the math module, you would write

# from math import radians, sin, cos

#to find the sine and cosine of a specific angle intially expressed in degrees, we can call the redians funciotn to convert it to radiansm and then call the sine and cosine functions, passing the angle in radians:

from math import radians, sin, cos

angle_degress = 40
angle_randians = radians(angle_degress)

sine_value = sin(angle_randians)
cos_value = cos(angle_randians)

print(sine_value)
print(cos_value)

