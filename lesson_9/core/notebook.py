from .note import Note

class Notebook:

    def __init__(self, notesList: list[Note] = []):
        self.notesList = notesList

    @classmethod
    def addNote(cls, note: Note) -> None:
        pass

    @classmethod
    def updateNote(cls) -> None:
        pass

    @classmethod
    def removeNote(cls) -> None:
        pass

    @classmethod
    def getNotes(cls) -> list[Note]:
        pass

    @classmethod
    def getNote(cls) -> Note:
        pass