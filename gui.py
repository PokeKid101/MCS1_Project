# Install python library for GUI
# py -m pip install pysimplegui (windows)

# Import simpleGUI library
import PySimpleGUI as psg

# Generate GUI layouts
window = "" # leave blank
windowName = "MCS - Final Project"
breakPoint = psg.Text("")

# Main page
mainLayout = [
    [psg.Text("MCS Final Project")],
    [psg.Text("Karaoke Machine")],
    [psg.Text("Landon Schreck and Matthew Mangsen")],
    [psg.Text("")],
    [psg.Text("(Instructions Here)")],
    [psg.Button("Record Audio"), psg.Button("Playback Audio")],
    [psg.Button("Karaoke Mode"), psg.Button("Merge Audio")],
    #[psg.Text("")],    
    #[psg.Text("File Name: "), psg.Input("", key="fileNameInput")],
    #[psg.Text("Num Minutes: "), psg.Input("", key="minutesInput")],
    #[psg.Text("Num Seconds: "), psg.Input("", key="secondsInput")],
    #[psg.Text("Song File Name: "), psg.Input("", key="songNameInput")],
    #[psg.Text("Merged File Name: "), psg.Input("", key="mergedNameInput")],
    #[psg.Button("Record Audio"), psg.Button("Playback Audio"), psg.Button("Merge Audio")],
    #[psg.Button("Record Play")],  
    []
]

# Record audio page
recordInstructions = "Please type in name of the file you wish to create (do NOT include the .wav extention). Then specify the length of the file."
recordLayout = [
    [psg.Text("Record Audio")],
    [psg.Button("Go Back")],
    [breakPoint],
    [psg.Text(recordInstructions)],
    [psg.Text("File Name: "), psg.Input("", key="fileNameInputRecord")],
    [psg.Text("Minutes:   "), psg.Input("", key="minutesInputRecord")],
    [psg.Text("Seconds:   "), psg.Input("", key="secondsInputRecord")],
    [psg.Button("Record")]
]

# Playback audio page
playbackInstructions = "write instructions here"
playbackLayout = [
    [psg.Text("Playback Audio")],
    [psg.Button("Go Back")],
    [breakPoint],
    [psg.Text(playbackInstructions)],
    [psg.Text("File Play: "), psg.Input("", key="filePlayInputPlayback")],
    [psg.Button("Playback")]
]    
    
# Karaoke mode page
karaokeInstructions = "write instructions here"
karaokeLayout = [
    [psg.Text("Karaoke Mode")],
    [psg.Button("Go Back")],
    [breakPoint],
    [psg.Text(karaokeInstructions)],
    [psg.Text("File Play: "), psg.Input("", key="filePlayInputKaroke")],
    [psg.Text("File Name: "), psg.Input("", key="fileNameInputKaroke")],
    [psg.Button("Record Karaoke")]
]
    
# Merge audio page
mergeInstructions = "write instructions here"
mergeLayout = [
    [psg.Text("Merge Audio Files")],
    [psg.Button("Go Back")],
    [breakPoint],
    [psg.Text(karaokeInstructions)],
    [psg.Text("File Merge 1: "), psg.Input("", key="fileMerge1InputMerge")],
    [psg.Text("File Merge 2: "), psg.Input("", key="fileMerge2InputMerge")],
    [psg.Text("File Name:    "), psg.Input("", key="fileNameInputMerge")],
    [psg.Button("Merge")]
]

# Final layout
layout = [
    [psg.Column(mainLayout, visible=False, key="main"),
     psg.Column(recordLayout, visible=False, key="record"),
     psg.Column(playbackLayout, visible=False, key="playback"),
     psg.Column(karaokeLayout, visible=False, key="karaoke"),
     psg.Column(mergeLayout, visible=False, key="merge"),
     
    ]
]

def switchWindow(show):
    global window
    
    # Make all layouts invisible
    window["main"].update(visible=False)
    window["record"].update(visible=False)
    window["playback"].update(visible=False)
    window["karaoke"].update(visible=False)
    window["merge"].update(visible=False)
    
    # Make specified layout visible
    window[show].update(visible=True)


def createWindow():
    global window
    
    # Set up the window with the layouts
    window = psg.Window(windowName, layout)

    # Set the current shown layout as mainLayout
    switchWindow("main")
