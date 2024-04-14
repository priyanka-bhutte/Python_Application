def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("It is odd number")

def main():
    print("Enter number : ")
    A = int(input())

    CheckEven(A)

main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\14-04-2024>python Even.py
# Enter number :
# 14
# It is even number

# C:\Users\Priyanka\Desktop\Python_2024\14-04-2024>python Even.py
# Enter number :
# 7
# It is odd number