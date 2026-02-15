
# Technically called a 'compound data type,' because its used to group together other values 
# Lists are built-in type and mutable 'sequences - iterable which supports element access using integer indicies'
# Kind of like arrays except they accept different types 

mrKrabs = [1, 2, 3, 4, 5] # single type
# print("I love money I have:", mrKrabs, "dollars")
 
spondgebob = ["yellow", "square", 666] # mixed type str and int 
# print("Spondgebob has the following features:", spondgebob) 

# print("Spondgebob is the color", spondgebob[0], "and has the mark of the", spondgebob[2], "beast") # index them starting at 0 like arrays 

print("Mr Krabs lost his money and is looking everywhere help wheres me money", mrKrabs[-3:]) # slicing works with index 1, 1:4, -1:, etc.,
mrKrabsLostMoney = [1 , 2]
mrKrabs = [3, 4, 5]
mrKrabsFoundHisMoney = mrKrabsLostMoney + mrKrabs
mrKrabsOtherPocket = mrKrabs + [1, 2]
print("Look at me other pockets its filled with cash heiheihei", mrKrabsOtherPocket)
print("Its literally sticking out of your pocket you crabby bastard", mrKrabsFoundHisMoney)
mrKrabs = [] # makes an empty list 

# print("Mr Krabs has no money look at his wallet lol:", mrKrabs)

# even though string objects are immutable you can concatentate them together like this because they are 'sequence types,' thus you can do most iterable operations 
# mrKrabs = "immutable greedy crab"
# mrKrabsReformed = "immutable not greedy crab"
# 
# newMrKrabs = mrKrabs + mrKrabs
# print(newMrKrabs)

# does not work because the string object with its iterable characters are unchangeable/immutable
# but if mrKrabs = [1, 2, 3] and you do mrKrabs[0] = "broke", that will work because lits are mutable
# print(ReformedmrKrabs)
# mrKrabs[0] = "L"

squidward = ["eggplant nose", "full of himself"]
print("Squidward has the following qualities:", squidward)
# list/sequence support the append operation 
squidward.append("horrible claronet player")
print(" Oh i forgot he's also a", squidward[2]) 
