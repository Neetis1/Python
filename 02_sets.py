a = {1,2,3,4,1,1,5}
print(type(a))
print(a)
#empty set 
#this will create an empty dictionary not an empty set 
#b = {} # empty dict

#an empty set can be created using the below syntax
a = set() 
print(type(a))

#methods
a.add(23)
a.add(12)
# a.add([1,2,3,4,4]) # unhashable type error (cannnot add because list can be modified ) also cannot add dictionary
a.add((1,4,5,6,7,7)) # llowed tuple bcz ttuple is immutable
print(a) 

# cannot access elemts using index 
print(len(a)) # prints the length of the set
a.remove(23) # removes 23 fromm set 
print(a)
# if we try to remove an elemnt which doesnt exist it will throw an error element not presnt in the set 
a.pop() # removes an element from the set (random value)
print(a)

#another important methods is set.intersection() and set.union() hope the name implies wat it does


