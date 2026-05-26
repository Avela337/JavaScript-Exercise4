# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a+=3
# TODO: Multiply b by 2 using *=
b*=2
# TODO: Modulo c by 4 using %=
c%=4

# TODO: Calculate the square root of (a^2 + b^2 + c^2)
result=math.sqrt(a**2+b**2+c**2)
# TODO: Print the final result rounded to 2 decimal places
print(f"The answer is: {round(result,2)}")


# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x=int(input("enter num1: "))
y=int(input("enter num2: "))
z=int(input("enter num3: "))
# TODO: Create conditions:
#   is_even = True if x is even
#   is_positive = True if y > 0
#   is_in_range = True if z between 10 and 50
is_even=x%2==0
is_positive=y>0
is_in_range=10 <= z <=50
if is_even and is_positive and is_in_range:
    print("All conditions are met")
else:
    print("Conditions are not met")
# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition= is_even and is_in_range
# TODO: Print final_condition
print(final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
base_score=int(input("enter your base score: "))
# TODO: Apply adjustments
late=input("was it late? (y/n) ")


final=base_score
if late:
    final-=10
else:

    final+=5
    

# TODO: Clamp score between 0 and 100
final= max(0,min(100,final))
# TODO: Use if-elif-else to determine grade and print it
if final >=90:
    grade="A"
elif final>=80:
    grade="B"
elif final>= 70:
    grade="C"
elif final>=60:
    grade="D"
else:
    grade="F"
print(f"Adjusted score: {final}")    
print(f"Grade: {grade}")


# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.
def calculater():
    try:
#  Input num1, num2
        num1=int(input("enter a number 1: "))
        num2=int(input("enter number 2: "))
    # TODO: Input operation
        operation=input("choose an operator(+, -, *, /, %, **):  ")
    # TODO: Match operation using if-elif

        if operation=="+":
            result=num1+num2
    #  
        elif operation=="-":
            result=num1-num2
    
        elif operation=="*":
            result=num1*num2

        elif operation=="/":
            if num2==0:
                print("Error: you can't divide by 0 ")
                return
            result=num1/num2
        elif operation=="%":
            if num2==0:
                print("error: you can't MOD by 0")
                return
            result=num1%num2
    
        elif operation =="**":
            result=num1**num2
        else:
            print(f"error {operation} is not valid")
            return
        if result==int(result):
            print(f"Result: {num1} {operation} {num2} = {int(result)}")
        else:
            print(f"Result: {num1} {operation} {num2} = {result}")


#  Handle division/modulus by zero with try-except
    except ValueError:
        print("error invalid input")

calculater()
# TODO: Print result


