# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x=2
x+=3
# TODO: Multiply y by 2 using the *= operator
y=3
y*=2
# TODO: Divide x by y and store the result in a variable called 'result'
result=x/y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a=5
b=3
c=9
# TODO: Create a condition that checks if a is greater than b
if a > b :
    num= True
else:
    num=False

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b % 2==0:
    num2=True
else:
    num2=False
# TODO: Create a condition that checks if c is less than or equal to a
if c <= a:
    num3=True
else:
    num3=False
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
if num or (num2 and num3):
    final_condition=True
else:
    final_condition=False

# TODO: Print the value of 'final_condition'
print(f"Final condition is: { final_condition}")
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score=int(input("enter your test score: "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score >= 90:
    grade="A"
elif score >=80:
    grade="B"
elif score>=70:
    grade="C"
elif score >=60:
    grade="D"
else:
    grade="F"

# TODO: Print the grade for the given score
print(f"Your grade is: {grade}")
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1=int(input("enter a num 1: "))
num2=int(input("enter a num 2: "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation=input("put an operator (+,-,*,/): ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation =="+":
    print(f"Ans: {num1+num2}")
elif operation=="-":
    print(f"Ans: {num1-num2}")
elif operation=="*":
    print(f"Ans: {num1*num2}")
elif operation=="/":
    if num2!=0:
        print(f"Ans: {num1/num2}")
    else:
        print("error")
else:
    print("invalid operation")

# TODO: Handle the case of division by zero


# TODO: Print the result of the operation
