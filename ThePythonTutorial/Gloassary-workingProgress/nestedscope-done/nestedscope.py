scope = "will be called third"

def  outer():
     scope = "will be called seccy"

     def inner():
         #scope = "will be called first"
         print(scope)
         
     inner()

outer()     

