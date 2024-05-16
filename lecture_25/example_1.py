employees = [
    {
        "name": "John",
        "surname": "Doe",
        "age": 25,
        "salary": 50000
    },

]

# version 2
employees = [
    ["John", "Doe", 25, 50000],
    ["Jane", "Doe", 30, 60000],
]


def print_employee(l):
    print(l[0], l[1])
