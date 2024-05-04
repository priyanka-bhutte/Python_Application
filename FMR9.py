#Using user defined filter map reduce function
from functools import reduce

CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No : No + 1
Add = lambda A,B : A + B


# Task : Name of function
# Elements : List of data elements
# filterX(CheckEven, [11,14,20,23,18,16,15,20])

def filterX(Task,Elements):
    Result = []             # Empty list to store filtered data
    
    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    Sum = 0

    # [15,21,19,17,21]
    for no in Elements:
        Sum = Task(Sum,no)

    return Sum

def main():

    print("Enter the number of elements  : ")
    size = int(input())

    Data = []

    print("Enter the elements : ")

    for i in range(0,size):
        no = int(input())
        Data.append(no)
    
    print("Data from input list : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filter activity : ",FData)

    MData = list(mapX(Increase,FData))
    print("Data after map activity : ",MData)
    
    RData = reduceX(Add,MData)
    print("Data after reduce activity is : ",RData)
if __name__ =="__main__":
    main()

# output:
# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python FMR9.py
# Enter the number of elements  :
# 5
# Enter the elements :
# 10
# 11
# 12
# 13
# 14
# Data from input list :  [10, 11, 12, 13, 14]
# Data after filter activity :  [10, 12, 14]
# Data after map activity :  [11, 13, 15]
# Data after reduce activity is :  39

