import sys

def DisplayF():
    print("Inside Display of foor loop : ")
    for i in range(1,6):
        print(i)

def DisplayW():
    print("Using While LooInside Display of while loop :")
    i = 1
    while(i<=5):
        print(i)
        i = i+1


def main():
    print("Welcome to the application : ",sys.argv[0])

    DisplayF()
    DisplayW()

if __name__ =="__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python Loops.py
# Welcome to the application :  Loops.py
# Inside Display of foor loop :
# 1
# 2
# 3
# 4
# 5
# Using While LooInside Display of while loop :
# 1
# 2
# 3
# 4
# 5
