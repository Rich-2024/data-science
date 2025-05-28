# 1. Create a list with 5 items (names of people) and output the 2nd item
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("1. 2nd item:", people[1])

# 2. Change the value of the first item
people[0] = "Alex"
print("2. Changed first item:", people)

# 3. Add a sixth item to the list
people.append("Fiona")
print("3. Added sixth item:", people)

# 4. Add “Bathel” as the 3rd item
people.insert(2, "Bathel")
print("4. Added Bathel as 3rd item:", people)

# 5. Remove the 4th item
del people[3]
print("5. Removed 4th item:", people)

# 6. Use negative indexing to print the last item
print("6. Last item (negative index):", people[-1])

# 7. New list, print 3rd, 4th, and 5th items
new_list = [10, 20, 30, 40, 50, 60, 70]
print("7. 3rd, 4th, 5th items:", new_list[2:5])

# 8. List of countries and make a copy
countries = ["Kenya", "Ghana", "Brazil", "Canada"]
countries_copy = countries.copy()
print("8. Countries:", countries)
print("   Copy of countries:", countries_copy)

# 9. Loop through the list of countries
print("9. Looping through countries:")
for country in countries:
    print("-", country)

# 10. List of animal names, sort ascending and descending
animals = ["zebra", "elephant", "lion", "giraffe", "antelope"]
print("10. Animals sorted ascending:", sorted(animals))
print("    Animals sorted descending:", sorted(animals, reverse=True))

# 11. Animal names with the letter ‘a’
print("11. Animals with 'a' in name:")
for animal in animals:
    if 'a' in animal.lower():
        print("-", animal)

# 12. Two lists: first names and second names, join them
first_names = ["John", "Mary", "Ali"]
last_names = ["Doe", "Smith", "Khan"]
full_names = first_names + last_names
print("12. Joined names:", full_names)
