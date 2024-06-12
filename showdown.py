# Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

# Approach one

num1 = input("Please enter the first number")
num2 = input("Please enter the second number")
num3 = input("Please enter the third number")

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2 
else:
    largest = num3
    
print("Largest number is",largest)

#Approach 2

# num1 = input("Please enter the first number")
# num2 = input("Please enter the second number")
# num3 = input("Please enter the third number")

# res = max(num1, max(num2,num3))

# print("Largest of the 3 numbers is" , res)
