#redo practice questions one through 6

#woprd frequency counter

sentence = "lol how in world lol cant find how it in fart tit how in understand"

split_sentence = {}

for x in sentence.split():
    if x not in split_sentence:
        split_sentence[x] = 1
    else:
        split_sentence[x] += 1

print(split_sentence)


#number two

#find max value key

grades = {"math": 85, "science": 92, "english": 88}

name = ""
number = 0


for subject, grade in grades.items():
    if grade > number:
        name = subject
        number = grade

print(name, number)

#number 3 now

filter_dictionary = {"hitler": 21, "lando": 85, "felix": 99, "clark": 98}

new_dictionary =  {}

for name, final in filter_dictionary.items():
    if final > 90:
        new_dictionary[name] = final

print(new_dictionary)

#number 4 now invert a dictionary

regular_dictionary = {"a": 1, "b": 2}

invert_dictionary = {}

for key, x in regular_dictionary.items():
    invert_dictionary[x] = key

print(invert_dictionary)


#number 5 count character frequency

word = "hello"

word_split = {}

for x in word:
    if x not in word_split:
        word_split[x] = 1
    else:
        word_split[x] += 1

print(word_split)

#now for number 6 group itmes by category

items = [("apple", "fruit"), ("carrot", "vegetable")]

dictionary = {}

for edible, category  in items:
    if category not in dictionary:
        dictionary[category] = []
    dictionary[category].append(edible)

print(dictionary)

