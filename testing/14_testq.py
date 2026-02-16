# code question 14

# Write your code here.
def validate_id(ID: str):
    result = ""
    if len(ID) == 8 and ID[0:3].isalpha() and ID[0:3].isupper() and ID[3:8].isdigit():
        return bool(1)
    else:
        return bool(0)

# You may alter the code below to test your solution or print help documentation.
# Only the validate_id function will be graded for this assessment.

#print(validate_id("jJ333333"))
# help(help)
#---
