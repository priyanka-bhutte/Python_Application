
def Addition(*No):
    Ans = 0
    print(type(No))
    print(len(No))
    
    for i in No:
        Ans = Ans + i

    return Ans

Result = Addition(10,20,30)
print(Result)

Result = Addition(10,20,30,40)
print(Result)

Result = Addition(10,20,30,40,50)
print(Result)

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\20-04-2024>python variable.py
# 60
# 100
# 150