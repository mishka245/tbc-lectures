
# კლასი / ტიპი
# ობიექტი
# ობიექტს გააჩნია ატრიბუტები, მაგალითად, name
class Employee:
    version = 1

    def __init__(self, n, s, a, salary):
        self.name = n
        self.surname = s
        self.age = a
        self.salary = salary

    def info(self):
        print(self.name, self.surname, self.version)


# ობიექტის შექმნა
emp1 = Employee("Goga", "Mindia", 33, 100)
emp1.info()
emp1.name = "ChangedName"
emp1.info()
emp2 = Employee("New", "Jhon", 33, 100)
emp2.info()

Employee.version = 2
emp3 = Employee("Nino", "Mindadze", 28, 1000)
emp3.info()



