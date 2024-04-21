import sys

def main():
    print("Demonstration of command line argument")

    print("Name of application : ",sys.argv[0])

    print("Datatype of argv is : ",type(sys.argv))

    print("Number of command line arguments are : ",len(sys.argv))

    print("First argument is : ",sys.argv[1])
    print("Second argument is : ",sys.argv[2])

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\21-04-2024>python Command.py "Priyanka Bhutte" Mumbai
# Demonstration of command line argument
# Name of application :  Command.py
# Datatype of argv is :  <class 'list'>
# Number of command line arguments are :  3
# First argument is :  Priyanka Bhutte
# Second argument is :  Mumbai