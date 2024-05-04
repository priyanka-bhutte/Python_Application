# Name = lambda Parameters : Logic
# Name(___, ____, .....)

def Cube(A):
  return  A**3

CubeX = lambda A : A**3

def main():
    Ret = CubeX(10)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python lambda4.py
# Addition is :  1000
# 
