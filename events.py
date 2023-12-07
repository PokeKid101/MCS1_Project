# Install python library for GUI
# py -m pip install pysimplegui (windows)

# File dedicated to the various functions of the GUI buttons

# Import necessary libararies and files
import PySimpleGUI as psg
import gui
import audio

# Default variables
audioFileLocation = "Sound Files/"
fileFormat = ".wav"

# Global variables
fileName = ""
filePlay = ""
fileMerge1 = ""
fileMerge2 = ""
numMinutes = ""
numSeconds = ""
filePath = ""

def updateValues(guiValues):
    global fileName, filePlay
    global fileMerge1, fileMerge2
    global numMinutes, numSeconds

    # Seperate try/exception cases for the different layouts

    # Record Inputs
    try:
        fileName = guiValues["fileNameInputRecord"]
        updateFilePath(fileName)
        numMinutes = guiValues["minutesInputRecord"]
        numSeconds = guiValues["secondsInputRecord"]
    except Exception as e:
        pass
    
    # Playback Inputs
    try:
        filePlay = guiValues["filePlayInputPlayback"]
        updateFilePath(filePlay)
    except Exception as e:
        pass
      
    # Karaoke Inputs
    try: 
        filePlay = guiValues["filePlayInputKaraoke"]
        updateFilePath(filePlay)
        fileName = guiValues["fileNameInputKaraoke"]
        updateFilePath(fileName)
    except Exception as e:
        pass
       
    # Merge Inputs
    try:
        fileMerge1 = guiValues["fileMerge1Merge"]
        fileMerge2 = guiValues["fileMerge2Merge"]
        # Format file mergers
        fileMerge1 = audioFileLocation + fileMerge1 + fileFormat
        fileMerge2 = audioFileLocation + fileMerge2 + fileFormat
        
        fileName = guiValues["fileNameInputMerge"]
        updateFilePath(fileName)
    except Exception as e:
        pass
    

def updateLabel(elementName, elementText):
    gui.window[elementName].update(elementText)

def updateFilePath(fileName):
    global filePath
    filePath = audioFileLocation + fileName + fileFormat

def playback():
     audio.play(filePath)

def record():    
    audio.record(audioFileLocation, fileName, numMinutes, numSeconds)

def merge():
    audio.merge(filePath, songPath, mergedPath)

def recordPlay():
    audio.recordAndPlay(filePath, audioFileLocation, songName)
