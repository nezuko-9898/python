x = lambda a,b : a + b
print(x(2,3))


def myfun(n):
    return lambda a: a - n
my= myfun(3)

print(my(1))


def my(n):
    return  lambda b: b -n
m= my(2)
print(m(2))