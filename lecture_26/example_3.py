class Animal:
    def __init__(self, age):
        self.age = age
        self.leg_count = -1

    def speak(self):
        raise NotImplemented("Must be implemented in sub classes")

    def info(self):
        print("My age is", self.age)


class Person(Animal):
    def __init__(self, age):
        super().__init__(age)
        self.leg_count = 2

    def speak(self):
        print("hello")


class Horse(Animal):
    def __init__(self, age):
        super().__init__(age)
        self.leg_count = 4

    def speak(self):
        print("whews")


p = Person(10)
p.info()
p.speak()

h = Horse(4)
h.info()
h.speak()
