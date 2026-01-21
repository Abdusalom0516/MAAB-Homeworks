from datetime import datetime
from core import Note, Notebook, Storage, JSONFile, CSVFile

class ConsoleApp:
    __notebook: Notebook

    def __init__(self):
        self.__notebook = Notebook(storage=CSVFile(file_name="notes.csv"))

    def run(self):
        print("Application running...")
        self.show_menu()


    def show_all_notes(self) -> None:
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


    def show_menu(self):
        while True:
            userOption = input('''
1. Add Note
2. Show All Notes
3. Show Note by ID
4. Update Note
5. Delete Note
6. Exit
Your Option: --------- ''')

            if userOption == "6":
                break
            elif userOption == "1":
                self.add_note()
            elif userOption == "2":
                self.show_all_notes()
            elif userOption == "3":
                self.show_note()
            elif userOption == "4":
                self.update_note()
            elif userOption == "5":
                self.delete_note()
            else:
                print("Invalid Option!")







if __name__ == "__main__":
    app = ConsoleApp()

    app.run()
