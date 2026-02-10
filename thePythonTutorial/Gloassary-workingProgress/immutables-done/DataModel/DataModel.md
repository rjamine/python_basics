# Data Model (only mentioning things related to immutables) 
This file contains material copied from the Python documentation: [https://docs.python.org/3.11/tutorial/]

 © Copyright 2001-2025, Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.

- [Python Documentation Used:](https://docs.python.org/3.11/reference/datamodel.html#index-17) 

## 3.1. Objects, values, and types

"Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. (In a sense, and in conformance to Von Neumann’s model of a “stored program computer”, code is also represented by objects.)

Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The is operator compares the identity of two objects; the id() function returns an integer representing its identity.

CPython implementation detail: For CPython, id(x) is the memory address where x is stored.

An object’s type determines the operations that the object supports (e.g., “does it have a length?”) and also defines the possible values for objects of that type. The type() function returns an object’s type (which is an object itself). Like its identity, an object’s type is also unchangeable. [1]" 

---

## 3.2. The standard type hierarchy - numbers.Number, Immutable sequences (strings, tuples, and byte objects), set types, frozen sets, and code objects
## 3.3. Special method names - basic customization (_new_, object._hash_(self) hashable collections key's hash value)
