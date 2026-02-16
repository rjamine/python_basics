# code question 7
def format_rgb(rgb):
    # Write your code here.
    formatted = f"rgb({','.join(map(str, rgb))})"
    return formatted

# You may alter the code below to test your solution or print help documentation.
# Only the format_rgb function will be graded for this assessment.

rgb_sample = [255, 165, 13]
#print(format_rgb(rgb_sample))
# help(help)
#---
x = "string"
print(f"hello mate ({','.join(map(str, rgb_sample))})")
