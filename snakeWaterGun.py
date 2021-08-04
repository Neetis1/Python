import random
def game(a,b):
    if(  a == "S" and b == "W"):
        return "you loose"
    elif(a == "S" and b == "G"):
        return "you win"
    elif(a == "W" and b == "S"):
        return "you win"
    elif(a == "W" and b == "G"):
        return "you loose"    
    elif(a == "G" and b == "W"):
        return "you win"
    elif(a == "G" and b == "S"):
        return "you loose"
    elif(a == b):
        return "Tie "
    else:
        return "incorrect option"

print("computer : Snake(S) water(W) Gun(G)")
randNo = random.randint(1,3) #gives random numbers between 1 -3
if randNo == 1:
    a = "S"
elif randNo == 2:
    a = "W"
else:
    a = "G"

b = input("your turn : Snake(S) water(W) Gun(G)")

winner = game(a,b)
print("computer : " + a + " you : " + b + " ---- " + winner)