#Task 1: Calculate Factorial Using a Function

def factorial(n):
 
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))
n=int(input("enter a number"))
result= factorial(n)
print(result)

#Task 2: Using the Math Module for Calculations
import math
num=int(input("enter a number"))
print(math.sqrt(num))
print(math.log(num))
print(math.sin(num))