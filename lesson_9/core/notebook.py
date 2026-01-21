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

    def add_note(self, note: Note) -> None:
        self.notes_list.append(note)

        self.__storage.save()


    def update_note(self, *, new_note: Note) -> None:
        for i in range(len(self.notes_list)):
            if self.notes_list[i].id == new_note.id:
                self.notes_list[i] = new_note
                break

        self.__storage.save()


    def delete_note(self, *, note_id: int) -> None:

        for i in range(len(self.notes_list)):
            if self.notes_list[i].id == note_id:
                self.notes_list.pop(i)
                break

        self.__storage.save()


    def get_notes(self) -> list[Note]:
        return self.notes_list


    def get_note(self, *, note_id: int) -> Note:
         for i in range(len(self.notes_list)):
            if self.notes_list[i].id == note_id:
               return self.notes_list[i]