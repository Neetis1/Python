
# greeting = "Good Morning "
# name = 'Neeti' #string is sequence of characters
# print(type(name))
# #concatinating 2 strings
# print(greeting + name)


name = "Neeti"
# print(name[0])

# # name[3] = "a"   -->this isnt allowed strings element cannot be modified 
# #string slicing 
# print(name[0:3])  #last index is excluded 
# print(name[1:4])
# print(name[:4]) # if first index is not given it will take 0th index as default same applies to if end index is not given 
# #negitive indexing 0  1  2  3  4
# #                 -5 -4 -3 -2 -1
# #useful when we want to retrieve the last element of any container
# print(name[-4:-1])
# #slicing with skip value

# print(name[0:5:1])  #prints NEETI since step value is one 
# print(name[0:5:2])  #skips every 2nd value NEI

greeting = "Good Morning"
print(greeting[0::2])