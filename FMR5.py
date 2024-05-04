#Using user defined filter map reduce function
from functools import reduce

CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No : No + 1
Add = lambda A,B : A + B


# Task : Name of function
# Elements : List of data elements
def filterX(Task,Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

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

    MData = list(map(Increase,FData))
    print("Data after map activity : ",MData)
    
    RData = reduce(Add,MData)
    print("Data after reduce activity is : ",RData)
if __name__ =="__main__":
    main()

# output:

