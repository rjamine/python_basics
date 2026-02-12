morning = "morning"
afternoon = "afternoon"
sunset = "sunset" 

x = str(input("want coffee? what time of day is it( morning | afternoon | sunset ): "))
if x == morning:
    print("Ok have one cup")
elif x == afternoon:
    print("Ok have another itll help get things moving")
elif x == sunset:
    print("No more coffee your brain is burnt")
else:
    print("You spelled something wrong dumb dumb")
    
#execute script on cli 
