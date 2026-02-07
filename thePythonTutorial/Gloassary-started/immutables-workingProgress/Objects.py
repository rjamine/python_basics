print("\n")
print("The dumb but humble human: What is an object in python?\n")

object1 = "object1: We are objects, we have an identity, type, and value. Our identity and type never change for the most part but our values can be either mutable or immutable."
object2 = "object2: I shouldn't have to explain the obvious right?*rolls eyes*"

print(object1)
print(object2, "\n")

print("The dumb but humble human: Ok thanks obj1 and obj2, soo I have NO idea what an identity is for python objects, but I do have an idea of what your type and value is, I would love to hear about it from ya'll.\n")

object1_identity = "obj1: My identity is my memory address, its where I come from and live at runtime, not compile time. For you humans it would be like where you were born/ethnic background, that can't be changed, it stays the same until you die. Even if, for example, after you died someone were born in the same place with the same ethnic background and same name, that wouldn't be you right?" 
object2_identity = "obj2: Ok so since your'e giving us nicknames willy nilly the 'dumb and humble human's' new name is 'dumbass"


memAddress_Obj1 = id(object1_identity)
memAddress_Obj2 = id(object2_identity)
print("\n")
print("Does object1 have the same identity as object2? True or False?", "\n")
print("Object 1's identity is:", memAddress_Obj1)
print("Object 2's identity is:", memAddress_Obj2, "\n")
print(object1_identity is object2_identity,"an objects identity/mem address is permanent at runtime but not across compiles.\n") 

object1_type = type(object1_identity)
object2_type = type(object2_identity)

print("What about an objects type?")
print("Object 1's type is:", object1_type)
print("Object 2's type is:", object2_type, "\n")

print("An objects type is also permanent at runtime but unlike its identity the type stays the same across compiles")
