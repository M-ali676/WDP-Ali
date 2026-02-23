# function in python
# is a modular programming in python
# user defined modules in python
# built in modules in python
# import math
# print(math.sqrt(16))
# from math import sqrt
# print(sqrt(16))
# from math import sqrt as s
# print(s(16))  
# import math as m
# print(m.sqrt(16))
# def function_name(parameters):
#     # function body
#     return value
def rafay():
    select=input("what do you want to use? \n1. calculator \n2. mark sheet \n3. nothing ")
    if select=="calculator":
        num1=int(input("Enter first number 1:"))
        num2=int(input("Enter second number 2:"))
        print(f"This is Addition: {num1+num2} \nThis is Subtraction: {num1-num2} \nThis is Multiplication: {num1*num2} \nThis is Division: {num1/num2}")
    elif select=="mark sheet":
        obtain=int(input("Enter obtain marks:"))
        total=500
        per=(obtain/total)*100
        if per>=70:
            grade="A+"
        else:
            grade="Fail"
        print(grade)