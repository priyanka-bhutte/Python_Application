#Using user defined filter map reduce function

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