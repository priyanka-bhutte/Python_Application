def fun():
    print("Inside fun")
    fun()

def main():
    fun()

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python Rec3.py
# Inside fun
# Inside fun
# Inside fun
# .
# .
# .
# .
# Inside fun
# Traceback (most recent call last):
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec3.py", line 9, in <module>
#     main()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec3.py", line 6, in main
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec3.py", line 3, in fun
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec3.py", line 3, in fun
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec3.py", line 3, in fun
#     fun()
#   [Previous line repeated 995 more times]
# RecursionError: maximum recursion depth exceeded
