from .note import Note
from .storage import Storage

class Notebook:
    notes_list: list[Note]

    def __init__(self, storage: Storage ):
        self.__storage = storage
        self.notes_list = self.__storage.load()

    @classmethod
    def add_note(cls, note: Note) -> None:
        pass

    @classmethod
    def update_note(cls) -> None:
        pass

    @classmethod
    def remove_note(cls) -> None:
        pass

    @classmethod
    def get_notes(cls) -> list[Note]:
        pass

    @classmethod
    def get_note(cls) -> Note:
        pass