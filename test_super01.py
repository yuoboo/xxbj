# encoding=utf8


class A(object):
    def __init__(self):
        print("Enter A")
        print("Leave A")


class AA(object):
    def __init__(self):
        print("enter aa")
        print("leave aa")


class B(A):
    def __init__(self):
        print("Enter B")
        super(B, self).__init__()
        print("Leave B")


class C(A):
    def __init__(self):
        print("Enter C")
        super(C, self).__init__()
        print("Leave C")


class D(AA):
    def __init__(self):
        print("Enter D")
        super(D, self).__init__()
        print("Leave D")


class E(B, C, D):
    def __init__(self):
        print("Enter E")
        super(E, self).__init__()
        print("Leave E")


E()  # 公共父类不会被重复执行,
print(E.mro())

# EBCDAADCBE

a = (4, 5, 6)
b = (1,) + a[1:]
print b


class Parent1(object):
    def __init__(self):
        print('enter p1')
        print('leave p1')


class Parent2(object):
    def __init__(self):
        print("enter p2")
        print("leave p2")


class C1(Parent1):
    def __init__(self):
        print("enter c1")
        super(C1, self).__init__()
        print("leave C1")


class C2(Parent2):
    def __init__(self):
        print("enter C2")
        super(C2, self).__init__()
        print("leave C2")


class C3(Parent1):
    def __init__(self):
        print("enter C3")
        super(C3, self).__init__()
        print("leave C3")


class C4(C1, C2, C3):
    pass


C4()
print (C4.mro())
