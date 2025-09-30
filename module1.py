def add(n1,n2):
    return n1 + n2


def sub(n1,n2):
    return n1 - n2


def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    if n2 == 0:
        raise ZeroDivisionError('Can not divide by zero')
    return n1 /n2

    