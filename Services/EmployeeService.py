from Services.DatabaseService import executeSQLCommand


def addNewEmployee(employee):
    record, condition = executeSQLCommand(""" INSERT INTO Employee
     (firstName, secondName, surname, dateOfBirth, position, endContract) VALUES (%s,%s,%s,%s,%s,%s)""", employee)
    if condition:
        return True
    else:
        return False