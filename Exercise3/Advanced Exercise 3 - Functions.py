# -------------------------------------------
# Advanced Python Exercise 03: Functions
# -------------------------------------------

# Question 1: Function with Parameters and Conditional Logic
# TODO: Define a function `greet_user` that takes `name` and `role` as parameters.
#       If role is "admin", greet them with "Welcome Admin <name>!"
#       Otherwise, greet them with "Hello <name>, enjoy your session."

# TIP: Use an if-else statement inside the function.
def greet_user(name,role):
    
    if role=="admin":
        result=(f"welcome admin{name}")
    else:
        result=(f"hello {name}, enjoy your session")
        print(result)
greet_user("Avela","admin")        
greet_user("Luke","user")
# ------------------------------------------------------------------------------------

# Question 2: Function with Default and Keyword Arguments
# TODO: Define a function `register_student` with parameters:
#       `name`, `course`, and `country='South Africa'`.
#       It should print a formatted registration message using all the data.
def register_student(name,course,country="South Africa"):
    print(f"Hello  {name} you have been successfuly registered for {course} course in {country}")
# TODO: Call this function twice:
#       - Once using positional arguments
#       - Once using keyword arguments in a different order
register_student("Avela"," IT")
register_student(course=" IT",name=" Avela")
# ------------------------------------------------------------------------------------

# Question 3: Returning Multiple Values
# TODO: Define a function `calculate_scores` that accepts 3 scores (int),
#       and returns the total and average.
def calculate_scores(score1,score2,score3):
    
    total=score1+score2+score3
    avg=total/3
    return total,avg
# TODO: Unpack the returned values and print them separately
value,val=calculate_scores(78,56,23)
print(f"Total: {value}, Average{val} ")
# TIP: Use the `return` keyword with comma-separated values.




# ------------------------------------------------------------------------------------

# Question 4: Nested Functions
# TODO: Define a function `student_progress` that:
#       - Accepts student name and 3 test scores
#       - Inside it, define another function `average_score` that calculates the average
#       - Return a message: "<name>'s average score is: <average>"
def student_progress(name,point1,point2,point3):
    def average_score():
        return(point1+point2+point3)/3
    average=average_score()
    return (f"{name}'s average score is: {average}")
print(student_progress("Avela",56,67,89))
# ------------------------------------------------------------------------------------

# Question 5: Function as Arguments with Lambdas
# TODO: Define a function `apply_to_list` that takes a list and a function,
#       and applies the function to each item in the list using a loop.
def aplply_to_list(numbers,func):
    result=[]
    for item in numbers:
        result.append(func(item))
    return
nums=[1,2,3,4]
# TODO: Use `apply_to_list` to double all items in `[1, 2, 3, 4]` using a lambda function.
double=aplply_to_list(nums,lambda x: x*2)
print(f"doubled: {double}")
# TODO: Then use it again to square all items in the same list using another lambda.
sqaure=aplply_to_list(nums,lambda x:x**2 )
print(f"sqaured {sqaure}")
# TIP: Lambda functions are useful for short, anonymous operations.

# ------------------------------------------------------------------------------------

# Question 6: Optional Challenge - Flexible Arguments
# TODO: Create a function `describe_user` that accepts name, and any number of hobbies using `*args`.
#       It should print the name and list of hobbies in a friendly format.
def describe_user(name,*hobbies):
    print(f"Name: {name}")
    print(f"Hobbies: {hobbies}")
    for hobby in hobbies:
        print(f"- {hobby}")
# TODO: Call the function with 3 or more hobbies.
describe_user("Avela","football","reading")
# TIP: Use a loop to iterate over `*args`.

