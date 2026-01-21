from .note import Note

class Notebook:

    def __init__(self, notesList: list[Note] = []):
        self.notesList = notesList

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