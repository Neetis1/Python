#creating a tuple () 
#diffrenece between tupl,e and list is tuple cannot be updated 
t = (1,2,3,4,5,1,1,1,1,1)
print(t[0])

#cannot update tuple
#t[0] = 34 # will give error
#tupls are immutable  (caanot change)

# t1 = () #empty tuple
t11 = (1) # not a tuple this ll be a number 
t1 = (1,) # tuple with single element 
print(t11,t1)

#tuple methods 
print(t.count(1)) #counts the elemt
print(t.index(1)) #gives 1st index of the element
