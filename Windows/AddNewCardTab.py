from datetime import datetime

import PySimpleGUI as sg

from Models.Employee import Employee

calendar_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8' \
                b'/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAg5JREFUeNqUUktrE1EYPeNcaFKfs0nIIpjHGKYttKYZcKkbwZ2LuhGXLnWh4p8oClJwU9CtrrosFKSlC0EURUJhOiQN0hRStbWmPprM23u/eThQCu2Be7/v3u87Z869c6UgCBBDkqQrPGh8mHz/PVI4qiYJAfZ0+xlPp7wv5jnjfr4x/vzbJ7ms/UoLHK4FTfdx4SGjqm3XH9y6eHXlzR7a7TYuj6mNaV2B4/hw3AB2IKEzkqPaJK8p03m8Xe2eElSaguEBcxwgKw1xc/ErmPMHP3Ys7H63sLPLx56Ng8Fvqu3bAwzckCO4LBKQRXx5p47m9TFYQwdF9hdPjGxyBOXSBHc2CZuFpmNOKGANKd5b6uHM6VE4lof+voUL57M4CjEH4hL51T4KToiIEzkAZJ8vFpaXSdD3/SR6nkcxvXd3ZoY4/y+RL9zoPVSrVaiqSnmlUqEhUC6XUSqVKBe9sQCLjiS7XLkxOwvXdWHzX6LZNrbn5siBoijo9/vkQOSiF2kBrsZiB7XbNyh+frGAa7pO+UfThK5plL9bW4sdsLSAHKmi9XqJHAg0Ox1yMJrJ4INhIH72ojc45IBv/pyfh1ooUJO5tYXxYjEU2thAvVYL3ayvxwIpB5I04kXq7V6PblrA2NwkB3SkVitxIHoFJxHgLWdl/sLyuRyOA9ErOIkA/15Xz2Re4WToiumfAAMAm3VXYXe8jNQAAAAASUVORK5CYII= '

accessPlaces = (
    'Brama wejściowa', 'Biuro', 'Laboratorium', 'Księgowość', 'Fabryka', 'Stacja prób', 'Spawalnia', 'Lakiernia',
    'Zarząd')


def AddNewCard():
    padding = (00, 0, 0, 0)
    checkboxes = [[sg.Text('Miejsca dostępu')],
                  *[[sg.CB(f'{place}', key=f'{place}''')] for place in accessPlaces]]
    idRow = [[sg.T("ID karty", size=(12, 1)), sg.I(key='cardID', size=(24, 10))]]
    expRow = [
        [sg.T("Data ważności", size=(12, 1)), sg.I(size=(20, 10), key='expDate', default_text='1.01.2022'),
         sg.CalendarButton('', image_data=calendar_icon, format='%d.%m.%Y', target='expDate',
                           key='calBtnForExp')]]
    accRow = [[sg.T("Miejsca dostępu", size=(12, 1)), sg.B('Wyświetl listę', pad=((45, 45), (0, 0)))]]
    photoRow = [[sg.T("Zdjęcie", size=(12, 1)), sg.I(key='photoPath', size=(14, 10)), sg.B('Wczytaj')]]
    viewRow = [[sg.T("Podgląd zdjęcia", size=(30, 1)), sg.Image(key='previewImage', size=(24, 130))]]

    Col1 = [[sg.T('Tworzenie karty')],
            [sg.Frame('', idRow)],
            [sg.Frame('', expRow)],
            [sg.Frame('', accRow)],
            [sg.Frame('', photoRow)],
            [sg.Frame('', viewRow)]
            ]

    layout = [[sg.Column(Col1), sg.Column(checkboxes)],[sg.B('Zapisz kartę', pad=((10, 0), (20, 0))), sg.B('Usuń dane', pad=((10, 0), (20, 0)))]]
    return sg.Window('IdManager v1.0', layout, size=(580, 460))
