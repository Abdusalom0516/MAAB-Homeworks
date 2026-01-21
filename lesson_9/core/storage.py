from abc import ABC, abstractmethod
import os
from .note import Note
import json
import csv

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
        print("Saved ✅")
        listOfJSONNotes: list[dict[str, str]] = []

        for note in notesList:
            listOfJSONNotes.append(note.to_json())

        with open(self.file_name, "w") as f:
            json.dump(listOfJSONNotes, f, indent=4)


     def load(self) -> list[Note]:
        list_of_notes = []

        if not os.path.exists(self.file_name):
            return list_of_notes
        
        if os.path.getsize(self.file_name) == 0:
            return list_of_notes

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
        print("Saved ✅")

        with open(self.file_name, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "text", "date_created"])
            writer.writeheader()

            for note in notesList:
                writer.writerow(note.to_json())


     def load(self) -> list[Note]:
        listOfNotes = []

        with open(self.file_name, "r") as f:
            reader = csv.reader(f)

            for values in reader:
                listOfNotes.append(Note.from_tuple(values))
        
        return listOfNotes

     def info(self) -> dict[str, str]:
        return {"file_name": self.file_ame}