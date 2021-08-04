# #use the open function to read the content of the file, by default the mode is r
# # open (filename, mode)
# f = open ('c:/Serverless/pythonbasics/File input output/sample.txt','r')
# #data = f.read() #read the contents
# data = f.read(5) # read first five characters
# print(data)
# f.close() # close file

#other methods to read a file
f = open('c:/Serverless/pythonbasics/File input output/sample.txt','r')
data = f.readline() #read first line
print(data)
data = f.readline() # read second line and so on 
print(data)
data = f.readline()
print(data)

#diffrent modes to open a file r,w,a(append),+(update)
#wrintig files

# f = open('c:/Serverless/pythonbasics/File input output/newfile.txt','w') #if there is anything in the file it ll be overwritten
# f.write("write this into file")
# f.close()


f = open('c:/Serverless/pythonbasics/File input output/sample.txt','a') #if there is anything in the file it ll be overwritten
f.write("and she likes to stay happy")
f.close()

#with statement
#if we use this no need to close the file it ll be done automatically
with open('c:/Serverless/pythonbasics/File input output/newfile.txt', 'r') as f:
    a = f.read()
print (a)