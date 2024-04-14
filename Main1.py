def Addition(No1, No2):
    print("Inside Addition function")
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Inside main function")
    print("Enter first number : ")
    A = int(input())

    print("Enter second number : ")
    B = int(input())

    Result = Addition(A,B)

    print("Addition is : ",Result)
    
main()
print("End of application")

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\14-04-2024>python Main1.py
# Inside main function
# Enter first number :
# 11
# Enter second number :
# 10
# Inside Addition function
# Addition is :  21
# End of application









# Output:
# C:\Users\Priyanka\Desktop\Python_2024\13-04-2024>python Function2.py
# Enter first number :
# 11
# Enter second number :
# 22
# Addition is :  33