# namespace areas: local, global, built-in, nested in object methods
import ast

# builtinNamespace = dir()
# print(builtinNamespace)

globalNameSpace = "i am a string object bound to a global name"

x = ast.dump.__globals__ # where the dump function namespace is   
y = ast.__dict__ # all names of ast including 'dump' 
print('dump' in x) #true  
print(x is y) # true

globalnum = 1

def f():
    localnum = 1
    print(locals())

f()
print(globals())
