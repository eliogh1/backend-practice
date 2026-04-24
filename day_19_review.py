#so first im going to review the projects i did yesterday and maybe a little more 

#ok so first lets start with number 1 word frequency counter

sentence = "lol word hi word come fast now oh lol hi nice wow word come lol"

sentence_dictionary = {}

for word in sentence.split():
    if word not in sentence_dictionary:
        sentence_dictionary[word] = 1
    else:
        sentence_dictionary[word] += 1


print(sentence_dictionary)

#now number 2 find max value

grades = {"math": 85, "science": 92, "english": 88}

subjects  = ""
highest_grade = 0

for subject, grade in grades.items():
    if grade > highest_grade:
        subjects = subject
        highest_grade = grade

print(subjects, highest_grade)


#ok now im going to number three filter dictionary

new_dictionary = {"mathew": 87,"jessica": 90, "mark": 95, "leon": 91, "felix": 75, "mike": 61}

highest_score = {}

for name, score in new_dictionary.items():
    if score > 90:
        highest_score[name] = score

print(highest_score)

#number 4 now i dont really remember how to do it but ill try (invert a dictionary)

regular_dictionary = {"a": 1, "b": 2}

invert_dictionary = {}


for letter, number in regular_dictionary.items():
    invert_dictionary[number] = letter

print(invert_dictionary)


#now number 5 count character frequency

words = "hello"

split_word = {}

for x in words:
    if x not in split_word:
        split_word[x] = 1
    else:
        split_word[x] += 1

print(split_word)

#ok done with that one now im going to do number 6

items = [("apple", "fruit"), ("carrot", "vegetable")]

grouping = {}

for item, category in items:
    if category not in grouping:
        grouping[category] = []

    grouping[category].append(item)

print(grouping)

#ok im done with number six now im doing number seven sum all values

prices = {"apple": 2, "banana": 3}

total = 0

for number in prices.values():
    total += number

print(total)

#ok now im doing number 8 nested dictionary traversal

students = {
    "leo": {"math": 90, "science": 85},
    "alex": {"math": 80, "science": 80}
}

for name, numbers in students.items():
    for subject, number in numbers.items():
        print(name,subject,number)

   




