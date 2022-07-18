#!/usr/bin/env python3

import random

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")

del alien_0['speed']
print(alien_0)

favorite_languages = {
        'arek': 'python',
        'kojo': 'scretch',
        'kama': 'different',
        'tom': 'python',
        }
language = favorite_languages['kojo'].title()
print(f"Kojo favorite language is {language}.")
language = favorite_languages.get('fiolka', "ERROR - this position in dictionaries doesn't exist")
print(f"Fiola favorite language is {language}.")

# --- Looping ---
for key, value in favorite_languages.items():
    print(f"{key} -> {value}")

for kind in favorite_languages.items():
    print('{} ---- {}'.format(kind[0], kind[1]))

user_0 = {
        'username': 'President',
        'fname': 'Joe',
        'lname': 'Biden'
        }

print(user_0)

for i in range(len(user_0)):
    print(i)

friends = ['kojo', 'kama']

for key in favorite_languages:
    if key in friends:
        print(f"Hello {key} I see that your favorite language is {favorite_languages[key]}")
    else:
        print(key)

name = 'john'
if name not in favorite_languages:
    print(f"\n{name.title()} please join to our poll\n")
else:
    print("\nThis is joke :-)\n")

# --- Sorted ---
for name in sorted(favorite_languages.keys()):
    print(f"{name} thank you for taking the poll.")

# --- Repeats duplicate ---
print("\n")
for lang in favorite_languages.values():
    print(lang)

# --- Not repeats ---
print("\n")
for lang in set(favorite_languages.values()):
    print(lang)

# --- Nesting ---

alien_0 = {'color': 'green', 'poin': 5}
alien_1 = {'color': 'red', 'poin': 10}
alien_2 = {'color': 'purple', 'poin': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# -> generate aliens
aliens = []     # make an empty list for storing aliens
fleet = 10
# Make fleet aliens
for alien_iteration in range(fleet):
    a_color = random.choice(['red', 'black', 'white', 'green', 'purple'])
    a_point = random.randrange(1, 100)
    a_speed = random.choice(['slow', 'medium', 'fast'])
    new_alien = {'color': a_color, 'point': a_point, 'speed': a_speed}
    aliens.append(new_alien)
# show the first 5 aliens in loop
for alien in aliens[:5]:
    print(alien)
# show how many aliens have been created
print(f"You have: {len(aliens)} aliens")

# --- List in Dictionaries ---

pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese', 'salami']
        }
print(f"\nYou ordered a {pizza['crust']}-crust pizza "
        "with the following toppings: ")
for topping in pizza['toppings']:
    print("\t", topping)

# Next example
favorite_languages = {
        'arek': ['python', 'c++', 'ruby'],
        'kojo': ['scretch', 'python'],
        'kama': ['basic'],
        'tom':  ['python', 'c#', 'java', 'CSS']
        }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()} favorite languages are:")
    for language in languages:
        print(f"\t{language}")

# --- Dictionary in Dictionary ---
print("\n")
user = {
        'nook17': {
            'fname': 'arkadiusz',
            'lname': 'demko',
            'locate': 'warszawa',
            },
        'kojo': {
            'fname': 'konrad',
            'lname': 'demko',
            'locate': 'mragowo',
            },
        }
for user_name, user_info in user.items():
    print(f"User Name: {user_name.title()}")
    full_name = f"{user_info['fname']} {user_info['lname']}"
    location = user_info['locate']
    print(f"\tName: {full_name.title()}\n\tLocation: {location.title()}\n")


