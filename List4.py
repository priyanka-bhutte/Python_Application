def Addition(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum

def main():
    print("Demonstration of addtion of n number of data using List")

    print("Enter the number of elements that you want to insert int the list : ")
    size = int(input())
    
    Arr = []  # or Arr = list()
    print("Enter the values in List")

    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are : ",Arr)

    Result = Addition(Arr)
    print("Sumation of all elements : ",Result)

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\21-04-2024>python List4.py
# Demonstration of addtion of n number of data using List
# Enter the number of elements that you want to insert int the list :
# 5
# Enter the values in List
# 10
# 20
# 30
# 40
# 50
# Entered elements are :  [10, 20, 30, 40, 50]
# Sumation of all elements :  150