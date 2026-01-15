
# ** Generalized `Vector` Class
# ** Objective**: Create a Python class `Vector` that represents a mathematical vector in an n-dimensional space, capable of handling any number of dimensions.


# ** Employee Records Manager (OOP Version)
# **Objective**: Create a program to manage employee records using classes and file handling.


# ** To-Do Application
# ** Objective**: Create a flexible To-Do application to manage tasks with support for different file storage formats (e.g., CSV, JSON). The application should be designed such that adding support for a new file format requires minimal changes to the code.

# Your To-Do application should provide the following features:
# 1. **Add a task**: Allow users to add tasks with the following details:
#    - `Task ID`
#    - `Title`
#    - `Description`
#    - `Due Date` (optional)
#    - `Status` (e.g., Pending, In Progress, Completed)
# 2. **View tasks**: Display all tasks with their details.
# 3. **Update a task**: Allow users to modify a task's details using its Task ID.
# 4. **Delete a task**: Remove a task by its Task ID.
# 5. **Filter tasks**: Filter tasks by status (e.g., Pending or Completed).
# 6. **Save and load tasks**: Save tasks to a file and load them from the file on startup.

from datetime import date
import json
class Task:
    def __str__(self):
        return f"taskID:{self.taskID}, title:{self.title}, description:{self.description}, status:{self.status}, dueDate:{self.dueDate}"

    def __init__(self, *, taskID, title, description, status, dueDate=date.today()):
        self.taskID = taskID
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.status = status
    
    def toJson(self):
        return {f"taskID: {self.taskID}, title: {self.title}, description: {self.description}, status: {self.status}, dueDate: {self.dueDate}"}

    @staticmethod
    def fromJson(json: dict):
        return Task(taskID=json["taskID"], description=json["description"], title=json["title"], status=json["status"], dueDate=json["dueDate"])
        
class ToDo:
    def __init__(self):
        while True:
            userOption = input('''
----------------------------------
Welcome to the To-Do Application!
# 1. Add a new task
# 2. View all tasks
# 3. Update a task
# 4. Delete a task
# 5. Filter tasks by status
# 6. Exit
# Your option: ''')

            if userOption == "6":
                break
            elif userOption == "1":
                ToDo.addNewTask()
            elif userOption == "2":
                 ToDo.viewTasks()
            elif userOption == "3":
                ToDo.updateTask()
            elif userOption == "4":
                ToDo.deleteTask()
            elif userOption == "5":
                ToDo.filterTaskByStatus()
            else:
                print("Invalid Option!")

    @staticmethod
    def addNewTask():
        data = {}
        with open("tasks.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

            newtTaskID = int(input("Enter a taskID: "))
            newtTaskTitle = input("Enter a title: ")
            newtTaskDescription = input("Enter a description: ")
            newtTaskStatus = input("Enter a status: ")


            data[newtTaskID] = {"taskID": newtTaskID, "title": newtTaskTitle, "description": newtTaskDescription, "dueDate": "2026-01-20", "status": newtTaskStatus}

        with open("tasks.json", "w") as f:
            json.dump(data, f, indent=4)


    @staticmethod
    def viewTasks():
        pass

    @staticmethod
    def updateTask():
        pass

    @staticmethod
    def deleteTask():
        pass

    @staticmethod
    def filterTaskByStatus():
        pass



myTodoApplication = ToDo()


