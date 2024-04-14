
def Calculations(No1, No2):
    Add = No1 + No2
    Sub = No1 - No2

    return Add, Sub

print("Enter first number : ")
A = int(input())

print("Enter second number : ")
B = int(input())

Result1, Result2 = Calculations(A,B)

print("Addition is : ",Result1)
print("Substraction is : ",Result2)

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\14-04-2024>python Multiple.py
# Enter first number :
# 11
# Enter second number :
# 10
# Addition is :  21
# Substraction is :  1
