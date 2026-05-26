# -----------------------------------------------
# 🔁 Advanced Python Exercise 04: Loops & Modules
# -----------------------------------------------

# 💡 In this exercise, you'll work with lists, loops, the `random` module, and modular code using custom Python files.

# -----------------------------------------------
# Question 1: Iterating with Index and Value
# -----------------------------------------------

# 📝 Task:
# - Create a list called `dishes` with at least 5 South African traditional dishes.
# - Use a `for` loop and `enumerate()` to print each dish in this format:
#   "Dish 1: Bunny Chow"
dish=["Umphokoqo","Umngqusho","Isidudu","Umbengo","Amanqina"]
for index,dishes in enumerate(dish,start=1):
    print(f" Dish {index}: {dishes}")
# 💡 Tip:
# Use `enumerate(dishes, start=1)` to get both the index and the dish name.


# -----------------------------------------------
# Question 2: Countdown with Timer
# -----------------------------------------------

# 📝 Task:
# - Use a `while` loop to count down from 10 to 1.
# - Print each number with a 1-second pause between each.

# 💡 Tip:
# Import the `time` module and use `time.sleep(1)` to pause for one second between prints.
import time
count=10
while count>=1:
    print(count)
    time.sleep(1)
    count-=1

# -----------------------------------------------
# Question 3: Printing Squares and Cubes in a Table
# -----------------------------------------------

# 📝 Task:
# - Use a `for` loop with `range(1, 11)` to print a table of numbers 1 to 10.
# - For each number, print its square and cube neatly formatted in columns.

# 💡 Tip:
# Use formatted strings (f-strings) and alignment tricks like `:^6` for clean table layout.
for numbers in range(1,11):
    sqaure=numbers*numbers
    cube=numbers*numbers*numbers
    print(numbers,sqaure,cube)

# -----------------------------------------------
# Question 4: Random Selection with No Repeats
# -----------------------------------------------

# 📝 Task:
# - Create a list of 10 colours (e.g., red, blue, green, etc.).
# - Use `random.sample()` to select and print 5 unique colours without repetition.

# 💡 Tip:
# Import the `random` module and use `random.sample(list, 5)` to avoid duplicates.
import random
list=["red","blue","green","yellow","black","purple","orange","brown","white"]
print(random.sample(list,k=5))


# -----------------------------------------------
# Question 5: Using a Custom Module and Looping Calculator
# -----------------------------------------------

# 📝 Task:
# - Create a separate Python file named `math_advanced.py` containing four functions:
#   `add`, `subtract`, `multiply`, and `divide`.
# - In your main file, import that module and build a loop that:
#     - Takes two numbers and an operation from the user.
#     - Calls the corresponding function from the module.
#     - Repeats until the user types `q` to quit.
import math_advanced

while True:
    select=input("enter operator(+,-,*,/ or 'q' for quit):  ")
    if select=='q':
        break
    if select not in ['+','-','*','/']:
        print("invalid operation")
        continue
    
    try:
            num1=int(input("enter number: "))
            num2=int(input("enter 2nd number: "))
            if select=="+":
                 result=math_advanced.add(num1,num2)
                 
            
            elif select=="-":
                 result=math_advanced.subtract(num1,num2)
                 
            
            elif select=="*":
                 result=math_advanced.multiply(num1,num2)
                 
            
            elif select=="/":
                 result=math_advanced.divide(num1,num2)
            
            print(f"Answer: {result}")     
    except ValueError:
         print("error cannot perform calculation!")        
print("Thank you !")         

            
        


# 💡 Tip:
# Handle invalid operations and division by zero using if-else and try-except blocks.
# Create the file `math_advanced.py` with function definitions like:

# def add(a, b): return a + b
# def subtract(a, b): return a - b
# def multiply(a, b): return a * b
# def divide(a, b): return a / b if b != 0 else "Cannot divide by 0"

