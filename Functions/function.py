# Introduction to function
#%%
# Simple calculator
firstNum = input("Enter your first number: ")
secNum = input("Enter your second number: ")

def addition(num_1, num_2):
    return int(num_1) + int(num_2)

print ("addition is:",addition(firstNum,secNum))
# Task - create the remaining functions for substraction, multiplication and division
def substract(num_1, num_2):
    return int(num_1) - int(num_2)

print("substract is:",substract(firstNum,secNum))

def multiply(num_1, num_2):
    return int(num_1) * int(num_2)

print("multiply is:",multiply(firstNum,secNum))

def divide(num_1,num_2):
    return int(num_1) / int(num_2)

print("divide is:",divide(firstNum,secNum))
