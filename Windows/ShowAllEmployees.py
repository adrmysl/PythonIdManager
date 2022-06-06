import PySimpleGUI as sg

from Services.EmployeeService import readAllEmployees
from Services.ImageService import convert_file_to_base64


def ShowAllEmployees():
    mainButtons = [sg.Button(image_data=convert_file_to_base64('home.png'),
                             image_subsample=2, pad=((0, 410), (0, 0)),
                             border_width=0, key='homeBtn'),
                   sg.Button(image_data=convert_file_to_base64('add.png'),
                             image_subsample=2, border_width=0,
                             key='addBtn'),
                   sg.Button(image_data=convert_file_to_base64('delete.png'),
                             image_subsample=2, border_width=0,
                             key='deleteBtn'),
                   sg.Button(image_data=convert_file_to_base64('edit.png'),
                             image_subsample=2, border_width=0,
                             key='editBtn'),
                   sg.Button(image_data=convert_file_to_base64('card.png'),
                             image_subsample=2, border_width=0,
                             key='cardBtn')]
    font = ('Arial', 8)
    headings = ['Imię', 'Drugie imię', 'Nazwisko', 'Data urodzin', 'Stanowisko', 'Koniec umowy', 'ID karty']
    employees = readAllEmployees()
    colSize = [10, 10, 10, 10, 10, 10, 6]
    employeesList = []
    for i in range(len(employees)):
        employeesList.append(employees[i][1:])
    layout = [mainButtons,
              [sg.Table(headings=headings,
                        key='showAllEmployeesTab',
                        selected_row_colors=('black', None),
                        col_widths=colSize,
                        values=employeesList,
                        justification='left',
                        auto_size_columns=False,
                        size=(580, 460),
                        font=font,
                        enable_events=True)
               ]]
    return sg.Window('IdManager v1.0', layout, size=(580, 460), finalize=True), employees
