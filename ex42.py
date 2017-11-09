class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ##??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ##??
        self.name = name


## ??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of same kind
        self.pet = None
