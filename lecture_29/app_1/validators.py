class Validator:

    @staticmethod
    def _valid(data):
        """
        Collect all common validations here, for example comparing with None
        """
        return data is not None

    def valid(self, data: str) -> bool:
        raise NotImplemented("Must be implemented in all subclasses")


class PhoneNumberValidator(Validator):
    """
    length must be more than 8 and less than 15, Only numbers.

    """

    def valid(self, data: str) -> bool:
        if not self._valid(data):
            return False
        if len(data) >= 15 or len(data) <= 8:
            return False
        if not data.isalpha():
            return False

        return True


class EmailValidator(Validator):
    """
    length must be more than 5 and less than 25. @ symbol must be present.

    """

    def valid(self, data: str) -> bool:
        if self._valid(data):
            return False
        if len(data) >= 25 or len(data) <= 5:
            return False
        # if "@" not in data:
        #     return False
        if data.count("@") != 1:
            return False
        return True
