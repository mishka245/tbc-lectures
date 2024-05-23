class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class CanFly:
    def fly(self):
        print("I can fly!")


class CanSwim:
    def swim(self):
        print("I can swim!")


class Bird(Animal, CanFly):
    def speak(self):
        return "Chirp!"


class Duck(Animal, CanFly, CanSwim):
    def speak(self):
        return "Quack!"


# Example usage:
bird = Bird("Sparrow")
print(bird.species)
print(bird.speak())
bird.fly()

duck = Duck("Mallard")
print(duck.species)
print(duck.speak())
duck.fly()
duck.swim()
