# Install python library for GUI
# py -m pip install pysimplegui (windows)

# Import simpleGUI library
import PySimpleGUI as psg

# Any setup code before running GUI
print("Program set up successful, executing program")

# Create and set up the GUI and events
import gui
import events
gui.createWindow()
print("GUI set up successful")

# Create an event loop
while True:
    event, values = gui.window.read()

    # End program if user closes window 
    if event == psg.WIN_CLOSED:
        break


    # Switch to 'Main Page' layout
    if event == "Exit Record":
        gui.switchWindow("main")
    elif event == "Exit Playback":
        gui.switchWindow("main")   
    elif event == "Exit Karaoke":
        gui.switchWindow("main")   
    elif event == "Exit Merge":
        gui.switchWindow("main")   
        
    # Switch to 'Record Audio' layout
    if event == "Record Audio":
        gui.switchWindow("record")
        
    # Switch to 'Playback Audio' layout
    if event == "Playback Audio":
        gui.switchWindow("playback")
    
    # Switch to 'Karaoke Mode' layout
    if event == "Karaoke Mode":
        gui.switchWindow("karaoke")
    
    # Switch to 'Merge Audio' layout
    if event == "Merge Audio":
        gui.switchWindow("merge")
    

    # Record audio from user
    if event == "Record":        
        events.record(values)

    # Playback user audio
    if event == "Playback":
        events.playback(values)
        
    # Record with Playback
    if event == "Record Karaoke":
        events.recordPlay(values) 
        
    # Playback merged user audio
    if event == "Merge":
        events.merge(values)
        
    
gui.window.close()
print("GUI closed successfully")

# Any closing code before exiting the program
print("Program closed successfully")
