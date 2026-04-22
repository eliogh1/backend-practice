#ok so im going to be coding what i learned in the review by coding some mini projects

# number one word frequency counter

sentence = "hello how are you im good how about you you feeling alright yes how about you im feeling fine"

words = sentence.split()



dictionary = {}

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(dictionary)

#second question is find max value

grades = {'math': 85, 'science': 92, "english": 88}

max_score = 0
max_subject = ''

for subject, score in grades.items():
    if score > max_score:
        max_score = score
        max_subject = subject

    print(max_subject, max_score)   
        

