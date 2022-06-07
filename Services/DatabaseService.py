import mysql.connector


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
            if type(element) is dict:
                result = cursor.execute(command, tuple(element.values()))
            else:
                result = cursor.execute(command)
            connection.commit()
        return result, True
    except mysql.connector.Error as error:
        print("Failed to execute command, error: {}".format(error))
        return None, False
