from dataclasses import dataclass


@dataclass
class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return "Произошла ошибка приложения."


@dataclass
class BadDataException(ApplicationException):
    errors: dict

    @property
    def message(self) -> str:
        return "Данные некорректны."
