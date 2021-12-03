class DomainException(Exception):
    pass


class CustomBaseException(Exception):
    error_message: str

    def __init__(self, error_message: str) -> None:
        super().__init__(error_message)
        self.error_message = error_message


class BadRequestException(CustomBaseException):
    pass


class NotFoundException(CustomBaseException):
    pass
