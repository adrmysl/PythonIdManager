import base64
import pathlib

import PySimpleGUI as sg


def convert_file_to_base64(filename):
    try:
        fullPath = pathlib.Path().resolve() / 'icon'
        contents = open(fullPath / filename, 'rb').read()
        encoded = base64.b64encode(contents)
        return encoded
    except Exception as error:
        sg.popup_error('Cancelled - An error occurred', error)