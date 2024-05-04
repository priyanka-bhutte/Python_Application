# Name = lambda Parameters : Logic
# Name(___, ____, .....)

def Cube(A):
  return  A * A * A

CubeX = lambda A : A*A*A

def main():
    Ret = CubeX(10)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()

# Output:
#C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python lambda3.py
# Addition is :  1000
