# end = " " is a keyword argument
# Types of arguments

# 1 : Positional argument
# 2 : keyword argument
# 3 : Default argument
# 4 : Variable number of argument

# 3 : Default argument
def Area(Radius, PI = 3.14):
    Result = PI * Radius * Radius
    return Result

Ans = Area(10.7)
print("Area of circle is : ",Ans)

# Here 7.20 gets overrrieds the default value 3.14
Ans = Area(10.7,7.20)
print("Area of circle is : ",Ans)

# Here we can say keyword argument while calling function
Ans = Area(Radius = 10.7)
print("Area of circle is : ",Ans)


# # Default argument should be at the 

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\20-04-2024>python Default.py
# Area of circle is :  359.49859999999995
# Area of circle is :  824.3279999999999
# Area of circle is :  359.49859999999995