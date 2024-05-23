class Employee:
    def __init__(self, name, email):
        # Encapsulation
        self.name = name
        self.email = email
        self.__test_var = "test_value"

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def capitalised_name(self):
        return self._name.capitalize()

    @name.setter
    def name(self, val):
        if len(val) < 3:
            raise ValueError("Name too short")
        self._name = val

    @email.setter
    def email(self, val):
        if val.count("@") != 1:
            raise ValueError("Incorrect email")
        self._email = val

    def __str__(self):
        return f"{self._name} - {self._email}"


def main():
    e2 = Employee("w", "goga123@mail.com")
    print(e2)


if __name__ == "__main__":
    main()
