from datetime import datetime
from typing import Tuple, List

from lecture_29.app_1.contacts import Contact


class ContactManager:
    def __init__(self):
        self._contacts: List[Contact] = []

    def add_contact(self, name: str, number: str, email: str) -> Tuple[bool, str]:
        c = Contact(name, number, email)
        self._contacts.append(c)
        return True, "Contact added successfully"

    def delete_contact(self, _id: str) -> Tuple[bool, str]:
        if not _id.isdigit():
            return False, "Invalid contact id"
        _id = int(_id)
        if _id >= len(self._contacts):
            return False, "Invalid contact id"
        if _id < 0:
            return False, "Invalid contact id"
        self._contacts.pop(_id)
        return True, "Contact deleted successfully"

    def update_contact(self, _id: str, **kwargs) -> Tuple[bool, str]:
        raise NotImplemented("Not implemented yet")

    def display_contacts(self):
        for i, c in enumerate(self._contacts):
            print(f"#: {i}")
            print(c)

    def to_dict(self) -> dict:
        return {
            "modified_at": datetime.utcnow().isoformat(),
            "contacts": [c.to_dict() for c in self._contacts]
        }

    @classmethod
    def from_dict(cls, data):
        result = cls()
        for c_dict in data.get("contacts", []):
            result._contacts.append(Contact.from_dict(c_dict))

        return result
