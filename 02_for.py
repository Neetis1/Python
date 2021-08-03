#for loop syntax
l1 = [1,2,3,4,5,6,7]
for i in l1:
    print(i,"\n")

#range function
for i in range(8):  
    print(i) # prints 0 to 7 (n-1)
    
for i in range(2,8):  
    print(i) # prints 2 to 7 (n-1)

for i in range(2,8,2):   #adding step size 2   
    print(i) # prints 0 to 7 (n-1)

#for with else 
for i in range(8):  
    print(i) # prints 0 to 7 (n-1)
else:
    print("Done")

#for loop breaK

for i in range(8):  
    print(i) # prints 0 to 7 (n-1)
    if i == 5:
        break       #we also have continue and pass (null statement in python (says to do nothing ))
else:
    print("Done")  #runs only when for loop executed completely if break this ll not b executed

