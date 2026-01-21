from abc import ABC, abstractmethod
from .note import Note

class Storage(ABC):
    @abstractmethod
    def save(self, notesList: list[Note]) -> None:
        pass

    @abstractmethod
    def load(self) -> list[Note]:
        pass

    @property
    @abstractmethod
    def info(self) -> dict[str, str]:
        pass