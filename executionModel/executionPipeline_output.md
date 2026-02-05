# Simple Python Execution Pipeline with real code output
---
## Execution Pipeline Summary 

1. .py files > tokens 
2. tokenized .py files > parsed into an AST tree
3. AST tree built > bytecode .pyc/code object that CPython (or other VM) can use
4. bytecode.pyc > C-based bytecode interpreter-CPython (or other Virtual Machine thats not JIT like PyPy) 
5. CPython > pre-compiled C-code that interprets bytecode into native machine instructions

---

## source.py output

x = int(2 + 3) 
print(x)

---

## tokenization.py output

TokenInfo(type=63 (ENCODING), string='utf-8', start=(0, 0), end=(0, 0), line='')
TokenInfo(type=1 (NAME), string='import', start=(1, 0), end=(1, 6), line='import builtins\n')
TokenInfo(type=1 (NAME), string='builtins', start=(1, 7), end=(1, 15), line='import builtins\n')
TokenInfo(type=4 (NEWLINE), string='\n', start=(1, 15), end=(1, 16), line='import builtins\n')
TokenInfo(type=62 (NL), string='\n', start=(2, 0), end=(2, 1), line='\n')
TokenInfo(type=1 (NAME), string='x', start=(3, 0), end=(3, 1), line='x = int(2 + 3) \n')
TokenInfo(type=54 (OP), string='=', start=(3, 2), end=(3, 3), line='x = int(2 + 3) \n')
TokenInfo(type=1 (NAME), string='int', start=(3, 4), end=(3, 7), line='x = int(2 + 3) \n')
TokenInfo(type=54 (OP), string='(', start=(3, 7), end=(3, 8), line='x = int(2 + 3) \n')
TokenInfo(type=2 (NUMBER), string='2', start=(3, 8), end=(3, 9), line='x = int(2 + 3) \n')
TokenInfo(type=54 (OP), string='+', start=(3, 10), end=(3, 11), line='x = int(2 + 3) \n')
TokenInfo(type=2 (NUMBER), string='3', start=(3, 12), end=(3, 13), line='x = int(2 + 3) \n')
TokenInfo(type=54 (OP), string=')', start=(3, 13), end=(3, 14), line='x = int(2 + 3) \n')
TokenInfo(type=4 (NEWLINE), string='\n', start=(3, 15), end=(3, 16), line='x = int(2 + 3) \n')
TokenInfo(type=1 (NAME), string='print', start=(4, 0), end=(4, 5), line='print(x)\n')
TokenInfo(type=54 (OP), string='(', start=(4, 5), end=(4, 6), line='print(x)\n')
TokenInfo(type=1 (NAME), string='x', start=(4, 6), end=(4, 7), line='print(x)\n')
TokenInfo(type=54 (OP), string=')', start=(4, 7), end=(4, 8), line='print(x)\n')
TokenInfo(type=4 (NEWLINE), string='\n', start=(4, 8), end=(4, 9), line='print(x)\n')
TokenInfo(type=0 (ENDMARKER), string='', start=(5, 0), end=(5, 0), line='')

---

## ASTparse.py output 

Module(
  body=[
    Assign(
      targets=[
        Name(id='x', ctx=Store())],
      value=BinOp(
        left=Constant(value=2),
        op=Add(),
        right=Constant(value=3))),
    Expr(
      value=Call(
        func=Name(id='print', ctx=Load()),
        args=[
          Name(id='x', ctx=Load())],
        keywords=[]))],
  type_ignores=[])
Module(
  body=[
    Assign(
      targets=[
        Name(id='x', ctx=Store())],
      value=BinOp(
        left=Constant(value=2),
        op=Add(),
        right=Constant(value=3))),
    Expr(
      value=Call(
        func=Name(id='print', ctx=Load()),
        args=[
          Name(id='x', ctx=Load())],
        keywords=[]))],
  type_ignores=[])
  
---

## bytecode.py output 

<code object <module> at 0x7f3c97e056f0, file "source.py", line 1>
  0           0 RESUME                   0

  2           2 LOAD_CONST               0 (5)
              4 STORE_NAME               0 (x)

  3           6 PUSH_NULL
              8 LOAD_NAME                1 (print)
             10 LOAD_NAME                0 (x)
             12 PRECALL                  1
             16 CALL                     1
             26 POP_TOP
             28 LOAD_CONST               1 (None)
             30 RETURN_VALUE
