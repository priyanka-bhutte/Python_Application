def Display(count):
    n = 0
    if(count <= 0):
        print("Invalid number")
        return

    for n in range(count):
        print("Jay Ganesh...")

def main():
    Cnt = int(input("Please enter the frequency : "))
    Display(Cnt)

if __name__ =="__main__":
    main()

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\20-04-2024>python Loop2.py
# Please enter the frequency : 5
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...

# C:\Users\Priyanka\Desktop\Python_2024\20-04-2024>python Loop2.py
# Please enter the frequency : -4
# Invalid number

# C:\Users\Priyanka\Desktop\Python_2024\20-04-2024>python Loop2.py
# Please enter the frequency : 0
# Invalid number