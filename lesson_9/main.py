from core import Note, Notebook, Storage, JSONFile, CSVFile

class ConsoleApp:
    
    def __init__(self):
        storage = Storage()
        self.__notebook = Notebook(storage=JSONFile(file_name="notes.json"))

