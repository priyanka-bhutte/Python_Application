# Name = lambda Parameters : Logic
# Name(___, ____, .....)

def Addition(A,B):
  return  A + B

Add = lambda A,B : A+B

def main():
    Ret = Addition(10,11)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python lambda2.py
# Addition is :  21
