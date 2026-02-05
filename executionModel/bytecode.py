from ASTparse import source

code = compile(source, filename="source.py", mode="exec")
print(code)

import dis
dis.dis(code)
