import tokenize, io, ast, dis, sys

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

# We can inspect the bytecode of the string object to easier see when it 'becomes' an object and how much an object costs 

print("Bytecode object address of 'stringliteral':", code, "bytes")
print("Bytecode object:", code.co_code, "Size:", len(code.co_code), "bytes")
print("Constants:", code.co_consts, "Size:", len(code.co_consts), "bytes")
print("Name:", code.co_names, "Size:", len(code.co_names), "bytes")
print("String Object Runtime Address:", id(stringliteral), "Size:", len(stringliteral), "bytes")
print("'String Object + metadata:", sys.getsizeof(stringliteral), "bytes")

# Above printing output: 
# Bytecode object address of 'stringliteral': <code object <module> at 0x7fdefa957ec0, file "Objects", line 1> bytes
# Bytecode: b'\x97\x00d\x00Z\x00d\x01S\x00' Size: 10 bytes
# Constants: ('object1', None) Size: 2 bytes
# Name: ('stringliteral',) Size: 1 bytes
# String Object Runtime Address: 140595663307632 Size: 7 bytes
# 'String Object + metadata: 56 bytes

# Now I'm still new to python, so maybe my wording is wrong somewhere, but it still shows that before runtime at tokenization and AST parsing an 'object' is still just data to use for compilation, you can clearly see a 'name' and 'type,' but no id/identity because the object does not exist, and when it is compiled into bytecode you can see the instructions like LOAD_CONST and STORE_NAME which each cost 1-2 bytes, and by pythons own definition in its spec "every object has an identity, a type, and a value," and we can see that you can't do this: 
# print(id(x))
# x = "does this run"
# because the potential string object "does this run" does not exist until its executed and once its executed it lives somewhere in memory with an address.
