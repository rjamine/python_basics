# Python Learning/Fun Notes

This file captures reflections, questions, practice notes, and wtf moments from the python environment and exercises.

--- 

## General Notes 


---

## OS specifics: Debian GNU/Linux 12 (bookworm)
1. Mistakes:
  - don't remove apt package python3, I crashed and corrupted my gdm3 + i3 session, had to reinstall both in root shell. I thought python3 was an older version of python3.11 and removed it, not fun. Learned a couple neat commands though (note: none of this is necessary after recovering your machine state, but I had an itch I needed to scratch for a couple hours) **sad face**: 
  - 'apt show $packagename' (a bunch of nice metadata about the package like source, priority, provides/depends, etc.,) 
  - 'apt-cache depends --important $packagename' ($packagename depends on the packages listed) 
  - 'apt rdepends $packagename' (reverse depends: the packages listed depend on $packagename
  - From the 'apt show $packagename' metadata, if its anything at or above 'optional' be wary and get ready for regex/confusion + answers.
  - So I ran the above commands to get the dependencies of gdm3 (my display manager), and what packages depend on python3 and stored that output to **gdm3Dependencies.txt** and **python3Provides.txt**.
  - The goal is to see **IF** gdm3 has a/some package(s) that python3 depends on, so we need the **comm** command, literal man output: **comm - compare two sorted files line by line** 
  - In order for comm to work you need any characters or whitespace to be reomved before the first character, and for it to be sorted with the **sort** command, an example of **apt-cache** or **apt rdepends** output thats not ok for **comm** even after sorting with **sort**:
	1. Depends: gnome-session-bin
	2. Depends: <x-terminal-emulator>
	3.    alacritty
  - So we do some **sed** and **regex** magic, '**cat** python3Provides.txt | **sed** 's/^[[:space:]]*[A-Za-z]\+:[[:sapce:]]*//g; s/^[[:space:]]*//' > python3Provides_sed.txt, and then do the same to gdm3Dependencies.txt
  - Then, '**sort** python3Provides_sed.txt > python3Provides_sorted.txt, and then do the same to gdm3Dependencies_sed.txt
  - Finally, **comm** -1 -2 --total python3Provides_sorted.txt gdm3Dependencies_sorted.txt, you literally get a clean list of all the packages that are similar, -1 (don't include file 1 output that are not matches) -2 (don't include file 2 ouput that are not matches) --total (a summary: 142 (file 1 different files) 2813 (file 2 different files) 7 (matched files) total.
  - So yes, now I know how to check, maybe I'll write a script that checks for me in the future.
  
2. OS Python package management
  - Debian apperentley uses python3 as a 'metapackage' to install the latest stable python interpreter and/or any other version you want/need, and other GNU/Linux distros may do it differently, and other OS's defintley do it differently, I think its kind of clever.
3. Maintainer: Matthias Klose doko@debian.org
   - As of version 3.11.2-1+b1
   - He is also part of the python software foundation since 2009 I think.
--- 

## Editor and Tools that make this possible and fun: 

1. Emacs
 - python major mode
 - lsp (python hook)

--- 

## Designer and History

### Designer: Guido van Rossum
1. 
 - name origin: monty python the flying circus TV show
 - python captures the essence of community driven development where everyone's voice is heard just like the cast of a Monty Python sketch. Its all about bringing people together, laughing at jokes and growing together as a global community. - some article by some guy I forgot that I will have to track down and give credit too. 


---

## Python Interpreter 

1. Python's Design Documentation Evolution: 
   - PEP 339: Cpython Compiler https://peps.python.org/pep-0339/
   - PEP 511: API for code transformers (bytecode transformers) https://peps.python.org/pep-0511/
   - PEP 659: Specializing Adaptive Interpreter 3.11+ https://peps.python.org/pep-0659/
   - PEP 523: Adding a frame evaluation API to CPython (custom evaluation loop) https://peps.python.org/pep-0523/
   - etc.,
2. Execution Model:
   - Python source (.py) > Bytecode (.pyc or whatever your VM implentation does: platform independent) > PVM (Python Virtual Machine) > Native Machine Instructions (interpreted at runtime)
3. Virtual Machine Alternatives (all follow the python language spec):
   - Cpython
   - PyPy
   - Jython (Python on the JVM: Java)
   - IronPython (Python on .NET)
   - MicorPython (Virtual Machine optimized for microcontrollers/embedded)
   - Nuitka (ahead-of-time compiler not a Virtual Machine)
4. Debian ships with python3: CPython's execution pipeline: 
   - .py source > AST (parser) > Bytecode (.pyc in __pycache__) > Cpython VM (ceval loop in C) > Native Machine Instructions
--- 



*Created by RJ Amine - Cloud and Network Engineering Student, IT & Networking Enthusiast* 
