class Employee:
    def __init__(self, name, email):
        # Encapsulation
        self._name = name
        self._email = email
        self.__test_var = "test_value"

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def set_name(self, val):
        if len(val) < 3:
            raise ValueError("Name too short")
        self._name = val

    def set_email(self, val):
        if val.count("@") != 1:
            raise ValueError("Incorrect email")
        self._email = val

    def __str__(self):
        return f"{self._name} - {self._email}"


def main():
    e1 = Employee("Goga", "goga123@mail.com")
    print(e1.get_email())
    # e1.set_email("newmail.com")
    e1.set_email("new@mail.com")
    print(e1.get_email())


if __name__ == "__main__":
    main()
