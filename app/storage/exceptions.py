from dataclasses import dataclass


@dataclass
class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return "Произошла ошибка приложения."


