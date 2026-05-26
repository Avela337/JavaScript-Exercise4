# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits=['Apple','Orange','Pear','Banana','Peach']
# TODO: Use a for loop to print each fruit in the list

for i in fruits:
    print(i)
    


#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count=5
while count>0:
    print(count)
    count=count-1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for num in range(1,11):
    print (num**2)




#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors=['Red','Blue','Black','Green','Yellow']
# TODO: Use a for loop to select and print 3 random colors from the list
random_color=random.choice(colors)
print(random_color)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations
# TODO: Use a while loop to create a simple calculator
while True:
   print("\nSelect operation: +,-,*,/ or 'q' to quit")
   choice=input("enter a choice: ").lower()
   if choice=='q':
      break
   num1=float(input("enter a number: "))
   num2=float(input("enter 2nd number: "))
   if choice=="+":
      print("Answer: ", math_operations.add(num,num2))
   elif choice=="-":
      print("Answer: ",math_operations.subtract(num1,num2))
   elif choice=="*":
      print("Answer: "),math_operations.multiply(num1,num2)
   elif choice=="/":
      print("Answer: ",math_operations.divide(num1,num2))
   else:
      print("invalid input")
   


