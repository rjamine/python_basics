# Python Learning/Fun Notes

This file captures reflections, questions, practice notes, and wtf moments from python exercises.

--- 

## General Notes 


---

## OS specifics: Debian GNU/Linux 12 (bookworm)
- don't remove apt package python3, I crashed and corrupted my gdm3 + i3 session, had to reinstall both in root shell. I was thought python3 was an older version of python3.11 and removed it, not fun. Learned a couple neat commands though: 
  1. 'apt show $python3' (a bunch of nice metadata about the package like source, priority, provides/depends, etc.,) 
  2. 'apt-cache depends --important $packagename' ($packagename depends on the packages listed) 
  3. 'apt rdepends $packagename' (reverse depends: the packages listed depend on $packagename
- From the 'apt show $packagename' metadata, if its anything at or above 'optional' be wary.

--- 

## Editor and Tools that make this possible and fun: 

1. Emacs
 - python major mode
 - lsp (python hook)

--- 

## Designer and History

### Designer: Guido van Rossum
 - name origin: monty python the flying circus TV show
 - python captures the essence of community driven development where everyone's voice is heard just like the cast of a Monty Python sketch. Its all about bringing people together, laughing at jokes and growing together as a global community. - some article by some guy I forgot that I will have to track down and give credit too. 


---

## Python Interpreter 


--- 



*Created by RJ Amine - Cloud and Network Engineering Student, IT & Networking Enthusiast* 
