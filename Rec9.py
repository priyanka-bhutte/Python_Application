# Factorial of 5 is : 5 * 4 * 3 * 2 * 1 i.e 120

i =1
Fact = 1
def Factorial(No):
    global i
    global Fact

    if(No >= 1):
        Fact = Fact * No
        No = No - 1
        Factorial(No)

    return Fact

def main():
    print("Enter the number limit : ")
    num = int(input())
    
    Ret = Factorial(num)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python Rec9.py
# Enter the number limit :
# 5
# Factorial is :  120


