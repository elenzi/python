"""define f as (x)
in f print x+= 1 and y = 1 a = 3 and b = 4
print x
print y
print z
return x
set a, b, x, y, z = 3, 4, 5, 10, 15
c = a * b
print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
z = f(x)
print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
print("b is", b)
z = f(x)
print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("c is", c)


"""


def f(x):
    print("In function f:")
    x += 1
    y = 1
    a = 3
    b = 4
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return x
a, b, x, y, z = 3, 4, 5, 10, 15
c = a * b
print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
print("b is", b)
z = f(x)
print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("c is", c)

"""
Before function f:
x is 5
y is 10
z is 15
a is 3
b is 4
In function f:
x is 6
y is 1
z is 15
After function f:
x is 5
y is 10
z is 6
c is 12
"""
