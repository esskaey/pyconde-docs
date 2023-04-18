# pyconde-decorators

## Motivation

### Why do we need decorators ?

Code injection - Aspect oriented programming

### What is aspect oriented programming ?

What is a closure ?
 A multilevel function (function inside a function)?

#### Basics of decorators

1. Decorators gets the function being called as arguments
2. The decorator is usually wrapped using a decorator

```python
from functools import wraps
```
3. Defining a decorator
```python
import functools

def hello(func):
 @functools.wraps(func)
 def wrapped(*args,**kwargs):
  print("Do something here")
  func(*args, **kwargs)
  return func
 return wrapped(func)

@hello
def add(a,b)
 return a + b
```

4. Usecases
   1. Logging
   2. Caching
   3. Checking pre-requisites before calling func
   
#### Advanced Decorators

- Decorators with arguments

```python
from functools import wraps

def say(text):
   def _say(func):
      @wraps(func)
      def __say(*args, **kwargs):
         print(text)
         return func(*args, **kwargs)
      return __say
   return _say

@say('hello')
def add(a,b):
   return a + b

# result
# hello
# 9
```

- Applying multiple decorators

```python
@say('hello')
@say('bye')
def add(a,b):
   return a + b

# result
# add(5,4)
# hello
# bye
# 9
```

- Callable ?
  -  implements dunder '__call__()'  
  
- using a decorator class

  ```python
  class Say:
   def __init__(self,text):
      self.text = text
   
   def __call__():
      # place the say method code here 


   @Say('Hello')
   def add(a,b):
      return a + b 
   
   # result for add(5,4) 
   # Hello
   # 9
  ```
#### Class Decorators

- Basic setup

  ```python
  def mark(cls):
      # do something ( inspect )
      cls.new_attr = 100
      return cls
  
  @mark
  class A:
   pass

  # test
  # A.new_attr
  ```


