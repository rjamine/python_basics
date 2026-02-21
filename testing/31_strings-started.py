
toggled = [["enabled", "disabled"], ["enabled", "disabled"], ["disabled"]]

def toggle_state(*string):
    result = []
    for one in string:
        for i in one:
            for (index, char) in enumerate(i):
                if char == "enabled":
                    i[index] = "disabled"
                elif char == "disabled":        
                    i[index] = "enabled"
                else:
                    print("you did something wrong")
            result.extend(map(str, i))
            newstring = ', '.join(result)
        return newstring 
print(toggle_state(toggled))

dictObject = {"mom" : "stephanie", "sister" : "karen", "brother" : "kevin"}

def toggle_dict(convert):
    for (i, char) in enumerate(convert):
        print(i, map(str, char))
toggle_dict(dictObject)
     
