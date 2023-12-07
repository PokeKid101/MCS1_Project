# Install python library for GUI
# py -m pip install pysimplegui (windows)

# Import simpleGUI library
import PySimpleGUI as psg

# Generate GUI layouts
window = "" # leave blank
windowName = "MCS - Final Project"
currentLayout = 1

# Main page
mainInstructions = " \
To use a feature provided in this project, click the button of the feature you would like to use. \n \
To retun to this page, click the associated 'Exit' button within the feature's window."
mainLayout = [
    [psg.Text("MCS Final Project")],
    [psg.Text("Karaoke Machine")],
    [psg.Text("Landon Schreck and Matthew Mangsen")],
    [psg.Text("")],
    [psg.Text(mainInstructions)],
    [psg.Button("Record Audio"), psg.Button("Playback Audio")],
    [psg.Button("Karaoke Mode"), psg.Button("Merge Audio")]
]

# Record audio page
recordInstructions = " \
'Record Audio' will record incoming audio signals for the specified amount of time. \n \
Please type in name of the file you wish to create in 'File Name' (do NOT include the .wav extention). \n \
Then specify the length of the file with 'Minutes' and 'Seconds'. \n \
When ready, press the 'Record' button to being recording."
recordLayout = [
    [psg.Text("Record Audio")],
    [psg.Button("Exit Record")],
    [psg.Text("")],
    [psg.Text(recordInstructions)],
    [psg.Text("File Name: "), psg.Input("", key="fileNameInputRecord")],
    [psg.Text("Minutes:   "), psg.Input("", key="minutesInputRecord")],
    [psg.Text("Seconds:   "), psg.Input("", key="secondsInputRecord")],
    [psg.Button("Record")]
]

# Playback audio page
playbackInstructions = " \
'Playback Audio' will play the entirity of a specified audio file to the outgoing audio device. \n \
Please type in the name of the file you wish to play in 'File Play' (do NOT include the .wav extension). \n \
When ready, press the 'Playback' button to being playing the audio file."
playbackLayout = [
    [psg.Text("Playback Audio")],
    [psg.Button("Exit Playback")],
    [psg.Text("")],
    [psg.Text(playbackInstructions)],
    [psg.Text("File Play: "), psg.Input("", key="filePlayInputPlayback")],
    [psg.Button("Playback")]
]    
    
# Karaoke mode page
karaokeInstructions = " \
'Karaoke Mode' will play the entirity of a specified audio file to the outgoing audio device while also \n \
recording any incoming audio signals. The incoming audio signals are saved as a stand alone file, if you \n \
wish to hear the recorded audio with the played audio, please merge the two files. \n \
Please type in the name of the file you wish to play in 'File Play' (do NOT include the .wav extension). \n \
Please type in the name of the file you wish to create 'File Name' (do NOT include the .wav extension). \n \
When ready, press the 'Record Karaoke' button to begin recording."
karaokeLayout = [
    [psg.Text("Karaoke Mode")],
    [psg.Button("Exit Karaoke")],
    [psg.Text("")],
    [psg.Text(karaokeInstructions)],
    [psg.Text("File Play: "), psg.Input("", key="filePlayInputKaraoke")],
    [psg.Text("File Name: "), psg.Input("", key="fileNameInputKaraoke")],
    [psg.Button("Record Karaoke")]
]
    
# Merge audio page
mergeInstructions = " \
'Merge Audio' will merge two seperate .wav files and create a new stand alone merged .wav file. The length \n \
of the merged file is dependent on the first .wav file, 'File Merge 1'. \n \
Please type in the name of the first file you wish to merge in 'File Merge 1' (do NOT include the .wav extension). \n \
Please type in the name of the second file you wish to merge in 'File Merge 2' (do NOT include the .wav extension). \n \
Please type the name of the created merged file in 'File Name' (do NOT include the .wav extension). \n \
When ready, press the 'Merge' button to merge the two .wav files."
mergeLayout = [
    [psg.Text("Merge Audio Files")],
    [psg.Button("Exit Merge")],
    [psg.Text("")],
    [psg.Text(mergeInstructions)],
    [psg.Text("File Merge 1: "), psg.Input("", key="fileMerge1InputMerge")],
    [psg.Text("File Merge 2: "), psg.Input("", key="fileMerge2InputMerge")],
    [psg.Text("File Name:    "), psg.Input("", key="fileNameInputMerge")],
    [psg.Button("Merge")]
]

# Final layout
layout = [
    [psg.Column(mainLayout, key='-COL1-'),
     psg.Column(recordLayout, visible=False, key='-COL2-'),
     psg.Column(playbackLayout, visible=False, key='-COL3-'),
     psg.Column(karaokeLayout, visible=False, key='-COL4-'),
     psg.Column(mergeLayout, visible=False, key='-COL5-'),     
    ]
]

def clearInputs():
    pass

def switchWindow(show):
    global window, currentLayout
    
    # Make current layout invisible
    window[f'-COL{currentLayout}-'].update(visible=False)
    
    # Check what should be the next viewed layout
    if show == "main":
        currentLayout = 1
    elif show == "record":
        currentLayout = 2
    elif show == "playback":
        currentLayout = 3
    elif show == "karaoke":
        currentLayout = 4
    elif show == "merge":
        currentLayout = 5
    else:
        currentLayout = 1 # resort to main menu if there is a problem
    
    # Display new layout
    window[f'-COL{currentLayout}-'].update(visible=True)


def createWindow():
    global window
    
    # Set up the window with the layouts
    window = psg.Window(windowName, layout, finalize=True)

    # Set the current shown layout as mainLayout
    switchWindow("main")
