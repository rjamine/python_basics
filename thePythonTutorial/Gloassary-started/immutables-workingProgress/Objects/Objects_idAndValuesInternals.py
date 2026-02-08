import tokenize, io

stringliteral = 'object1 = object1'

tokens = tokenize.generate_tokens(io.StringIO(stringliteral).readline)
for tok in tokens:
    print(tok)
    
