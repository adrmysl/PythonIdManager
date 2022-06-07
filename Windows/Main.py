import datetime

import PySimpleGUI as sg

from Models.Employee import Employee
from Services.EmployeeService import addNewEmployee, editEmployee, deleteEmployee
from Windows.AddNewCardTab import AddNewCard
from Windows.AddUserTab import AddNewUser, EditUser
from Windows.ShowAllEmployees import ShowAllEmployees

elementList = ['firstName', 'secondName', 'surname', 'dateOfBirth', 'position', 'endContract']
my_new_theme = {'BACKGROUND': '#FFFFFF',
                'TEXT': 'black',
                'INPUT': 'white',
                'TEXT_INPUT': 'black',
                'SCROLL': 'white',
                'BUTTON': ('black', 'white'),
                'PROGRESS': ('#FFFFFF', '#FFFFFF'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

sg.theme_add_new('my_custom_theme', my_new_theme)
sg.theme('my_custom_theme')
employees = None


def cleanInput():
    for element in elementList:
        window[element].Update('')
        if element == 'dateOfBirth':
            window[element].Update('1.01.2022')
        if element == 'endContract':
            window[element].Update('1.01.2022')


def checkInput(newEmployee, infoBar):
    infoBar.Update('')
    for value in newEmployee:
        if value in elementList and value != 'secondName':
            if value == 'dateOfBirth' or value == 'endContract':
                try:
                    datetime.datetime.strptime(newEmployee[value], '%d.%M.%Y')
                except ValueError:
                    infoBar.Update('Data jest niepoprawna!')
                    print('Bledna data dla', value)
                    return False
            if newEmployee[value] == '':
                infoBar.Update('Wprowadź wszystkie dane!')
                return False
    return True


selectedEmployee = {}
window = AddNewCard()


while True:
    event, values = window.read()
    if event in (None, 'Exit') or event == sg.WIN_CLOSED:
        break
    if event == 'createBtn':
        if checkInput(values, window['infoBar']):
            isOk = addNewEmployee(Employee(values))
            if isOk:
                window, employees = ShowAllEmployees()
            else:
                window['infoBar'].Update('Wystąpił błąd')
    if event == 'eraseBtn':
        cleanInput()
    if event == 'homeBtn':
        window.close()
        window, employees = ShowAllEmployees()
    if event == 'showAllEmployeesTab':
        selectedRow = [employees[row] for row in values[event]]
        row = selectedRow.pop()
        selectedEmployee['id'] = row[0]
        row = row[1:]
        for i in range(len(elementList)):
            selectedEmployee[elementList[i]] = row[i]
    if event == 'addBtn':
        window.close()
        window = AddNewUser()
    if event == 'editBtn':
        if selectedEmployee:
            window.close()
            window = EditUser(selectedEmployee)
    if event == 'updateBtn':
        editEmployee(values, selectedEmployee)
        window.close()
        window, employees = ShowAllEmployees()
    if event == 'deleteBtn':
        answer = sg.popup_yes_no('Usunąć pracownika?')
        if answer == 'Yes':
            deleteEmployee(selectedEmployee)
            window.close()
            window, employees = ShowAllEmployees()


