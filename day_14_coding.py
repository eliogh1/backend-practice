#first im going to review the first three projects that i did to refresh the memory

#even number exractor

lists = [1,2,3,4,5,6,7,8,9,10]

def even_numbers(even):
    return even % 2 == 0

even_lists = list(filter(even_numbers, lists))

print(even_lists)

even_numberss = [num for num in lists if num % 2 == 0 ]

print(even_numberss)

#now for square all numbers

lists_2 = [1,2,3,4,5,6,7,8,9,10]

def squared_nums(power):
    return power ** 2

squared_numbers = list(map(squared_nums, lists_2))
print(squared_numbers)

#nexxt sum of all positive numbers

list_3 = [3, -1, 5, -2, 9]

positive_nums = sum([num for num in list_3 if num > 0])

print(positive_nums)

#ok so now one i havent done before

#remove empty strings

list_4 = ["hello", "", "world", "", "python"]

#def truthy(true):
#    return true == True

truth = list(filter(None, list_4))
print(truth)

#convert strings to intergers

list_5 = ["1", "2", "3"]

def interger(intergers):
    return int(intergers)

string_intergers = list(map(interger, list_5))
print(string_intergers)

# im going to do each project in three ways a normal for loop list comprehension and using map and filter


#even number extractor

lis_1 = [1,2,3,4,5,6,7,8]
lis_2 = [] 

for x in lis_1:
    if x % 2 == 0:
        lis_2.append(x)    
print(lis_2)

#now for the list comprehension version

lis_comprehension_1 = [n for n in lis_1 if n % 2 == 0]
print(lis_comprehension_1)

#now for the map or filter version

def even_lis(lis):
    return lis % 2 == 0

even_num = list(filter(even_lis, lis_1))
print(even_num)

#ok now to do the same thing but with numbers 2

lis_square_num = [1,2,3,4]
store_squared = []

for x in lis_square_num:
    store_squared.append(x ** 2)

print(store_squared)

#now to do it for comprehension

squared_comprehension = [n ** 2 for n in lis_square_num]

print(squared_comprehension)

#now to do it with map or filter function / map

def squared_map(squared):
    return squared ** 2

squared_result = list(map(squared_map,lis_square_num))
print(squared_result)

#now to do each for sum of positive numbers first for loop

sum_positive = [3, -1, 5, -2, 9]
total = 0

for x in sum_positive:
    if x > 0:
        total += x

print(total)

# now to do comprehension list

sum_comprehension = sum([n for n in sum_positive if n > 0])
print(sum_comprehension)

# now to do it in a map or filter function

def positve_sum(n):
    return n > 0

sum_filter = sum(list(filter(positve_sum,sum_positive)))

print(sum_filter)

#removing empty strings for loop

remove_strings = ["hello", "", "world", "", "python"]
remove_strings_1 =[]

for x in remove_strings:
    if x:
        remove_strings_1.append(x)

print(remove_strings_1)

#now to do the list comprehension

remove_strings_comprehension = [n for n in remove_strings if n]
print(remove_strings_comprehension)

#now to do it in a map() or filter() function

def truthy_list(x):
    return x != ""

truthy_list_1 = list(filter(truthy_list,remove_strings))
print(truthy_list_1)






