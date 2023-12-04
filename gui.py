# Install python library for GUI
# py -m pip install pysimplegui (windows)

# Import simpleGUI library
import PySimpleGUI as psg

# Generate GUI layout
layout = [
    [psg.Text("MCS Final Project")],
    [psg.Text("Karaoke Machine")],
    [psg.Text("Landon Schreck and Matthew Mangsen")],
    [psg.Button("Say 'Hello World'")],
    [psg.Text("", key="testTxt")]
]

# Create window with disired layout
window = psg.Window("MCS Final Project", layout)