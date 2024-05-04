# Name = lambda Parameters : Logic
# Name(___, ____, .....)

def CheckEven(A):
  return (A%2 == 0)          # return true if condition is true other wise false

CheckEvenX = lambda A : (A%2 == 0)  # CheckEvenX is considered as python object

def main():
    Ret = CheckEvenX(10)
    if(Ret == True):
       print("It is even number")
    else:
       print("It is odd number")

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python lambda6.py
# It is even number
