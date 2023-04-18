def outer(arg1):
    def inner(arg2):
        return arg1 + arg2
    return inner

i10 = outer(10)

result = i10(4)

print(result)


def hello(func):
    print('hello')

def add(a,b):
    return a+b


