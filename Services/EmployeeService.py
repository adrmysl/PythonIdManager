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


def editEmployee(employee, oldEmployee):
    employee['dateOfBirth'] = datetime.strptime(str(employee['dateOfBirth']), '%d.%m.%Y').isoformat()
    employee['endContract'] = datetime.strptime(str(employee['endContract']), '%d.%m.%Y').isoformat()
    record, condition = executeSQLCommand(f""" UPDATE Employee SET firstName='{employee['name']}', 
    secondName='{employee['secondName']}', surname='{employee['surname']}', dateOfBirth='{employee['dateOfBirth']}', 
    position='{employee['position']}', endContract='{employee['endContract']}' WHERE id={oldEmployee['id']}""")
    return condition


def readAllEmployees():
    results, isOk = executeSQLCommand("""SELECT * from Employee""")
    return results


def deleteEmployee(selectedEmployee):

    results, isOk = executeSQLCommand(f"""DELETE FROM Employee WHERE id={selectedEmployee['id']}""")
    return results
