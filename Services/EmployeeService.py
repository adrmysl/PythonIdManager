from datetime import datetime

from Services.DatabaseService import executeSQLCommand


def addNewEmployee(employee):
    employee = employee.__dict__
    employee['dateOfBirth'] = datetime.strptime(employee['dateOfBirth'], '%d.%m.%Y').isoformat()
    employee['endContract'] = datetime.strptime(employee['endContract'], '%d.%m.%Y').isoformat()
    record, condition = executeSQLCommand(""" INSERT INTO Employee
     (firstName, secondName, surname, dateOfBirth, position, endContract) VALUES (%s,%s,%s,%s,%s,%s)""", employee)
    if condition:
        return True
    else:
        return False


# edit po showAllUser
def editEmployee(employee):
    # TODO: zmodyfikowac calosc editEmployee po showalluser
    record, condition = executeSQLCommand(""" UPDATE Employee SET 
     (firstName, secondName, surname, dateOfBirth, position, endContract) VALUES (%s,%s,%s,%s,%s,%s)
     WHERE id=%s""", employee)
    if condition:
        return True
    else:
        return False
