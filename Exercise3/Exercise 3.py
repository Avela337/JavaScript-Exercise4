# Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"
def greet():
    print("hello, world")

# TODO: Call the 'greet' function
greet()

#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalized_greeting(name):
    print(f"Hello , {name} I hope you are good")
# TODO: Call the 'personalized_greeting' function with your name
personalized_greeting("Avela")

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number as a parameter and returns its square
def square(num):
    return num**2
num2=[2,4,6,8,10]
for num3 in num2:
    print(f"The square of {num3} is {square(num3)}")
# TODO: Call the 'square' function with the number 5 and print the result
print(f"The square of 5 is {square(5)}")

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length,width):
    return length*width
area=rectangle_area(4,5)
print(f"The area of a rectanle is {area}")

# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result


#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(func,number):
    return func(number)
# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double(number):
    return number *2
# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
result_double=apply_operation(double,7)
print(result_double)
# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
def sqaure(number):
    return number **2
result_sqaure=apply_operation(sqaure,3)
print(result_sqaure)
