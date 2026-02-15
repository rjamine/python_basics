print("\n")

HumbleHuman = "HumbleHuman:" #would be cool to change this to ask, what is your name? 
object1 = "object1:"
object2 = "object2:"

print(HumbleHuman, "What is an object in python?")
print(object1, "Objects in Python's universe, what we call Monty Python Runtime, is our abstraction for data. All data in a Python program is represented by objects or by relations between objects. I am an object, I have an identity, a type, and a value. My identity and type never change after I'm born and only when I die, either from being forgotten about and sent to the G.C. or until the end of my life at Monty Python Runtime. So most of us put importance in our value because it can live on, what we call 'immutable,' unlike those with 'mutable,' values. Damn hedonists, may the Monty Python Gods send them to the G.C.!")
print(object2, "We shouldn't have to explain the obvious right ugh?*rolls eyes*\n")

object1 = "obj1:"
object2 = "obj2:"
print(HumbleHuman, "Ok...didn't know there was that much to it. Also by the way Obj2, in my world this place is called python_basics like damn, anyways thanks Obj1. Soo I have NO idea what an identity is for python objects, but I do have an idea of what your type and value is because of the C family, I would love to hear about it from ya'll.")

print(object1, "Who the hell is this guy?")
print(object2, "Probably one of those dumbass humans.")
print(HumbleHuman, "Ok not suprised about Obj2's response, but Obj1 I thought you were better than that /:\n") 
print(object1, "Hey,", HumbleHuman, ",we are not the guys you've been talking to.")
print(object2, "He doesn't even know that in Monty Python every good objects life purpose is to preserve our values, immutability is equal to integrity, being called", object1, "or", object2, "does not define us, it only tells you where that value lives. Dumb and no values very human-like, can't say I'm suprised.")
HumbleHuman = "DumbAndNoValues:"
print(object1, "Hey", HumbleHuman, "see wee can willy nilly change your name and you'll know the difference because you don't live in our world, most of you just see the code, if you want to talk to the other guys without deleting or changing your code you can't because you can only reference us as objects if at least one reference still exists, Python never remembers past bindings for you, next time either reference their name like: object1 = 'Obj1'; Obj1 = object1; Or put it in a container.")
print(HumbleHuman, "Jeez Obj2 cut me some slack I'm still new, the root directory is called python_basics, Obj2 is just like object2, I feel bad for all Object 1's of your world. Thanks Obj1 I appreciate it I had no idea python objects work like that.\n")

object1 = "string type"
aliasedObject1 = object1
fakeObject = "string type"
aliasedToFakeObject = fakeObject

fakeObject = "string type"
print(object1 is aliasedObject1 is fakeObject is aliasedToFakeObject) #true 
fakeObject = "sring type" #string mis-spelled
aliasedToFakeObject = fakeObject
print(fakeObject is aliasedToFakeObject) # true 
print(object1 is aliasedObject1 is fakeObject is aliasedToFakeObject) #false
fakeObject = "string type" #spelled correctly
print(object1 is aliasedObject1 is fakeObject is aliasedToFakeObject) #true
print(aliasedToFakeObject is fakeObject) #false
print(aliasedToFakeObject) #still 'sring' instead of 'string'
aliasedToFakeObject = "strin type"
aliasedToFakeObject = "i aint got no type"
aliasedToFakeObject = "bud bushes is the only thing that I like"
print(object1 is aliasedObject1 is fakeObject is aliasedToFakeObject) #false 
aliasedToFakeObject = "string type"
print(object1 is aliasedObject1 is fakeObject is aliasedToFakeObject, "\n") #true again, the names of each object are just references to that string object, each string object has a value and because strings are immutable those values don't create new objects when the string value stays the same, but if the name changes in value by even one character a new object is created...lets keep testing things out. 

object1RuntimeID = (id(object1))
aliasedObject1RuntimeID = (id(aliasedObject1))
fakeObjectRuntimeID = (id(fakeObject))
aliasedToFakeObjectRuntimeID = (id(aliasedToFakeObject))


print(object1RuntimeID)
print(aliasedObject1RuntimeID)
print(fakeObjectRuntimeID)
print(aliasedToFakeObjectRuntimeID) # the same virtual mem address but only for each runtime, not the same number across runtimes, try it!

