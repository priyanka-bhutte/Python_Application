# List datatype

# Heterogeneous
# UnOrdered
# UnIndexed
# Mutable
# Duplicates are not allowed

Arr = {11,78.90, True, "Marvellous",11}
print(Arr)
print(len(Arr))

#print(Arr[0]) # Not allowed because set is unindexed

Arr.add("Python") # set is mutablt
print(Arr)

Arr.remove("Python")
print(Arr)

# Output:
# C:\Users\Priyanka\Desktop\Python_2024\21-04-2024>python Set.py
# {'Marvellous', True, 11, 78.9}
# 4
# {'Marvellous', True, 'Python', 11, 78.9}
# {'Marvellous', True, 11, 78.9}