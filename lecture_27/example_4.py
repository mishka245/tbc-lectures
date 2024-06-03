class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, prog_lang, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = prog_lang

    def compare(self, other: "Developer"):
        if not isinstance(other, Developer):
            raise ValueError("Only Developer class object is allowed")
        if self.salary > other.salary:
            max_salary_dev = self
        else:
            max_salary_dev = other

        print("Max salary dev is ->", max_salary_dev.fullname)


class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []

    def add_employee(self, e):
        if e not in self.employees:
            self.employees.append(e)
            return True
        return False

    def remove_employee(self, e):
        if e in self.employees:
            self.employees.remove(e)
            return True
        return False

    def print_employees(self):
        for e in self.employees:
            print("-->", e.fullname)


def main():
    dev_1 = Developer("C++", first="Nino", last="Tonia", salary=10000)
    dev_2 = Developer("C++", first="Giorgi", last="Beridze", salary=1000)
    dev_1.compare(dev_2)


if __name__ == "__main__":
    main()
