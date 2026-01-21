from datetime import datetime
from core import Note, Notebook, Storage, JSONFile, CSVFile

class ConsoleApp:
    __notebook: Notebook

    def __init__(self):
        self.__notebook = Notebook(storage=JSONFile(file_name="notes.json"))

    def run(self):
        print("Application running...")

    def show_notes(self) -> None:
        all_notes = self.__notebook.get_notes()

        for note in all_notes:
            print(note)

    def add_note(self):
        note_id = int(input("Enter a note_id: "))
        text = input('Enter text: ')
        date_created = datetime.now()
        self.__notebook.add_note(note=Note(id=note_id, text=text, date_created=date_created))


    def show_note(self) -> None:
        note_id = int(input("Enter a note_id: "))
        note = self.__notebook.get_note(note_id=note_id)
        print(note)


    def update_note(self):
        note_id = int(input("Enter a note_id: "))
        new_text = input('Enter new text: ')

        self.__notebook.update_note(new_note= Note(id=note_id, text=new_text, date_created=datetime.now()))


    def delete_note(self) -> None:
        note_id = int(input("Enter a note_id: "))
        self.__notebook.delete_note(note_id=note_id)



if __name__ == "__main__":
    app = ConsoleApp()

    app.run()

    app.show_notes()

    app.show_note()
