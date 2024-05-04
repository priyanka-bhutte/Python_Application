
def DisplayR(No):

    if(No >= 1):
        print(No)
        No = No - 1
        DisplayR(No)

def main():
    print("Enter the number limit : ")
    num = int(input())
    
    DisplayR(num)

if __name__ == "__main__":
    main()

# output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python Rec8.py
# Enter the number limit :
# 10
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


