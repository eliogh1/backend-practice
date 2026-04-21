# ok now im going to work on some mini projects

Toyota_car_dictionary = {
    'toyota_camry_$': 32000,
    'toyota_year': 2026,
    'toyota_max_speed': 130,
    'toyota_trim': 'le',
    'toyota_color': 'black'
    
    
}

Toyota_car_dictionary.update({'toyota_year': 2027})

print(Toyota_car_dictionary.keys())

print(Toyota_car_dictionary.values())


if 'toyota_camry_$' in Toyota_car_dictionary:
    print("the key is here")
else:
    print("the key is not here")

Toyota_car_dictionary.pop("toyota_camry_$", 32000)

year_of_toyota = Toyota_car_dictionary.get('toyota_year', [])
print(year_of_toyota)

three_friends_mine = {
    'elieser': 20,
    'jordan': 21,
    'luis': 19
}

for x in three_friends_mine.items():
    print(x)