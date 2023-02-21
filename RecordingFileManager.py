import os
import pickle

from shared import *


class RecordingFileManager:
    loaded_mouse_events = []
    loaded_keyboard_events = []

    def saveCurrentRecording(self, mouse_events, keyboard_events, name):
        recordingDirectory = RECORDING_PATH + "\\" + name + "\\"
        try:
            os.mkdir(recordingDirectory)
        except:
            print("Error")

        self.saveEvents(
            recordingDirectory + MOUSE_RECORDING_FILENAME,
            mouse_events
        )

        self.saveEvents(
            recordingDirectory + KEYBOARD_RECORDING_FILENAME,
            keyboard_events
        )

    def loadRecordingsByName(self, name):
        print(name)
        self.loaded_mouse_events = self.loadEvents(RECORDING_PATH + "\\" + name + "\\" + MOUSE_RECORDING_FILENAME)

        self.loaded_keyboard_events = self.loadEvents(RECORDING_PATH + "\\" + name + "\\" + KEYBOARD_RECORDING_FILENAME)

    # TODO ta sama nazwa pliku
    def saveEvents(self, path, events):
        output = open(path, 'wb+')
        pickle.dump(events, output)
        output.close()

    def loadEvents(self, path):
        input = open(path, 'rb')
        events = pickle.load(input)
        input.close()
        return events

    def getRecordingsNames(self):
        filenames = [x[0] for x in os.walk(RECORDING_PATH)]
        recordingNames = list(map(lambda filepath: filepath.replace(RECORDING_PATH + "\\", ''), filenames))
        recordingNames.pop(0)
        print(recordingNames)
        return recordingNames
