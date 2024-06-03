
from lecture_29.app_1.io_handling import FileHandler
from lecture_29.app_1.manager import ContactManager


class Operator:

    def __init__(self):
        self.file_handler = FileHandler()
        self.contact_manager = ContactManager.from_dict(self.file_handler.read_contacts())
        self._operation = -1

    def start(self):
        while True:
            self.display_operations()
            if self._operation == "1":
                self.contact_manager.display_contacts()
            if self._operation == "2":
                self._add_contact()
            if self._operation == "3":
                print("Coming soon!!! support - supporttbcacademy@mail.com")
            if self._operation == "4":
                self._delete_contact()
            if self._operation == "5":
                self.file_handler.write_contacts(self.contact_manager.to_dict())
                break
            if self._operation == "6":
                break

    def display_operations(self):
        while True:
            print("1. Display contacts")
            print("2. Add contact")
            print("3. Update contact")  # skip for now
            print("4. Delete contact")
            print("5. Save changes and exit")
            print("6. Exit")
            operation = input("Enter operation number: ")
            operation = operation.strip()
            if operation in ("1", "2", "3", "4", "5", "6"):
                break
            print("Please enter valid operation number")
        self._operation = operation

    def _add_contact(self):
        # todo add validations here
        name = input("Please enter user name")
        number = input("Please enter user name")
        email = input("Please enter user name")
        self.contact_manager.add_contact(name, number, email)

    def _delete_contact(self):
        while True:
            contact_index = input("Please enter contact index")
            contact_index = contact_index.strip()
            success, message = self.contact_manager.delete_contact(contact_index)
            if success:
                break
            else:
                print(message)


if __name__ == "__main__":
    app = Operator()
    app.start()
