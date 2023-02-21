import mouse
import keyboard
import threading
import keybinds

class Recorder:
    mouse_events = []
    keyboard_events = []

    def startRecording(self):
        mouse.hook(self.mouse_events.append)
        keyboard.hook(self.keyboard_events.append)
        keyboard.start_recording()
        keyboard.wait(keybinds.END_RECORDING_KEY)
        mouse.unhook(self.mouse_events.append)
        keyboard.unhook(self.keyboard_events.append)
        keyboard.stop_recording()

    def playRecording(self):
        k_thread = threading.Thread(target=lambda: keyboard.play(self.keyboard_events))
        k_thread.start()

        m_thread = threading.Thread(target=lambda: mouse.play(self.mouse_events))
        m_thread.start()
        k_thread.join()
        m_thread.join()

    def reset(self):
        self.mouse_events = []
        self.keyboard_events = []