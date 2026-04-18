#im going to study more from string i dont feel like i have enough understanding in strings

normal_string = "hello"

reverse_string = normal_string[::-1]

print(reverse_string)

# now im going to count vowels

number_of_vowels = 0
word = "programming"
for x in word.lower():
    if x in "aeiou":
        number_of_vowels += 1

print(number_of_vowels)
