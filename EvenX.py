def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("It is odd number")

def main():
    print("Enter number : ")
    A = int(input())

    CheckEven(A)

print(__name__)

if __name__ == "__main__":
    main()


# Output:
# C:\Users\Priyanka\Desktop\Python_2024\14-04-2024>python EvenX.py
# __main__
# Enter number :
# 14
# It is even number
# 