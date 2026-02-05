import tokenize

with open("source.py", "rb") as f:
    for token in tokenize.tokenize(f.readline):
        print(token)
