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
def ali():
    select=input("what do you want to use? \n1. atmachine \n2. curency \n3. nothing ")
    if select=="atmachine":
        balance=1000
        print(f"Your balance is {balance}")
        withdraw=int(input("Enter amount to withdraw:"))
        if withdraw<=balance:
            balance=balance-withdraw
            print(f"Your new balance is {balance}")
        else:
            print("Insufficient funds")
    elif select=="curency":
        amount=int(input("Enter amount in PKR:"))
        usd=amount/150
        print(f"Your amount in USD is {usd}")
    else:
        print("Thank you for using our services")

    