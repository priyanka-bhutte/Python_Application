import sys

def Addition(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    # This is called as Banner
    print("Welcome to the application : ",sys.argv[0])

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Please provide the numeric arguments to perform addition")
        return 
    
    Result = Addition(int(sys.argv[1]),int(sys.argv[2]))
    
    print("Addition is : ",Result)


if __name__ == "__main__":
    main()


# Output:
# C:\Users\Priyanka\Desktop\Python_2024\21-04-2024>python Addition.py 10
# Welcome to the application :  Addition.py
# Invalid number of arguments
# Please provide the numeric arguments to perform addition

# C:\Users\Priyanka\Desktop\Python_2024\21-04-2024>python Addition.py 10 20
# Welcome to the application :  Addition.py
# Addition is :  30