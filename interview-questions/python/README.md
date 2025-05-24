# Python Interview Questions

### Q1. Package vs Module
|Feature|Module|Package|
|-------|------|-------|
|Definition|single file with python code|directory with multiple modules and '\_\_init\_\_.py'|
|Usage|Group related code|Structured organization of large codebase|
|import|import math|from mypackage import math|

### Q2. Python is compiled or interpreted?
Partially Compiled -> python code is converted to bytecode.
Interpreted -> line by line bytecode execution by an interpretor.

### Q3. Python language advantages as a tool
1. Simplicity -> easy to read and write
2. Versatility -> can be used in various fields
3. Extensive Libraries and Frameworks -> Django, Pandas, Tensorflow, FastAPI, Flask
4. Strong Community Support
5. Portability -> Platform Independent
6. Development Speed
7. Dynamic Typing
8. Opensource

### Q4. Global, Protected & Private attributes
Global variables are public variable. To use a global variable inside a function, the global keyword is required
```python
x = 10
def someFunction():
    global x
    x += 10
someFunction()
print(x) // should print 20
```
Protected variables are marked with single underscore. While they still can be accessed outside the class, its the developers responsibility to avoid doing so.
```python
class Apples:
    def __init__(self):
        self._apple = 10
a = Apples()
a._apple # can be accessed but shouldn't be accessed. 
```
Private variables have double underscore. They as well can be accessed outside the class.
```python
class Apples:
    def __init__(self):
        self.__apple = 10
a = Apples()
a.__apple # can be accessed but shouldn't be accessed. 
```
Python isn't strict like Java and C++ regarding variable accessibility. We just use standard practices that's it.

### Q5. Is python variables case sensitive
Yes

### Q6. How to do Exception Handling in Python
```python
def divide(a, b):
    try:
        return a / b
    except e:
        print(e)
    finally:
        return None
```
In the above case, we expect an error to happen if b is zero. Because you cannot divide anything with zero. So we wrapped the code which can result into error, in a try except block.

The ``try`` will try it. In case the error is thrown, the ``except`` will catch it and do something with it, and then the ``finally`` block will do the clean up work, returning ``None`` in this case.

### Q7. For vs While
You iterate over something using for loop. You iterate as long as a condition is true using while loop
```python
for i in range(10):
    print(i)
i = 0
while i < 10:
    print(i)
    i += 1
```

Different ways of for loop
```python
for item in [1, 2, 3]:
    pass
for char in "string":
    pass
for i in range(10): # 0 to 10 excluding 10
    pass
for i in range(1, 10): # 0 to 10 excluding 10
    pass
for i in range(10, 0, -1): # 10 to 0 excluding 0
    pass
for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    pass
myd = {"a": 1, "b": 2}
for key in myd: # iterating over keys
    pass
for key, value in myd.items(): # iterating over key and value
    pass
for index, value in enumerate(["a", "b", "c"]):
    pass
numbers = [1, 2, 3]
characters = ["a", "b", "c"]
for number, character in zip(numbers, characters):
    pass

# Creating array
squares = [x*x for x in range(10)]

# Copying 2d array
squares = [[x for x in row] for row in originalArray]

# Looping over file lines
with open("file.txt") as f:
    for line in f:
        print(line.strip())
```

Different ways of while loop
```python
# Infinite While
while True:
    pass

# Condition
while i < 5:
    pass

# clean up after while
i = 0
while i < 5:
    i += 1
else:
    i = 0
```
Bonus: with blocks are used to create a contextual block where you want to operate with a variable.
```python
file = open("file.txt", "r")
print(file.read())
```
This can be written as
```python
with open("file.txt", "r") as file:
    print(file.read())
```

Some other usecases of with
```python
# Copy files
with open('in.txt') as infile, open('out.txt', 'w') as outfile:
    outfile.write(infile.read())
```

```python
# With for locking (Thread-safe)
from threading import Lock
lock = Lock()
with lock:
    print("Locked")
```

```python
# Database Connection
import sqlite3
with sqlite3.connect('my.db') as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER)")
```

With can be used with classes only if they have \_\_enter__ and \_\_exit__ methods defined. The enter method should usually return ``self`` i.e. the class itself so that it could be initialized to a variable as seen below.

```python
class MyResource:
    def __enter__(self):
        print("Acquiring resource")
        return self  # <- critical
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
    def use(self):
        print("Using resource")

with MyResource() as resource:
    resource.use()
```

In the lock example, the Lock() class does not have the above two methods and hence we initialized it outside and then used it as ``with lock:``

### Q8. ``self`` in python
``self`` is basically ``this`` keyword as compared to other languages.

### Q9. Garbage Collection
1. Python uses reference counting to track object references and automatically deallocates objects with zero references.
2. Garbage Collector handles cyclic references and recycles unused memory to free up space.

### Q10. Multiple Inheritance is supported
Yes

### Q11. Memory Management
1. Python uses a private heap space where all objects and data structures are stored.
2. Programmers cannot access heap as python interpreter manages it.
3. Garbage Collector frees up unused memory for future use

### Q12. How python sorts using `sort()` and `sorted()`
Tim sort, a hybrid of merge and insertion sort, which has worst case of O(N log N)

### Q13. How to do multithreading
using threading module. 

### Q14 Inheritance in Python

### Q15. Shallow copy vs deep copy

### Q16. pass, continue and break

### Q17. Type conversion in python

### Q18. pass by value / reference

### Q19. built in modules

### Q20. range vs xrange

### Q21. *args and **kwargs

### Q22. Generators in python

### Q23. Global Interpreter Lock

### Q24. pip