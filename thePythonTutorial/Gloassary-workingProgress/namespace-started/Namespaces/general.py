# namespace areas: local, global, built-in, nested in object methods

scope = "will be called third"

def  outer():
     scope = "will be called seccy"

     def inner():
         #scope = "will be called first"
         print(scope)
         
     inner()

outer()     

