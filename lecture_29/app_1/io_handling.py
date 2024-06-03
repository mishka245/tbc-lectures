import json
from pathlib import Path


class FileHandler:
    store_path: Path = Path("./contacts.json")

    def read_contacts(self):
        if not self.store_path.exists():
            return {}
        with open(self.store_path, "r") as f:
            return json.load(f)

    def write_contacts(self, data: dict):
        with open(self.store_path, "w") as f:
            json.dump(data, f)
