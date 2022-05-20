import mysql.connector
from datetime import datetime


def executeSQLCommand(command, element=None):
    print("Connecting to MySQL")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='idmanager',
                                             user='root',
                                             password='')

        cursor = connection.cursor()
        if "SELECT" in command:
            cursor.execute(command)
            result = cursor.fetchall()
        else:
            cursor = connection.cursor()
            employee = element.__dict__
            employee['dateOfBirth'] = datetime.strptime(employee['dateOfBirth'], '%d.%m.%Y').isoformat()
            employee['endContract'] = datetime.strptime(employee['endContract'], '%d.%m.%Y').isoformat()
            result = cursor.execute(command, tuple(element.__dict__.values()))
            connection.commit()
        return result, True
    except mysql.connector.Error as error:
        print("Failed to execute command, error: {}".format(error))
        return None, False