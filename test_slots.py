
class Person(object):
    # __slots__ = ("age", "name")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print "Person eat"


class Animal(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def run(self):
        print "animal run"


@staticmethod
def walk():
    print "this is walk"


P = Person("tom", 10)
Person.walk = walk
Person.walk()
print vars(P), P.__dict__
delattr(P, "name")
print vars(P)
