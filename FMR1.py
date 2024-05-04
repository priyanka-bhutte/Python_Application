#Using inbuilt filter map reduce function
from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 1

def Add(A,B):
    return A + B

def main():
    Data = [11,14,20,23,18,16,15,20]

    print("Data from input list : ",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after filter activity : ",FData)

    MData = list(map(Increase,FData))
    print("Data after map activity : ",MData)

    RData = reduce(Add,MData)
    print("Data after reduce activity is : ",RData)
if __name__ =="__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python FMR1.py
# Data from input list :  [11, 14, 20, 23, 18, 16, 15, 20]
# Data after filter activity :  [14, 20, 18, 16, 20]
# Data after map activity :  [15, 21, 19, 17, 21]
# Data after reduce activity is :  93