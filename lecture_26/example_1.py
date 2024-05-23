"""
შევქმნათ მონაცემთა სტრუქტურა სტეკი  - Stack

Last in First Out - LIFO

[]
insert 23 - [23]
insert 25 - [23, 25]
insert 27 - [23, 25, 27]
pop element - 27 - [23, 25]
pop element - 25 - [23]

"""


class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def insert(self, new_element):
        self.elements.append(new_element)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")

        return self.elements.pop(-1)


my_stack = Stack()
# print(my_stack.pop())  # Raises value error
my_stack.insert(10)
my_stack.insert(25)
my_stack.insert(33)

print(my_stack.pop())
print("left in stack ", my_stack.elements)
