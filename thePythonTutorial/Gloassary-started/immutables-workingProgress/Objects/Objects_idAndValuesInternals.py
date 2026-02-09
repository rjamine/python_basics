import tokenize, io, ast, dis

stringliteral = "object1"

tokens = tokenize.generate_tokens(io.StringIO('stringliteral = "object1"').readline)
for tok in tokens:
    print(tok)

# Actual tokenization output as if it were to come from the string object 'string literal' above:
# TokenInfo(type=1 (NAME), string='stringliteral', start=(1, 0), end=(1, 13), line='stringliteral = "object1"')
# TokenInfo(type=54 (OP), string='=', start=(1, 14), end=(1, 15), line='stringliteral = "object1"')
# TokenInfo(type=3 (STRING), string='"object1"', start=(1, 16), end=(1, 25), line='stringliteral = "object1"')
# TokenInfo(type=4 (NEWLINE), string='', start=(1, 25), end=(1, 26), line='')
# TokenInfo(type=0 (ENDMARKER), string='', start=(2, 0), end=(2, 0), line='')
# So far we have a type and name, both necessary to make a python object, but no ID and nothing that can be operated on, just text to feed the AST parsing

tree = ast.parse('stringliteral = "object1"')
print(ast.dump(tree, indent=2), "\n")

# Actual output of Abstract Syntax Tree (step after tokenization) from the same text above: 'stringliteral = "object1"'  
# Module(
#   body=[
#     Assign(
#       targets=[
#         Name(id='stringliteral', ctx=Store())],
#       value=Constant(value='object1'))],
#   type_ignores=[])

code = compile(tree, filename="Objects", mode="exec")
dis.dis(code)
# Actual output from 'code' compiling into a bytecode object and disassembling it into their instructions:
#   0           0 RESUME                   0
# 
#   1           2 LOAD_CONST               0 ('object1')
#               4 STORE_NAME               0 (stringliteral)
#               6 LOAD_CONST               1 (None)
#               8 RETURN_VALUE
# Notice how LOAD_CONST mentions the "value," and STORE_NAME mentions the name binding/reference, but no type, becaue in python 'object1' is implied to be a string and you can see that after looking at the AST parse and the '' characters, you can mess around with what tree = ast.parse('x = 5 + 9') for example and see what happens with the output

# we can 

print("Code Object:", code)
print("Byte size:", len(code.co_code))
print("Bytecode:", code.co_code)
print("Constants:", code.co_consts)
print("Names:", code.co_names)
