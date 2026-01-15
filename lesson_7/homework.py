
# ** Generalized `Vector` Class
# ** Objective**: Create a Python class `Vector` that represents a mathematical vector in an n-dimensional space, capable of handling any number of dimensions.

import math
class Vector:
    def __init__(self, *arg):
        self.values = arg

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return f"Vector{self.values}"

    def __add__(self, v2):
        if len(self) == len(v2):
            values1 = self.values
            values2 = v2.values
            newValues = []

            for i in range(len(values1)):
                newValues.append(values1[i] + values2[i])

            return Vector(*newValues)
        else:
            print("Vectors have differenct length!")
            return None

    def __sub__(self, v2):
        if len(self) == len(v2):
            values1 = self.values
            values2 = v2.values
            newValues = []

            for i in range(len(values1)):
                newValues.append(values1[i] - values2[i])

            return Vector(*newValues)
        else:
            print("Vectors have differenct length!")
            return None

    def __rmul__(self, v2):
        return self.__mul__(v2)

    def __mul__(self, v2):

        if isinstance(v2, (int, float)):
            values1 = self.values
            newValues = []

            for i in range(len(values1)):
                    newValues.append(values1[i] * v2)

            return Vector(*newValues)
        else:
            if len(self) == len(v2):
                values1 = self.values
                values2 = v2.values
                newValues = []

                for i in range(len(values1)):
                    newValues.append(values1[i] * values2[i])

                return Vector(*newValues)
            else:
                print("Vectors have differenct length!")
                return None

    def magnitude(self):
        squaredValues = [elem**2 for elem in self.values]

        sumOfValues = sum(squaredValues)

        return math.sqrt(sumOfValues)

    def normalize(self):
        magnitudeValue = self.magnitude()
        newValue = []

        for elem in self.values:
            newValue.append(round(elem/magnitudeValue, 3))

        return Vector(*newValue)




v1 = Vector(1, 2, 3)
v2 = Vector(5, 8, 4)
v3 = v1 + v2
v4 = v3 - Vector(7, 3, 1)

multiplication = v1 * v2
scalarMultiplication = v1 * 2

print(v3)
print(v4)
print(multiplication)
print(scalarMultiplication)
print(v1.magnitude())
print(v1.normalize())


# ** Employee Records Manager (OOP Version)
# **Objective**: Create a program to manage employee records using classes and file handling.

# from datetime import date
# import json

# #  - `employee_id`
# #      - `name`
# #      - `position`
# #      - `salary`

# class Employee:
#     def __str__(self):
#         return f"employeeID: {self.employeeID}, name: {self.name}, position: {self.position}, salary: {self.salary}"

#     def toString(self):
#         return f"employeeID: {self.employeeID}, name: {self.name}, position: {self.position}, salary: {self.salary}"

#     def __init__(self, *, employeeID,  name, position, salary):
#         self.employeeID = employeeID
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def toJson(self):
#         return {f"employeeID: {self.employeeID}, name: {self.name}, position: {self.position}, salary: {self.salary}"}

#     @staticmethod
#     def fromJson(json: dict):
#         return Employee(employeeID=json["employeeID"], name=json["name"], position=json["position"], salary=json["salary"])


# class EmployeeRecordManager:
#     def __init__(self):
#         while True:
#             userOption = input('''
# ----------------------------------
# Welcome Employee Record Manager Application!
# # 1. Add new employee record
# # 2. View all employee records
# # 3. Search for an employee by Employee ID
# # 4. Update an employee's information
# # 5. Delete an employee record
# # 6. Exit
# # Your option: ''')

#             if userOption == "6":
#                 break
#             elif userOption == "1":
#                 EmployeeRecordManager.addNewEmlployeeRecord()
#             elif userOption == "2":
#                 EmployeeRecordManager.viewEmployeeRecords()
#             elif userOption == "3":
#                 EmployeeRecordManager.searchForEmployeeByID()
#             elif userOption == "4":
#                 EmployeeRecordManager.updateEmployeeRecord()
#             elif userOption == "5":
#                 EmployeeRecordManager.deleteEmployeeRecord()

#             else:
#                 print("Invalid Option!")

#     @staticmethod
#     def addNewEmlployeeRecord():
#         data = {}
#         with open("employees.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#             newEmployeeID = int(input("Enter a employeeID: "))
#             newEmployeeName = input("Enter a name: ")
#             newEmployeePosition = input("Enter a position: ")
#             newEmployeeSalary = float(input("Enter a salary: "))


#             data[newEmployeeID] = {"employeeID": newEmployeeID, "name": newEmployeeName, "position": newEmployeePosition, "salary": newEmployeeSalary}

#         with open("employees.json", "w") as f:
#             json.dump(data, f, indent=4)
        
#         print("\Employee record added successfully 🎉.")


#     @staticmethod
#     def viewEmployeeRecords():
#         data = {}
#         with open("employees.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#         print("\n")
#         employeeNumber = 0
#         for elem in data.values():
#             employeeNumber += 1
#             print(f"{employeeNumber}. "+Employee.fromJson(elem).toString())

        
#         if employeeNumber == 0:
#             print("No employee found!")


#     @staticmethod
#     def updateEmployeeRecord():
#         employeeID = input("Enter a employeeID to update: ")

#         data = {}
#         with open("employees.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#         employee = data.get(employeeID)

#         print("\n")
#         if employee == None:
#             print(f"Employee not found with {employeeID} ID!")
#         else:
#             newName = input("Enter a name: ")
#             newtPosition = input("Enter a position: ")
#             newSalary = float(input("Enter a salary: "))

#             data[employeeID] = {"employeeID": employeeID, "name": newName, "position": newtPosition, "salary": newSalary}
#             print("Employee record updated successfully 🎉.")
#         with open("temployees.json", "w") as f:
#             json.dump(data, f)

#     @staticmethod
#     def deleteEmployeeRecord():
#         taskId = input("Enter a employeeID to delete: ")

#         data = {}
#         with open("employees.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#         deletedValue = data.pop(taskId, None)

#         print("\n")
#         if deletedValue == None:
#             print(f"Employee not found with {taskId} ID!")
#         else:
#             print("Employee record deleted successfully 🎉.")
#             with open("employees.json", "w") as f:
#                 json.dump(data, f)


#     @staticmethod
#     def searchForEmployeeByID():
#         employeeID = int(input("Enter a employeeID to search: "))

#         data = {}
#         with open("employees.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#         employeeNumber = 0
#         print("\n")
#         for elem in data.values():
#             employeeConv = Employee.fromJson(elem)
#             if employeeConv.employeeID == employeeID:
#                  employeeNumber+=1
#                  print(Employee.fromJson(elem).toString())
#                  break

#         if employeeNumber == 0:
#             print(f"Employee not found with {employeeID} ID!")



# employeeRecordManagerApplication = EmployeeRecordManager()


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

# from datetime import date
# import json
# class Task:
#     def __str__(self):
#         return f"taskID: {self.taskID}, title: {self.title}, description: {self.description}, status: {self.status}, dueDate: {self.dueDate}"
    
#     def toString(self):
#         return f"taskID: {self.taskID}, title: {self.title}, description: {self.description}, status: {self.status}, dueDate: {self.dueDate}"

#     def __init__(self, *, taskID, title, description, status, dueDate=date.today()):
#         self.taskID = taskID
#         self.title = title
#         self.description = description
#         self.dueDate = dueDate
#         self.status = status
    
#     def toJson(self):
#         return {f"taskID: {self.taskID}, title: {self.title}, description: {self.description}, status: {self.status}, dueDate: {self.dueDate}"}

#     @staticmethod
#     def fromJson(json: dict):
#         return Task(taskID=json["taskID"], description=json["description"], title=json["title"], status=json["status"], dueDate=json["dueDate"])
        
# class ToDo:
#     def __init__(self):
#         while True:
#             userOption = input('''
# ----------------------------------
# Welcome to the To-Do Application!
# # 1. Add a new task
# # 2. View all tasks
# # 3. Update a task
# # 4. Delete a task
# # 5. Filter tasks by status
# # 6. Exit
# # Your option: ''')

#             if userOption == "6":
#                 break
#             elif userOption == "1":
#                 ToDo.addNewTask()
#             elif userOption == "2":
#                  ToDo.viewTasks()
#             elif userOption == "3":
#                 ToDo.updateTask()
#             elif userOption == "4":
#                 ToDo.deleteTask()
#             elif userOption == "5":
#                 ToDo.filterTaskByStatus()
#             else:
#                 print("Invalid Option!")

#     @staticmethod
#     def addNewTask():
#         data = {}
#         with open("tasks.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#             newtTaskID = int(input("Enter a taskID: "))
#             newtTaskTitle = input("Enter a title: ")
#             newtTaskDescription = input("Enter a description: ")
#             newtTaskStatus = input("Enter a status: ")
#             newtTaskDueDate = input("Enter a due date (YYYY-MM-DD): ")


#             data[newtTaskID] = {"taskID": newtTaskID, "title": newtTaskTitle, "description": newtTaskDescription, "dueDate": newtTaskDueDate, "status": newtTaskStatus}

#         with open("tasks.json", "w") as f:
#             json.dump(data, f, indent=4)


#     @staticmethod
#     def viewTasks():
#         data = {}
#         with open("tasks.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#         taskNumber = 0
#         for elem in data.values():
#             taskNumber += 1
#             print(f"{taskNumber}. "+Task.fromJson(elem).toString())

#         print("\n")
#         if taskNumber == 0:
#             print("\nNo task found!")


#     @staticmethod
#     def updateTask():
#         taskId = input("Enter a taskID to update: ")

#         data = {}
#         with open("tasks.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#         task = data.get(taskId)

#         if task == None:
#             print(f"\nTask not found with {taskId} ID!")
#         else:
#             newtTaskTitle = input("Enter a title: ")
#             newtTaskDescription = input("Enter a description: ")
#             newtTaskStatus = input("Enter a status: ")
#             newtTaskDueDate = input("Enter a due date (YYYY-MM-DD): ")

#             data[taskId] = {"taskID": taskId, "title": newtTaskTitle, "description": newtTaskDescription, "dueDate": newtTaskDueDate, "status": newtTaskStatus}
#             print("\nTask updated successfully 🎉.")

#         with open("tasks.json", "w") as f:
#             json.dump(data, f)

#     @staticmethod
#     def deleteTask():
#         taskId = input("Enter a taskID to delete: ")

#         data = {}
#         with open("tasks.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#         deletedValue = data.pop(taskId, None)

#         if deletedValue == None:
#             print(f"\nTask not found with {taskId} ID!")
#         else:
#             print("\nTask deleted successfully 🎉.")
#             with open("tasks.json", "w") as f:
#                 json.dump(data, f)


#     @staticmethod
#     def filterTaskByStatus():
#         taskStatus = input("Enter a status to filter: ")

#         data = {}
#         with open("tasks.json", "r") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#         taskNumber = 0
#         print("\n")
#         for elem in data.values():
#             taskConv = Task.fromJson(elem)
#             if taskConv.status == taskStatus:
#                  taskNumber+=1
#                  print(f"{taskNumber}. "+Task.fromJson(elem).toString())

#         if taskNumber == 0:
#             print(f"\nTasks not found with {taskStatus} Status!")



# myTodoApplication = ToDo()


