# Install python library for GUI
# py -m pip install pysimplegui (windows)

# File dedicated to the various functions of the GUI buttons

# Import necessary libararies and files
import PySimpleGUI as psg
import gui

def updateLabel(elementName, elementText):
    gui.window[elementName].update(elementText)

