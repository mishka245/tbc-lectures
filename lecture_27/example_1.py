class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@email.com"
        self.salary = salary

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.programming_language = prog_lang


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
            print("-->", e.fullname())
