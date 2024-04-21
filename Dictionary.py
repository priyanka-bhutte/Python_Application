print("Demonstration of Dictionary")

Price = {"Python" : 2000, "Java" : 1500, "C" : 1100, "C++" : 3000, "Java" : 4300}

print(Price)

print(type(Price))

print(Price["C"]) #Key -value pair

print(Price.keys()) # get all the keys frm dictionary

print(Price.values()) # get all the values from dictionary

#Output:
# C:\Users\Priyanka\Desktop\Python_2024\21-04-2024>python Dictionary.py
# Demonstration of Dictionary
# {'Python': 2000, 'Java': 1500, 'C': 1100, 'C++': 3000}
# <class 'dict'>
# 1100
# dict_keys(['Python', 'Java', 'C', 'C++'])
# dict_values([2000, 1500, 1100, 3000])