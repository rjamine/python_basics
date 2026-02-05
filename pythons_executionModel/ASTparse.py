import ast  

source = """
x = 2 + 3
print(x)
"""

tree = ast.parse(source)
print(ast.dump(tree, indent=2)) 
