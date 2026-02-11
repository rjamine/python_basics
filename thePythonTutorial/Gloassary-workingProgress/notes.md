# This file captures reflections, questions, practice notes, and wtf moments from the python environment and exercises.
This file contains material copied from the Python documentation: [https://docs.python.org/3.11/tutorial/]

 © Copyright 2001-2025, Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.

---
## General Notes 
- All information was taken from: https://docs.python.org/3.11/glossary.html#glossary and: https://docs.python.org (quick search) and: https://docs.python.org/3.11/reference/index.html 

---
## Terms in the Gloassary 

### immutable 
	An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.
### namespace 
    The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions builtins.open and os.open() are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing random.seed() or itertools.islice() makes it clear that those functions are implemented by the random and itertools modules, respectively.
### annotation/type hinting
A label associated with a variable, a class attribute or a function parameter or return value, used by convention as a type hint.

Annotations of local variables cannot be accessed at runtime, but annotations of global variables, class attributes, and functions are stored in the __annotations__ special attribute of modules, classes, and functions, respectively.

An annotation that specifies the expected type for a variable, a class attribute, or a function parameter or return value.

Type hints are optional and are not enforced by Python but they are useful to static type checkers. They can also aid IDEs with code completion and refactoring.

Type hints of global variables, class attributes, and functions, but not local variables, can be accessed using typing.get_type_hints().
