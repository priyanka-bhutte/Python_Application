from MarvellousFMR import *

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

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python FMR10.py
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
