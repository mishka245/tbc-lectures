class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"Animal: {self.name}, {self.age}"


class Person(Animal):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name
        self.friends = []

    def get_friends(self):
        return self.friends

    def print_friends(self):
        for f in self.friends:
            print(f)

    def add_friend(self, friend):
        self.friends.append(friend)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print(f"Age diff between {self.name} and {other.name} {abs(diff)}")

    def __str__(self):
        return f"person, {self.name}, {self.age}"


def main():
    person_1 = Person(33, "Gocha")
    person_2 = Person(44, "Nino")
    person_3 = Person(55, "Alexander")
    person_1.add_friend(person_2)
    person_1.add_friend(person_3)
    person_1.print_friends()
    person_1.speak()

    person_2.age_diff(person_3)


if __name__ == "__main__":
    main()
