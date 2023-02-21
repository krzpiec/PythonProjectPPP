import customtkinter
from tkinter import *
from Recorder import Recorder
from RecordingFileManager import RecordingFileManager

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("1000x1000")

recorder = Recorder()
recordingFileManager = RecordingFileManager()


def saveRecording():
    recordingFileManager.saveCurrentRecording(recorder.mouse_events, recorder.keyboard_events, nameEntry.get())


def loadRecordings():
    recordingFileManager.loadRecordingsByName(nameEntry.get())
    recorder.keyboard_events = recordingFileManager.loaded_keyboard_events
    recorder.mouse_events = recordingFileManager.loaded_mouse_events


def listRecordings():
    recordings = recordingFileManager.getRecordingsNames()
    counter = 0
    for record in recordings:
        listbox.insert(counter, record)
        counter += 1


def clearRecordingsList():
    listbox.delete(0, END)


def selectRecording():
    nameEntry.delete(0, END)
    nameEntry.insert(0, listbox.get(ANCHOR))


mouse_events = []
keyboard_events = []

frame = customtkinter.CTkFrame(master=root);
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Bot do metina na klikanko")
label.pack(pady=12, padx=10)

nameEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Recording name")
nameEntry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Record", command=recorder.startRecording)
button.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Play", command=recorder.playRecording)
button1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Reset", command=recorder.reset)
button2.pack(pady=12, padx=10)

button3 = customtkinter.CTkButton(master=frame, text="Save", command=saveRecording)
button3.pack(pady=12, padx=10)

button4 = customtkinter.CTkButton(master=frame, text="Load", command=loadRecordings)
button4.pack(pady=12, padx=10)

button5 = customtkinter.CTkButton(master=frame, text="Load", command=recordingFileManager.getRecordingsNames)
button4.pack(pady=12, padx=10)

button5 = customtkinter.CTkButton(master=frame, text="Show recordings", command=listRecordings)
button5.pack(pady=12, padx=10)

button6 = customtkinter.CTkButton(master=frame, text="Clear recordings list", command=clearRecordingsList)
button6.pack(pady=12, padx=10)

button7 = customtkinter.CTkButton(master=frame, text="Select recordings", command=selectRecording)
button7.pack(pady=12, padx=10)

listbox = Listbox(frame)
listbox.pack(pady=5, padx=20)

root.mainloop()
