story = "a quick brown fox jumps over a lazy little dog"

# string Functions
print(len(story)) #returns length of the string
print(story.endswith("kjirjir")) #returns false
print(story.endswith("dog")) #returns true
print(story.count("a"))
print(story.count("fox"))
print(story.capitalize())
print(story.find("fox")) #tells the first occurance of the word or chahrcater in the string
print(story.replace("fox","Lion"))

#escape sequences
#examples : \n \t \\ (escaping backslash )
story2 = "prologue : It all started with rain, \\ \'\tShailaja was so tired of the scorching summer she decided to move to Banglore.\nEver since her best friend moved to the city she had had begging her to come to banglore"
print(story2)
