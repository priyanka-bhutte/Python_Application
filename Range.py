#range (start, end, displacement)
# start is by default 0 if not mentioned
# displacement is by default 1 if not mentioned 
# end should be mentioned explicitelly (It is excluded)

print(list(range(5))) # start is 0 by default, displacement is 1 by default and end is 5
# [0, 1, 2, 3, 4]

print(list(range(3,8)))  #3 should be start and 8 should be end and displacement will be by default is 1
#[3, 4, 5, 6, 7]

print(list(range(3,12,2))) # start is 3, displacement is 2 and end is 12
#[3, 5, 7, 9, 11]

print(list(range(20,1,-1)))
#[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]