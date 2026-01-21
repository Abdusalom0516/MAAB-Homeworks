from __future__ import annotations
from datetime import datetime

from .note import Note
from .storage import Storage


class Notebook:
    notes_list: list[Note]
    __storage: Storage

    def __init__(self, storage: Storage):
        self.__storage = storage
        self.notes_list = self.__storage.load()

    @classmethod
    def add_note(cls, note: Note) -> None:
        pass

    @classmethod
    def update_note(cls, *, new_note: Note) -> None:
        pass

    @classmethod
    def delete_note(cls, *, note_id: int) -> None:
        pass

    @classmethod
    def get_notes(cls) -> list[Note]:
        # NOTE: Dummy Implementation
        return [Note(id=999, text="Damn man...", date_created=datetime.now()), Note(id=777, text="Fuck that...", date_created=datetime.now())]

    @classmethod
    def get_note(cls, *, note_id: int) -> Note:
        # NOTE: Dummy Implementation
        return Note(id=999, text="Damn man...", date_created=datetime.now())