# Install python library for GUI
# py -m pip install pysimplegui

import PySimpleGUI as sg

layout = [
    [sg.Text("MCS Final Project")],
    [sg.Text("Karaoke Machine")],
    [sg.Text("Landon Schreck and Matthew Mangsen")],
    [sg.Button("OK")]
]

# Create the window
window = sg.Window("MCS Final Project", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()