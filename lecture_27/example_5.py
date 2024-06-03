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

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
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

    # manager_2.compare(manager_1)
    # self = manager_2
    # other = manager_1
    def compare(self, other: "Manager"):
        if not isinstance(other, Manager):
            raise ValueError("Only Manager class object is allowed")
        max_employee_manager = max(self, other, key=lambda x: len(x.employees))

        return max_employee_manager

    def __str__(self):
        return f"Manager - {self.fullname}, Employees - {len(self.employees)}"


def main():
    dev_1 = Developer("Nino", "Tonia", 10000, "C++")
    dev_2 = Developer("Giorgi", "Beridze", 1000, "C++")
    manager_1 = Manager("Giga", "Liparteliani", 1500, None)
    manager_2 = Manager("Manana", "Nunua", 1500, None)
    manager_1.add_employee(dev_1)
    manager_1.add_employee(dev_2)
    manager_2.add_employee(dev_1)

    result = manager_2.compare(manager_1)
    print(result)


if __name__ == "__main__":
    main()
