hinToEng = {
    "kya" : "what",
    "kaise" : "how",
    "kidhar" : "where",
    "kyun" : "why",
    "kab" : "when"
}

print("options are", hinToEng.keys())
user = input("enter the hindi word you wnat to translate")
print(hinToEng.get(user))


favLang = {}

a = input("enter your fav lang neeti")
b = input("enter your lang sonu")
c = input("enter you fav lang rams")
favLang["neeti"] = a
favLang["sonu"] = b
favLang["rams"]= c
print(favLang)