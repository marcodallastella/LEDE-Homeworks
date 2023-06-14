# Marco Dalla Stella
# 2023-06-07
# Homework 2, Part 1

print("PART ONE: Lists")

numbers = [22, 90, 0, -10, 3, 22, 48]

print("2. Display the number of elements in the list")
print(len(numbers))

print("3. Display the 4th element of this list.")
print(numbers[3])

print("4. Display the sum of the 2nd and 4th element of the list.")
print(numbers[1]+numbers[3])

print("5. Display the 2nd-largest value in the list.")
numbers_sort = sorted(numbers)
print(numbers_sort[-2])

print("6. Display the last element of the original unsorted list")
print(numbers[-1])

print("7. Display the sum of all of the numbers divided by two.")
result = sum(numbers)/2
print(result)

print("8. Print whether the median or the mean of the numbers is higher")
mean = int(sum(numbers)/len(numbers))

median_len = len(numbers_sort)

if median_len % 2 == 0:
    median1 = numbers_sort[median_len//2]
    median2 = numbers_sort[median_len//2 - 1]
    median = (median1 + median2)/2
else:
    median = numbers_sort[median_len//2]
    
if mean > median:
    print(f"Mean value is {mean}, which is higher than {median}")
elif mean < median:
    print(f"Mean value is {median}, which is higher than {mean}")
else:
    print(f"It seems mean and median have the same value of {mean}")

print("######")
print("PART ONE: Dictionaries")

movie = {
    'title' : 'Jurassic Park',
    'year' : 1993,
    'director' : 'Steven Spielberg'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie['budget'] = 63000000
movie['revenue'] = 1109802321

if movie['budget'] > movie['revenue']:
    print("That was a bad investment.")
elif movie['revenue'] > movie['budget']*5:
    print("That was a great investment")
else:
    print("That was an okay investment.")


population = {
    'Manhattan' : 1.6,
    'Brooklyn' : 2.6,
    'Bronx' : 1.4,
    'Queens' : 2.3,
    'Staten Island' : 0.47
}
print("Population of Brooklyn:")
print(population['Brooklyn'], "million.")

print("Population of New York City:")
pop_ny = sum(population.values())
print(pop_ny,"million.")

Manhattan_percentage = (population['Manhattan']/pop_ny*100)
Manhattan_percentage = round(Manhattan_percentage, 2)

print(Manhattan_percentage,"percent of NYC's population lives in Manhattan")
