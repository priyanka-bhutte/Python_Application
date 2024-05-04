def fun():
    i = 1                  # i get created newly at every function call
    print("Inside fun",i)
    i = i + 1
    fun()

def main():
    fun()

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-2024>python Rec4.py
# Inside fun 1
# Inside fun 1
# Inside fun 1
# Inside fun 1
# Inside fun 1
# Inside fun 1
# Inside fun 1
# Inside fun 1
# Inside fun 1
# Inside fun 1
# Inside fun 1
# .
# .
# .
# .
# Inside fun 1
# Inside fun 1
# Traceback (most recent call last):
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec4.py", line 11, in <module>
#     main()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec4.py", line 8, in main
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec4.py", line 5, in fun
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec4.py", line 5, in fun
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec4.py", line 5, in fun
#     fun()
#   [Previous line repeated 995 more times]
# RecursionError: maximum recursion depth exceeded