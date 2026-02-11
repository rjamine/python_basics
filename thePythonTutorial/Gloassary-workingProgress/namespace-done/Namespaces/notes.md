# This file captures reflections, questions, practice notes, and wtf moments from the python environment and exercises
This file contains material copied from the Python documentation: [https://docs.python.org/3.11/tutorial/]

 © Copyright 2001-2025, Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.

--- 

## Definition

The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions builtins.open and os.open() are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing random.seed() or itertools.islice() makes it clear that those functions are implemented by the random and itertools modules, respectively.
