from datetime import datetime

import PySimpleGUI as sg

from Models.Employee import Employee
from Services.ImageService import convert_file_to_base64

calendar_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8' \
                b'/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAg5JREFUeNqUUktrE1EYPeNcaFKfs0nIIpjHGKYttKYZcKkbwZ2LuhGXLnWh4p8oClJwU9CtrrosFKSlC0EURUJhOiQN0hRStbWmPprM23u/eThQCu2Be7/v3u87Z869c6UgCBBDkqQrPGh8mHz/PVI4qiYJAfZ0+xlPp7wv5jnjfr4x/vzbJ7ms/UoLHK4FTfdx4SGjqm3XH9y6eHXlzR7a7TYuj6mNaV2B4/hw3AB2IKEzkqPaJK8p03m8Xe2eElSaguEBcxwgKw1xc/ErmPMHP3Ys7H63sLPLx56Ng8Fvqu3bAwzckCO4LBKQRXx5p47m9TFYQwdF9hdPjGxyBOXSBHc2CZuFpmNOKGANKd5b6uHM6VE4lof+voUL57M4CjEH4hL51T4KToiIEzkAZJ8vFpaXSdD3/SR6nkcxvXd3ZoY4/y+RL9zoPVSrVaiqSnmlUqEhUC6XUSqVKBe9sQCLjiS7XLkxOwvXdWHzX6LZNrbn5siBoijo9/vkQOSiF2kBrsZiB7XbNyh+frGAa7pO+UfThK5plL9bW4sdsLSAHKmi9XqJHAg0Ox1yMJrJ4INhIH72ojc45IBv/pyfh1ooUJO5tYXxYjEU2thAvVYL3ayvxwIpB5I04kXq7V6PblrA2NwkB3SkVitxIHoFJxHgLWdl/sLyuRyOA9ErOIkA/15Xz2Re4WToiumfAAMAm3VXYXe8jNQAAAAASUVORK5CYII= '


def AddNewUser():
    nameCol = [[sg.T("Imię"), sg.In(key='firstName')]]
    secondNameCol = [[sg.Text("Drugie imię"), sg.Input(key='secondName')]]
    surnameCol = [[sg.Text("Nazwisko"), sg.Input(key='surname')]]
    positionCol = [[sg.Text("Stanowisko"), sg.Input(key='position')]]
    endContractCol = [[sg.Text("Data końca umowy"), sg.I(size=(20, 10), key='endContract', default_text='1.01.1900'),
                       sg.CalendarButton('', image_data=calendar_icon, format='%d.%m.%Y', target='endContract',
                                         key='calBtn1')]]

    layout = [[sg.Button(image_data=convert_file_to_base64('home.png'),
                         image_subsample=2, pad=((0, 410), (0, 0)),
                         border_width=0, key='homeBtn')],
              [sg.Text("Wprowadź dane:", border_width=5, key='Header')],
              [sg.Frame('', nameCol)],
              [sg.Frame('', secondNameCol)],
              [sg.Frame('', surnameCol)],
              [sg.Frame('',
                        [[sg.Text("Data urodzin"), sg.I(size=(20, 10), key='dateOfBirth', default_text='1.01.2022'),
                          sg.CalendarButton("", image_data=calendar_icon, format='%d.%m.%Y', target='dateOfBirth',
                                            key='calBtn2')]])],
              [sg.Frame('', positionCol)],
              [sg.Frame('', endContractCol)],
              [sg.Button("Utwórz pracownika", key="createBtn", pad=(0, 0, 0, 10)),
               sg.Button('Usuń dane', key="eraseBtn")],
              [sg.Text("", key="infoBar")]]
    return sg.Window('IdManager v1.0', layout, default_element_size=(24, 1), auto_size_text=False, size=(580, 460))


def EditUser(employee):
    employee = Employee(employee)
    employee = employee.__dict__
    employee['dateOfBirth'] = datetime.strptime(str(employee['dateOfBirth']), '%Y-%m-%d').strftime('%d.%m.%Y')
    employee['endContract'] = datetime.strptime(str(employee['endContract']), '%Y-%m-%d').strftime('%d.%m.%Y')

    employee = Employee(employee)
    nameCol = [[sg.T("Imię"), sg.In(key='name', default_text=employee.firstName)]]
    secondNameCol = [[sg.Text("Drugie imię"), sg.Input(key='secondName', default_text=employee.secondName)]]
    surnameCol = [[sg.Text("Nazwisko"), sg.Input(key='surname', default_text=employee.surname)]]
    positionCol = [[sg.Text("Stanowisko"), sg.Input(key='position', default_text=employee.position)]]
    endContractCol = [
        [sg.Text("Data końca umowy"), sg.I(size=(20, 10), key='endContract', default_text=employee.endContract),
         sg.CalendarButton('', image_data=calendar_icon, format='%d.%m.%Y', target='endContract',
                           key='calBtn1')]]

    layout = [[sg.Button(image_data=convert_file_to_base64('home.png'),
                         image_subsample=2, pad=((0, 410), (0, 0)),
                         border_width=0, key='homeBtn')],
              [sg.Text("Edytuj dane:", border_width=5, key='Header')],
              [sg.Frame('', nameCol)],
              [sg.Frame('', secondNameCol)],
              [sg.Frame('', surnameCol)],
              [sg.Frame('',
                        [[sg.Text("Data urodzin"),
                          sg.I(size=(20, 10), key='dateOfBirth', default_text=employee.dateOfBirth),
                          sg.CalendarButton("", image_data=calendar_icon, format='%d.%m.%Y', target='dateOfBirth',
                                            key='calBtn2')]])],
              [sg.Frame('', positionCol)],
              [sg.Frame('', endContractCol)],
              [sg.Button("Aktualizuj dane", key="updateBtn", pad=(0, 0, 0, 10)),
               sg.Button('Usuń dane', key="eraseBtn")],
              [sg.Text("", key="infoBar")]]
    return sg.Window('IdManager v1.0', layout, default_element_size=(24, 1), auto_size_text=False, size=(580, 460))
