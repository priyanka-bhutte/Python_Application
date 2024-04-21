def Display(count):
    i = 0
    if(count <= 0):
        print("Invalid number")
        return

    for i in range(count):
        print("Jay Ganesh...",end = " ")

def main():
    Cnt = int(input("Please enter the frequency : "))
    Display(Cnt)

if __name__ =="__main__":
    main()

# C:\Users\Priyanka\Desktop\Python_2024\20-04-2024>python Loop3.py
# Please enter the frequency : 4
# Jay Ganesh... Jay Ganesh... Jay Ganesh... Jay Ganesh...