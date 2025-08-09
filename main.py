import badge

class App(badge.BaseApp):
    def __init__(self):
        self.bpm = 0.2
        self.frequencies = {
            "C": 262, 
            "C#": 277, 
            "D": 294, 
            "D#": 311, 
            "E": 330, 
            "F": 349, 
            "F#": 370, 
            "G": 392, 
            "G#": 415, 
            "A": 440, 
            "A#": 466, 
            "B": 494
        }
        self.rickroll = ["G#", "F#", "F", "D#", "C#", "C#", "C#", "C#", "C#", "C#", "D#", "D#", "D#", "D#", "D#", "D#", "G#", "G#", "G#", "G#", "D#", "D#", "D#", "D#", "D#", "D#", "F", "F", "F", "F", "F"]

    def on_open(self):
        badge.display.fill(1)
        badge.display.nice_text("Music Player", 0, 0, 32)
        badge.display.show()

    def loop(self):
        for note in self.rickroll:
            badge.buzzer.tone(self.frequencies[note], self.bpm)