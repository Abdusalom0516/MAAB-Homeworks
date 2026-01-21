from abc import ABC, abstractmethod
from .note import Note
import json 

class Storage(ABC):
    @abstractmethod
    def save(self, notesList: list[Note]) -> None:
        pass

    @abstractmethod
    def load(self) -> list[Note]:
        pass

    @property # That helps me to turn method to the field and we can use it like this "object.info".
    @abstractmethod
    def info(self) -> dict[str, str]:
        pass


class JSONFile(Storage):

     def __init__(self, file_name: str):
         super().__init__()

         self.file_name = file_name


     def save(self, notesList: list[Note]) -> None:
        print(f"{len(notesList)} notes saved into file {self.file_name}.")
        listOfJSONNotes: list[dict[str, str]] = []

        for note in notesList:
            listOfJSONNotes.append(note.to_json())

        with open(self.file_name, "w") as f:
            json.dump(listOfJSONNotes, f, indent=4)


     def load(self) -> list[Note]:
        list_of_notes = []

        with open(self.file_name, "r") as f:
            json_value = json.load(f)

            for value in json_value:
                list_of_notes.append(Note.from_json(value))

        return list_of_notes


     def info(self) -> dict[str, str]:
        return {"file_name": self.file_ame}



class CSVFile(Storage):

     def __init__(self, file_name: str):
         super().__init__()

         self.file_name = file_name


     def save(self, notesList: list[Note]) -> None:
        print(f"{len(notesList)} notes saved into file {self.file_name}.")

     def load(self) -> list[Note]:
        return [Note(id=1, text= "Read book", date_created="2026-01-11"), Note(id=2, text= "Learn Python", date_created="2026-01-12")]

     def info(self) -> dict[str, str]:
        return {"file_name": self.file_ame}