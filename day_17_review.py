# what are some common techniques to loop over a dictionary

#you can loop over a dictionary if you need to access and process its key-value pairs 

#this is helpfull for updating their values or applying some logic to them

#lets say that we have a products dictionary that associates every product with its price

products = {
    'laptop': 990,
    'smartphone': 600,
    'tablet': 250,
    'headphones': 70,
}

#if we went to offer a 20 percent discount on all of our products, we can loop over all the key-value pairs and modify the prices

#the .values(), .keys(), and .items() methods are essential for these techniques we covered them briefly in a previous lesson

#you write for, the loop variable(price in this case), products.values() to get all the values of the products dictionary, a colon. and then the body of the loop,

#where you can apply logic to the values. in this case we are printing them

#the loop vairable will take each one of the values one per iteration 

for price in products.values():
    print(price)

for product in products.keys():
    print(product)

for product in products.items():
    print(product)

#if you want to store the keyu and the value in separate loop variables, you just need to define them and seperate the  with a comma

for product, price in products.items():
    print(product, price)

#now that you know more about this, we can go back to our initial example if we want to offer a 20 % discount we would multiply each price by 0.8
#and reassign it as the value of that product key

#we can also use round the result down if we want to work with intergers

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

#then if we print the dictionary we woul;d get these key-value pairs with the discounted prices

#and finally if you need to iterate over the key-value pairs while keeping track of a counter, you can call the enumerate() function.

#this counter essentially acts as a sort of index or count for that elementy within the loop

#the function returns an enumerate object, which assigns an interger to each key-value pair like a counter. 

#you can start the counter from any number but by defualt it starts from 0

for product in enumerate(products, 1):
    print(product)

#if yoy need to, you can assign these values to seperate loop variables(index and product)

#this is what you will commonly see and use when you work with enumerate():

for index, product in enumerate(products):
    print(index, product)

#if you need to iterate over the values, you can replace products by products.values():

for price in enumerate(products.values()):
    print(price)

#you can assign them to different loop as well:


for index, price in enumerate(products.values()):
    print(index, price)


#and with products.items(). you can get the entire key-value pair in addition to the index or counter

for index, product in enumerate(products.items(), 1):
    print(index, product)