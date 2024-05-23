class Animal(object):
    def __init__(self, age, color=None):
        self.age = age
        self.color = color
        self.leg_count = -1

    def speak(self):
        raise NotImplemented("Must be implemented in sub classes")

    def info(self):
        print("My age is", self.age)
        if self.color is not None:
            print("My color is ", self.color)


class Person(Animal):
    def __init__(self, age):
        super().__init__(age)
        self.leg_count = 2

    def speak(self):
        print("hello")


class Horse(Animal):
    def __init__(self, age, color):
        super().__init__(age, color)
        self.leg_count = 4

    def speak(self):
        print("whews")


class Centaurus(Horse, Person):
    def __init__(self, age, color):
        super().__init__(age, color)
        self.leg_count = 4


p = Person(10)
p.info()
p.speak()

h = Horse(4, "Black")
h.info()
h.speak()
