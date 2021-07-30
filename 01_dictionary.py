myDict = {
    "fast" : "in a quick manner",
    "neeti" : "A developer",
    "marks" : [1,2,4],
    "myDict2" : {
        "neeti" : "gamer",
        "love" : "frienship"
    },
    1: 2
}

# print(myDict["Fast"])
# print(myDict["Neeti"])
# print(myDict["marks"])
# print(myDict["myDict2"])
# print(myDict["myDict2"]["neeti"])
# print(myDict["myDict2"]["love"])

#dict are mutable (can be changed)
myDict["marks"] = [20,90,333]
print(myDict["marks"])

#methods in dicts

print(myDict.keys()) # prints the keys of the dict
print(list(myDict.keys()))
print(myDict.values()) # prints values of the dict 
print(myDict.items()) # gets the dicts key: value for all contents of the dict in a tuple format 
updateDict = {
    "what" : "awesome",
    "marks" : [1,1,1],
    "neeti" : "teacher"
}
myDict.update(updateDict) # updates the dict with aupplied key: value pairs
print(myDict)

print(myDict.get("neeti"))
#diffrece between get and fetching the value through [] is that when we use get if the key isnt present it returns None
# but in we use [] it throws an error "key not present" better to use get 
