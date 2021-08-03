#problem 1
# num = int(input("enter the number"))

# for i in range(1,11) :
#     #print(str(num) + "x" + str(i) + "=" + str(i*num) )
#     #using fstrins
#     print(f"{num}X{i} = {num*i}")

#problme 2

# l1 = ["ssweetie","ritu","shiela","rohit","saina"]
# for i in l1:
#     if i.startswith("s"):
#         print("hello " + i)
#     else:
#         pass

# problem 3
# num = int(input("Num"))
# for i in range(2,num):
#     if(num%i == 0 and num!= 2):
#         print("not prime")
#         break
# else:
#     print("PRIME NUMBER IT IS ")

# print('DONE')

#program 4 
#sum of n natural numbers
# n = int(input("enter the num"))
# i=0
# sum =0
# while i<= n:
#     sum += i
#     i +=1
# print(sum,"\n")

#program 6
#factorial

# n = int(input("num"))
# fact =1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

#program 7 
#print pTTERN 
#*
#**
#***
#****
for i in range (5):
    print("*"*i)
    
num = int(input("enter the number"))
i =10
while i>=1:
    print(str(num) + "x" + str(i) + "=" + str(i*num) )
    i -=1
    

