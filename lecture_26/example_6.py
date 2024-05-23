class Employee:
    def __init__(self, name, email):
        # Encapsulation
        self._name = name
        self._email = email
        self.__test_var = "test_value"

    def __str__(self):
        return f"{self._name} - {self._email}"


def main():
    e1 = Employee("Goga", "goga123@mail.com")
    print(e1.email)
    e1.email = "new@mail.com"
    # print(e1._Employee__test_var)  # DO NOT DO THIS THING
    print(e1.email)


if __name__ == "__main__":
    main()
