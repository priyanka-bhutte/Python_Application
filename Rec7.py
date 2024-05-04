i = 1

def DisplayR(No):
    global i

    if(i <= No):
        print(i)
        i = i + 1
        DisplayR(No)

def main():
    print("Enter the number limit : ")
    num = int(input())
    
    DisplayR(num)

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python Rec7.py
# Enter the number limit :
# 10
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10