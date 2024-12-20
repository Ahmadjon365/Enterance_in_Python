# Closures

# global
a = 4


def f1():
    print(a)


def f2():
    global a
    a += 1


# local
def f3():
    a = 4
    print(a)


def f4():
    a = 4

    def f1():  # inner function
        print(a)  # nonlocal
