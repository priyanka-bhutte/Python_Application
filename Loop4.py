def Display(count):
    i = 0
    if(count <= 0):
        print("Invalid number")
        return

    while(i < count):
        print("Jay Ganesh...",end = " ")
        i = i + 1

def main():
    Cnt = int(input("Please enter the frequency : "))
    Display(Cnt)

if __name__ =="__main__":
    main()

# C:\Users\Priyanka\Desktop\Python_2024\20-04-2024>python Loop4.py
# Please enter the frequency : 5
# Jay Ganesh... Jay Ganesh... Jay Ganesh... Jay Ganesh... Jay Ganesh...