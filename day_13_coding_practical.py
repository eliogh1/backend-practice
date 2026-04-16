#now im doing a little bit of a practical to test my skill on functions i just learned


#even number extractor 

#the goal is to filter only even numbers from the list

#input [1,2,3,4,5,6,7,8,]

#output


list_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

even_numbers = [num for num in list_numbers if num % 2 == 0]
print(even_numbers)

#now im going to do the same thing but using only the filter() function

def even_numberss(nums):
    return nums % 2 == 0

even_number = list(filter(even_numberss, list_numbers))
print(even_number)


lists = [1,2,3,4]

def squared_lists(nums):
    return nums ** 2

squared_list = list(map(squared_lists, lists))

print(squared_list)


# now a little harder

#sum of positive numbers

neg_pos_list = [3,-1,5,-2,9]

positives = sum([n for n in neg_pos_list if n > 0 ])

print(positives)


    
        
