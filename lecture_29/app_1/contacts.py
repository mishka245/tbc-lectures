class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"""Name: {self.name}
Phone: {self.number}
Email: {self.email}"""

    def to_dict(self):
        return {
            "name": self.name,
            "number": self.number,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict.get("name"),
            number=data_dict.get("number"),
            email=data_dict.get("email"),
        )

