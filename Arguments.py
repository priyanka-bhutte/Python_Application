# end = " " is a keyword argument
# Types of arguments

# 1 : Positional argument
# 2 : keyword argument
# 3 : Default argument
# 4 : Variable number of argument

def Information(Name, Age, Salary):
    print("Name is : ", Name)
    print("Age is :", Age)
    print("Salary is : ", Salary)

# 1 : Positional argument
# Position of argument matters
Information("Amit",32,90000)
Information("Pooja",29,70000)

# 2 : keyword argument
# Position of argument doen't matter , name of the variables used in function matters here
Information(Age = 31, Salary = 78000, Name = "Sagar") # Inthis case your should know the name of varible used while accepting values in function

