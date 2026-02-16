# code question 14

# Write your code here.
def validate_id(ID: str):
    IDlength = len(ID)
    IDisaLetter = ID[0:3].isalpha()
    IDisUppercase = ID[0:3].isupper()
    IDisDigit = ID[3:8].isdigit()
#    if len(ID) == 8 and ID[0:3].isalpha() and ID[0:3].isupper() and ID[3:8].isdigit():
    if IDlength == 8 and IDisaLetter and IDisUppercase and IDisDigit: 
        return bool(1) 
    else:
        return bool(0) 

# You may alter the code below to test your solution or print help documentation.
# Only the validate_id function will be graded for this assessment.

print(validate_id("JJJ33333"))
# help(help)
#---

