# Import necessary libraries
# py -m pip install pyaudio (windows)
import pyaudio 
# py -m pip install wave (windows)
import wave 
#pip install pydub
from pydub import AudioSegment
import time
import os

def play(filePath):
    # Initalize PyAudio and open audio file
    audio = pyaudio.PyAudio()
    audioFile = wave.open(filePath, 'rb')
    stream = audio.open(
        format=audio.get_format_from_width(audioFile.getsampwidth()),
        channels=audioFile.getnchannels(),
        rate=audioFile.getframerate(),
        output=True
    )

    # Get frames per buffer
    frames_per_buffer = 1024
    print("File Rate:", audioFile.getframerate())

    # Play the audio file
    data = audioFile.readframes(frames_per_buffer)
    print("Playing:", filePath)
    while data:
        stream.write(data)
        data = audioFile.readframes(frames_per_buffer)
    
    # Close the stream and PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

def record(fileLocation, fileName, numMinutes, numSeconds):
    # Set up audio formatting
    audio = pyaudio.PyAudio()
    
    stream = audio.open(
        format=pyaudio.paInt16, 
        channels=1, 
        rate=44100, 
        input=True, 
        frames_per_buffer=1024
        )
    frames = []
    print("Audio formatting set up")

    # Ask user for info
    minutes  = int(numMinutes)
    seconds = int(numSeconds)

    # Set up timer
    timeLength= (minutes*60) + seconds
    timerEnd = time.time() + timeLength
    print("Timer ready")

    # Record audio
    print("Recording...")
    try:
        while time.time() < timerEnd:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    print("Stopped recording")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    print("Saving audio")
    filePath = fileLocation + fileName + ".wav"
    sound_file = wave.open(filePath, "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    print("Audio saved:", filePath)

def recordAndPlay(filePath, fileLocation, fileName):
    # Set up input/output audio
    audioIn = pyaudio.PyAudio();
    audioOut = pyaudio.PyAudio();
    audioFile = wave.open(filePath, 'rb');
    
    # Set up input/output streams
    streamIn = audioIn.open(
        format = pyaudio.paInt16,
        channels = 1,
        rate = audioFile.getframerate(),
        input = True,
        frames_per_buffer = 1024
        )
    streamOut = audioOut.open(
        format = audioOut.get_format_from_width(audioFile.getsampwidth()),
        channels = audioFile.getnchannels(),
        rate = audioFile.getframerate(),
        output = True,
        frames_per_buffer = 1024
        )
    frames = []
    frames_per_buffer = 1024
    print("Input/Output streams set up")
    
    # Record and play audio
    # Duration is as long as played audio
    print("Playing:", filePath)
    print("Recording...")
    dataOut = audioFile.readframes(frames_per_buffer)
    while dataOut:
        streamOut.write(dataOut)        
        dataIn = streamIn.read(1024)
        frames.append(dataIn)
        dataOut = audioFile.readframes(frames_per_buffer)
    
    print("Stopped recording")
    streamIn.stop_stream()
    streamOut.stop_stream()
    streamIn.close()
    streamOut.close()
    audioIn.terminate()
    audioOut.terminate()
    
    print("Saving audio")
    newFilePath = fileLocation + fileName + ".wav"
    sound_file = wave.open(newFilePath, "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audioIn.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    print("Audio saved:", newFilePath)
    

def merge(filePath, songPath, mergedPath):

    print("File Paths:")
    print(f"filePath: {filePath}")
    print(f"songPath: {songPath}")
    print(f"mergedPath: {mergedPath}")
    
    #Read both audio files
    audio1 = AudioSegment.from_file(filePath)
    audio2 = AudioSegment.from_file(songPath)
    
    # Overlay sounds to play simultaneously
    combined_audio = audio1.overlay(audio2)
    
    # Export the combined audio to the specified output file path
    combined_audio.export(mergedPath, format="wav")
