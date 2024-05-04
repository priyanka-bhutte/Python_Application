import os
import multiprocessing

def Task1(No):
    print("Executing first task")
    print("PID of task1 : ",os.getpid())  # suppose 51
    print("PID of task1 : ",os.getppid()) # will be 11

def Task2(No):
    print("Executing first task")
    print("PID of task2 : ",os.getpid())  #suppuse 101
    print("PID of task2 : ",os.getppid()) # will be 11

def main():
    print("PID of running process : ",os.getpid())  #suppose  ...it is my process
    print("PID of parent process ie command prompt is : ",os.getppid())  #supoose 21 .. it is main process

    Value = 11
    p1 = multiprocessing.Process(target = Task1, args = (Value,))
    p2 = multiprocessing.Process(target = Task2, args = (Value,))

    p1.start()
    p2.start()

    # join is used to say until my child process get completely executed the main process has to alive
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()


#my process has two prosess ie task1 and task2

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\28-04-2024>python Multi2.py
# PID of running process :  35664
# PID of parent process ie command prompt is :  32520
# Executing first task
# PID of task1 :  37580
# PID of task1 :  35664
# Executing first task
# PID of task2 :  36472
# PID of task2 :  35664

