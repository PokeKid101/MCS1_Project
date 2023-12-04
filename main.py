# Install python library for GUI
# py -m pip install pysimplegui (windows)

# Import simpleGUI library
import PySimpleGUI as psg

# Any setup code before running GUI
print("Program set up successful, executing program")

# Create and set up the GUI
import gui
import events as events
print("GUI set up successful")

# Create an event loop
while True:
    event, values = gui.window.read()

    # End program if user closes window 
    if event == psg.WIN_CLOSED:
        break

    # Print hello world when button is pressed
    if event == "Say 'Hello World'":
        events.updateLabel('testTxt', 'hello again')

gui.window.close()
print("GUI closed successfully")

# Any closing code before exiting the program
print("Program closed successfully")