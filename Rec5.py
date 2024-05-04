i = 1
def fun():
    global i        # use global word to access the global varibales
    print("Inside fun",i)
    i = i + 1
    fun()

def main():
    fun()

if __name__ == "__main__":
    main()


# Output:
# C:\Users\Priyanka\Desktop\Python_2024\27-04-202
# Inside fun 1
# Inside fun 2
# Inside fun 3
# Inside fun 4
# Inside fun 5
# Inside fun 6
# Inside fun 7
# Inside fun 8
# Inside fun 9
# Inside fun 10
# Inside fun 11
# Inside fun 12
# .
# .
# .
# .
# .
# Inside fun 997
# Inside fun 998
# Traceback (most recent call last):
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec5.py", line 12, in <module>
#     main()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec5.py", line 9, in main
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec5.py", line 6, in fun
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec5.py", line 6, in fun
#     fun()
#   File "C:\Users\Priyanka\Desktop\Python_2024\27-04-2024\Rec5.py", line 6, in fun
#     fun()
#   [Previous line repeated 995 more times]
# RecursionError: maximum recursion depth exceeded
