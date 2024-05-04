import sys


def main():
    print("Recursion limit is : ",sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("Recursion limit is : ",sys.getrecursionlimit()) # it display the 1500 but practically we can not predict that it will be available or not

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python Rec2.py
# Recursion limit is :  1000
# Recursion limit is :  1500
