#Using inbuilt filter map reduce function
from functools import reduce

def main():
    Data = [11,14,20,23,18,16,15,20]

    print("Data from input list : ",Data)

    FData = list(filter((lambda No : (No % 2 == 0)),Data))
    print("Data after filter activity : ",FData)

    MData = list(map((lambda No : No + 1),FData))
    print("Data after map activity : ",MData)

    # 15,21,19,17,21
    # 0 + 15 = 15
    # 15 + 21 = 36
    # 36 + 19 = 55
    # 55 + 17 = 72
    # 72 + 21 = 93
    RData = reduce((lambda A,B : A + B),MData)
    print("Data after reduce activity is : ",RData)
if __name__ =="__main__":
    main()

# output:
# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python FMR3.py
# Data from input list :  [11, 14, 20, 23, 18, 16, 15, 20]
# Data after filter activity :  [14, 20, 18, 16, 20]
# Data after map activity :  [15, 21, 19, 17, 21]
# Data after reduce activity is :  93
