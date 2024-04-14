# Here we are taking only required things from module Marvellous.py
# Specific import
from Marvellous import Addition
from Marvellous import Multiplication

def main():
    print("Enter first number : ")
    A = int(input())

    print("Enter second number : ")
    B = int(input())

    Ans = Addition(A,B)
    print("Addition is : ",Ans)

    Ans = Multiplication(A,B)
    print("Multiplication is : ",Ans)

main()

# modules byte code files gets generated automatically in __pycache__ folder
# Here module is Marvellous.py
# module should be in current directory 

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\14-04-2024>python Client1.py
# Enter first number :
# 11
# Enter second number :
# 10
# Addition is :  21
# Multiplication is :  110

