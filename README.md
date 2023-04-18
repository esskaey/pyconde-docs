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
   
#### Advanced Decorators

- Decorators with arguments

```python
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
# hello
# bye
# 9
```

- Callable ?

