#create a list using []
a = [1,2,3,56,8]
#print a list
print(a)
#assignement
#we can modify the contents the list (we coudnt do this in strings)
a[1] = 99
print(a[1]) 
#we can create a list with items of diffrent types
c = [29, "Neeti", True,100]
print (c)

#list slicing
friends = ["neeti","sonu","dewanshu","moni","ramu",45]
print(friends[0:4])
print(friends[0:5:2])
print(friends[-4:-1])
print(friends[-4:])

#list methods
print(type(friends))
l1 = [1,8,7,4,21,15]
# l1_sorted = l1.sort() #in our case list itself is getting sorted so no need to do this 
# print(l1_sorted)
#sorts the list
l1.sort()
print(l1)
#reveses the list 
l1.reverse()
print(l1)
#appends at the end of the list
l1.append(45)
print(l1)

#inserts at the particular index
l1.insert(5,434)
print(l1)

#will delete the elememt at the index
l1.pop(4)
print(l1)
l1.remove(434)
print(l1)