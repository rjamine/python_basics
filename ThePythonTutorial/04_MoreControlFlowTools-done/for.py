feelings = ['sad', 'hurt', 'horny']
# iterates items/indexs of any sequence in the order they appear 
for feeling in feelings:
    print(feeling)

# for leveloffedup in range(7, 10):
#     print(leveloffedup)

levelsoffedup = ['unbothered', 'annoying', 'dont play with me', 'your getting smacked', 'were throwing hands']
for i in range(len(levelsoffedup)):
    print(i, levelsoffedup[i], "\n")

for thisiscringe in range(0, 6):
    if thisiscringe == 0:
        print("level of cringe:", thisiscringe, "- not so bad")
    elif thisiscringe == 1:
        print("level of cringe:", thisiscringe, "- ew")
    elif thisiscringe == 2:
        print("level of cringe:", thisiscringe, "- facepalm")
    else:
        print("level of cringe:", thisiscringe, "- cant watch this anymore")

for num in range(2, 10):
    if num % 2 == 0:
        print("found an even number", num)
        continue
    print("found and odd number", num)

class MyEmptyClass:
    pass

def empytfunc():
    pass

