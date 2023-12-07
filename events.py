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

def playback(guiValues):
    global audioFileLocation, fileFormat
    
    # Playback Inputs
    try:
        filePlay = guiValues["filePlayInputPlayback"]
        filePath = audioFileLocation + filePlay + fileFormat
        print("Playback inputs read")
        audio.play(filePath)
    except Exception as e:
        print("Cannot playback audio")
        print(e)
      
def record(guiValues):    
    global audioFileLocation
    
    # Record Inputs
    try:
        fileName = guiValues["fileNameInputRecord"]
        numMinutes = guiValues["minutesInputRecord"]
        numSeconds = guiValues["secondsInputRecord"]
        print("Record inputs read")
        audio.record(audioFileLocation, fileName, numMinutes, numSeconds)
    except Exception as e:
        print("Cannot record audio")
        print(e)
        
def merge(guiValues):
    global audioFileLocation, fileFormat
        
    # Merge Inputs
    try:
        fileMerge1 = guiValues["fileMerge1InputMerge"]
        fileMerge1Path = audioFileLocation + fileMerge1 + fileFormat
        fileMerge2 = guiValues["fileMerge2InputMerge"]
        fileMerge2Path = audioFileLocation + fileMerge2 + fileFormat
        fileName = guiValues["fileNameInputMerge"]
        filePath = audioFileLocation + fileName + fileFormat
        print("Merge inputs read")
        audio.merge(fileMerge1Path, fileMerge2Path, filePath)
    except Exception as e:
        print("Cannot merge audio")
        print(e)
    
def recordPlay(guiValues):
    global audiofileLocation
    
    # Karaoke Inputs
    try: 
        filePlay = guiValues["filePlayInputKaraoke"]
        filePlayPath = audioFileLocation + filePlay + fileFormat
        fileName = guiValues["fileNameInputKaraoke"]
        print("Karaoke inputs read")
        audio.recordAndPlay(filePlayPath, audioFileLocation, fileName)
    except Exception as e:
        print("Cannot karaoke")
        print(e)
         
