def func(x):
   print(x)

# default arguments that become obligatory when you call them (score)
# keyword arguments that become optional when you call them (failed, passed, exceeded)
# position of function parameters does not matter unless enforced 
def pass_or_fail_test(score, failed=79, passed=80, exceeded=81):
   for num in range(0, 79):
       if score == num:
           print("you failed:", num)
           break
       elif score == failed:
           print("you were so close:")
           break 
   if score == 80:
       print("just passed:", passed)
   for num in range(82, 100):
       if score == num:
           print("look at you big dawg high achiever:", num)
           break
   if score == exceeded:
       print("did a bit better than average nice:", exceeded)

# a clearer example, try putting whatever in the func arg call       
def jokes(name, joke, /, *, blutofjoke="netanyahu", **status):
    print("-- What does", joke, "rhyme with", name, "?")
    for num in blutofjoke:
        print(num)
    for kw in status:
        print(kw, ":", status[kw])

jokes("bubba", "lying ahh", status="im not suicidal") #works just fine 
# jokes("partna", "liar", "netanyahu", "im not suicidal") does not run, **keyword syntax enforces dict form so you need key=value

def hotness_scale(name="rj", **hotness):
   for name in range(0, 10):
      print(name)
   for num in hotness:
     print(num, ":", hotness[num]) 
#    for num in scaling:
#       print(scaling[num])

hotness_scale("rj", hotness="0")
