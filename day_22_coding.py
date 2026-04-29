#Ok so im coding a little bit of strings to get back the basics of coding with them

#first is reverse a string

word = "hello"

reversed_word = word[::-1]

print(reversed_word)

#now to count vowels

word_vowels = "programming"

vowels = 0

for x in "aeiou":
    if x in word_vowels:
        vowels += 1

print(vowels)

#check palindrome is the next question

palindrome = "racecar"

palindrome_reversed = palindrome[::-1]

if palindrome == palindrome_reversed:
    print("this is a palidrome")

else:
    print("this is not palindrome")


#ok now to count characters

count_letters = {}

for x in word:
    if x not in count_letters:
        count_letters[x] = 1
    else:
        count_letters[x] += 1

print(count_letters)

#number 5 remove spaces

word_spaces = "h e l l o"

for x in word_spaces.replace(" ","" ):
    print(x, end="")

print(word_spaces.replace(' ', ""))

#ok now on to real logic level 2

#capatilize each word (no .title())

sentence = "hello world"

upper_case_sentence = ""

for x in sentence.split():
        upper_case_sentence += x.upper() + " "

print(upper_case_sentence.strip())


#now number 7 lets see if i can do it

#find the longest word

longest_word_sentence = 'i love programming'

longest_word = ""

for x in longest_word_sentence.split():
    if len(x) > len(longest_word):
        longest_word = x

print(longest_word)

#ok now lets replace vowels with *

words = "hello"

replace_vowels = ""

for x in words:
    if x in "aeiou":
       replace_vowels = words.replace("aeiou", "*")

print(replace_vowels)
        
