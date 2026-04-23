#im going to continue with the mini coding projects

#number 3 filter a dictionary

grades = {"math": 85, "science": 92, "english": 88}

subject_90 = ""
grade_90 = 0

#right buyt still wrong not that efficent

for subjects ,grade in grades.items():
    if grade > 90:
        subject_90 = subjects
        grade_90 = grade
        print(subject_90, grade_90)


#this is the correct way to do it 

filtered = {}

for subject, grade in grades.items():
    if grade > 90:
        filtered[subject] = grade

print(filtered)

#ok so now im going to invert a dictionary

regular_dictionary = {"a": 1, "b": 1}

invert_dictionary = {}

for k, v in regular_dictionary.items():
    if v not in invert_dictionary:
        invert_dictionary[v] = []
    invert_dictionary[v].append(k)
print(invert_dictionary)

#number 5 now im going to count character frequency


word = "hello"


dictionary_word = {}

for letter in word:
    if letter in dictionary_word:
        dictionary_word[letter] += 1
    else:
        dictionary_word[letter] = 1

print(dictionary_word)

#number 6 group items by category

items = [("apple", "fruit"), ("carrot", "vegetable")]

grouped_list = {}

for item, category in items:
    if item not in grouped_list:
        grouped_list[category] = []
    grouped_list[category].append(item)
    



print(grouped_list)

#important pattern

#if key not in dict:
#   dict[key] = []
# dict[key.append(value)

#number 7 now sum all values

prices = {"apple": 2, "banana": 3}

total_price = 0

for price in prices.values():
    total_price += price

print(total_price)
    


#im going to do some old problems to see if i learned it fr

#number one again word frequency counter

sentence = "apple banana apple orange banana apple"

split_sentence = sentence.split()

sentence_dictionary = {}

for word in split_sentence:
    if word not in sentence_dictionary:
        sentence_dictionary[word] = 1
    else:
        sentence_dictionary[word] += 1

print(sentence_dictionary)







salaries = {
    "john": 55000,
    "emma": 72000,
    "alex": 68000
}

max_salary = 0
top_person = ""

for name, salary in salaries.items():
    if salary > max_salary:
    
        top_person = name
        max_salary = salary


print(top_person, max_salary)



products = {
    "laptop": 1200,
    "phone": 800,
    "tablet": 600,
    "monitor": 300
}

max_price = 0
most_expensive = ""

for product, price in products.items():
    if price > max_price:
        max_price = price
        most_expensive = product

print(most_expensive, max_price)

#ok im done practicing number 2 now im going to practice number 3

scores = {
    "leo": 78,
    "emma": 92,
    "alex": 65,
    "sophia": 88,
}


highest_score = {}

for name , score in scores.items():
    if score > 80:
        highest_score[name] = score

print(highest_score)