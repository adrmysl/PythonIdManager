import base64
import pathlib

import PySimpleGUI as sg

calendar_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8' \
                b'/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAg5JREFUeNqUUktrE1EYPeNcaFKfs0nIIpjHGKYttKYZcKkbwZ2LuhGXLnWh4p8oClJwU9CtrrosFKSlC0EURUJhOiQN0hRStbWmPprM23u/eThQCu2Be7/v3u87Z869c6UgCBBDkqQrPGh8mHz/PVI4qiYJAfZ0+xlPp7wv5jnjfr4x/vzbJ7ms/UoLHK4FTfdx4SGjqm3XH9y6eHXlzR7a7TYuj6mNaV2B4/hw3AB2IKEzkqPaJK8p03m8Xe2eElSaguEBcxwgKw1xc/ErmPMHP3Ys7H63sLPLx56Ng8Fvqu3bAwzckCO4LBKQRXx5p47m9TFYQwdF9hdPjGxyBOXSBHc2CZuFpmNOKGANKd5b6uHM6VE4lof+voUL57M4CjEH4hL51T4KToiIEzkAZJ8vFpaXSdD3/SR6nkcxvXd3ZoY4/y+RL9zoPVSrVaiqSnmlUqEhUC6XUSqVKBe9sQCLjiS7XLkxOwvXdWHzX6LZNrbn5siBoijo9/vkQOSiF2kBrsZiB7XbNyh+frGAa7pO+UfThK5plL9bW4sdsLSAHKmi9XqJHAg0Ox1yMJrJ4INhIH72ojc45IBv/pyfh1ooUJO5tYXxYjEU2thAvVYL3ayvxwIpB5I04kXq7V6PblrA2NwkB3SkVitxIHoFJxHgLWdl/sLyuRyOA9ErOIkA/15Xz2Re4WToiumfAAMAm3VXYXe8jNQAAAAASUVORK5CYII= '

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


def convert_file_to_base64(filename):
    try:
        fullPath = pathlib.Path().resolve() / 'icon'
        contents = open(fullPath / filename, 'rb').read()
        encoded = base64.b64encode(contents)
        return encoded
    except Exception as error:
        sg.popup_error('Cancelled - An error occurred', error)

def myDef():
    nameCol = [[sg.T("Imię"), sg.In(key='name')]]
    secondNameCol = [[sg.Text("Drugie imię"), sg.Input(key='secondName')]]
    surnameCol = [[sg.Text("Nazwisko"), sg.Input(key='surname')]]
    positionCol = [[sg.Text("Stanowisko"), sg.Input(key='position')]]
    endContractCol = [[sg.Text("Data końca umowy"), sg.I(size=(20, 10), key='endContract'), sg.CalendarButton('', image_data=calendar_icon, format='%d.%M.%Y', key='calBtn1')]]

    layout = [[sg.Button(image_data=convert_file_to_base64('calendar.png'), image_subsample=4)],
              [sg.Text("Wprowadź dane:", border_width=5)],
              [sg.Frame('', nameCol)],
              [sg.Frame('', secondNameCol)],
              [sg.Frame('', surnameCol)],
              [sg.Frame('',
                        [[sg.Text("Data urodzin"), sg.I(size=(20, 10), key='dateOfBirth'), sg.CalendarButton("", image_data=sg.red_x , format='%d.%M.%Y', key='calBtn2')]])],
              [sg.Frame('', positionCol)],
              [sg.Frame('', endContractCol)],
              [sg.Button("Utwórz pracownika", key="createBtn", pad=(0,0,0,10)), sg.Button('Usuń dane', key="eraseBtn")]]
    window = sg.Window('IdManager v1.0', layout, default_element_size=(24, 1), auto_size_text=False, size=(580, 460))

    while True:
        event, values = window.read()
       # print(event, values)
        if event in (None, 'Exit'):
            break
        if event == 'createBtn':
            print(values)
    window.close()

myDef()