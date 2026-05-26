# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits=["apple","orange","pineapple","blueberry"]
# TODO: Add a fruit to the end of the list
fruits.append("peach")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"coconut")
# TODO: Remove a fruit from the list
fruits.remove("orange")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers=[1,2,3,4,5]
# TODO: Create a new list with each number squared
new=[num**2 for num in numbers]
# TODO: Find the sum and average of the original numbers
total=sum(numbers)
avg=total/len(numbers)
# TODO: Print the results
print(f"squared numbers: {new}")
print(f"sum of numbers: {total}, Average{avg}")

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries={"South Africa": "Pretoria","Egypt":"Cairo","Zimbabwe":"Harare"}
# TODO: Add a new country-capital pair
countries["England"]="London"

# TODO: Update the capital of an existing country
countries["South Africa"]="Cape Town"
# TODO: Remove a country-capital pair
del countries["Zimbabwe"]
# TODO: Print the modified dictionary
print(countries)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors={"Apple":"green","Banana":"Yellow","Orange":"orange"}
# TODO: Print all the fruits (keys)
print(fruit_colors.keys())
# TODO: Print all the colors (values)
print(fruit_colors.values())

# TODO: Print each fruit and its color
for fruit,color in fruit_colors.items():
    print(f"The {fruit} is {color}")
# TODO: Check if a fruit is in the dictionary and print its color
check_fruit=input("search fruit: ")
if check_fruit in fruit_colors:
    print(f"The color of {check_fruit} is {fruit_colors[check_fruit]}")
else:
    print("fruit not found")
