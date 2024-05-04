import os

def main():
    print("PID of running process : ",os.getpid())
    print("PID of parent process ie command prompt is : ",os.getppid())

if __name__ == "__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python Multi1.py
# PID of running process :  31648
# PID of parent process ie command prompt is :  32520

# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python Multi1.py
# PID of running process :  10448
# PID of parent process ie command prompt is :  32520

# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python Multi1.py
# PID of running process :  40532
# PID of parent process ie command prompt is :  32520

# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python Multi1.py
# PID of running process :  27728
# PID of parent process ie command prompt is :  32520

#32520 is process id of Command promt which not getting changed. cmd is interface between the end user and os. CMd is CUI version of desktop