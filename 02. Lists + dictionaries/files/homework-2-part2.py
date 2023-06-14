# Marco Dalla Stella
# 2023-06-07
# Homoework 2, Part 2

# #PART TWO: Lists

# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ['Italy', 'Mozambique', 'Ecuador', 'Mexico', 'Spain', 'United States', 'Peru']

# 2) Using a for loop, print each element of the list
for country in countries:
    print(country)

# 3) Sort the list permanently.
countries.sort()

#4) Display the first element of the list.

print(countries[0])

#5) Display the second-to-last element of the list.
print(countries[1:])

#6) Delete one of the countries from the list using its name.
countries.remove('United States')

#7) Using a for loop, print each country's name in all caps.
for country in countries:
    print(country.upper())

# PART TWO: Dictionaries

tree = {
    'name' :'Árbol del Tule',
    'species' : 'Taxodium mucronatum',
    'age' : 1500,
    'location_name' : 'Oaxaca, Mexico',
    'latitude' : 17.0465065069963,
    'longitude' : -96.63618837482673
}

print(f"{tree['name']} is a {tree['age']:,} year old tree that is in {tree['location_name']}")

newyork = {
    'latitude' : 40.7128,
    'longitude' : -74.0059
}

if tree['latitude'] < newyork['latitude']:
    print(f"The tree {tree['name']} in {tree['location_name']} is south of NYC")
else:
    print(f"The tree {tree['name']} in {tree['location_name']} is north of NYC")

user_age = input("How old are you?")
user_age = int(user_age)

if user_age > tree['age']:
    print(f"You are {user_age - tree['age']} years older than {tree['name']}.")
elif user_age < tree['age']:
    print(f"{tree['name']} was {tree['age']-user_age:,} years old when you were born.")


# PART TWO: List of dictionaries

cities = [
   {
      'name' : 'Moscow',
      'latitude' : 55.75838263807063,
      'longitude' : 37.61605473190841
   },
     {
      'name' : 'Tehran',
      'latitude' : 35.729421960290466,
      'longitude' : 51.34072050667131
   },
   {
      'name' : 'Falkland Islands',
      'latitude' : -51.76787874412779,
      'longitude' : -58.94950001371609
   },
    {
      'name' : 'Seoul',
      'latitude' : 37.563672530835994,
      'longitude' : 126.99060210436139
   },
    {
      'name' : 'Santiago',
      'latitude' : -33.43797689039714,
      'longitude' : -70.66285607767455
   }
]

for city in cities:
    if city['latitude'] > 0:
        print(f"{city['name']} is above the Equator")
    else:
        print(f"{city['name']} is below the Equator")
    if city['name'] == 'Falkland Islands':
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

for city in cities:
    if city['latitude'] > tree['latitude']:
        print(f"{city['name']} is north of {tree['name']}")
    else:
        print(f"{city['name']} is south of {tree['name']}")