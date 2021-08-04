#program 1 
#read from a file and find if it cntains sometings

# a = open ('c:/Serverless/pythonbasics/File input output/newfile.txt','r')
# contents = a.read()
# if("Neeti" in contents):
#     print("Yes ")
# else:
#     print("No")

# a.close() # very important

# def game():
#     return 190

# #did this cz it will allow to open either read or in wrte mode this will open and close 
# with open ('c:/Serverless/pythonbasics/File input output/newfile.txt','r') as f :
#     highScore = f.read()

# currScore = game()
# if(int(highScore) < currScore or highScore == ""):
#     with open ('c:/Serverless/pythonbasics/File input output/newfile.txt','w') as f :
#         f.write(str(currScore))

words = ["donkey","motu","patlu","kaddu", "pagal"]

with open ("c:/Serverless/pythonbasics/File input output/newfile.txt",'r') as f :
    content = f.read()
for word in words:
        content = content.replace(word,"######")

with open ("c:/Serverless/pythonbasics/File input output/newfile.txt",'w') as f :
    f.write(content)