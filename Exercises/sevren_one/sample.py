from logcall import logged
from validate import Integer, validated

@logged
@validated
def add(x, y):
    return x + y


@logged
@validated
def sub(x, y: Integer):
    return x - y


if __name__ == '__main__':
    sub(1,2)
    sub(1, '4')