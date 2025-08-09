import badge

class App(badge.BaseApp):
    def __init__(self):
        self.frequencies = {
            " ": 0,
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
            "B": 494, 
            "C5": 523,
            "C5#": 554,
            "D5": 587,
            "D5#": 622,
            "E5": 659,
            "F5": 698,
            "F5#": 740,
            "G5": 784,
            "G5#": 831,
            "A5": 880,
            "A5#": 932,
            "B5": 988
        }
        self.rickroll = [("G#", 0.2), ("F#", 0.2), ("F", 0.2), ("D#", 0.2), ("C#", 0.2), ("C#", 0.2), ("C#", 0.2), ("C#", 0.2), ("C#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("G#", 0.2), ("G#", 0.2), ("G#", 0.2), ("G#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("F", 0.2), ("F", 0.2), ("F", 0.2), ("F", 0.2), ("F", 0.2), ("G#", 0.2), ("F#", 0.2), ("F", 0.2), ("D#", 0.2), ("C#", 0.2), ("C#", 0.2), ("C#", 0.2), ("C#", 0.2), ("C#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("G#", 0.2), ("G#", 0.2), ("G#", 0.2), ("G#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("D#", 0.2), ("F", 0.2), ("F", 0.2), ("F", 0.2), ("F", 0.2), ("F", 0.2)]
        self.carelesswhisper = [("E5", 0.5), ("D5", 0.3), ("A", 0.5), ("F", 0.5), ("E5", 0.8), ("D5", 0.3), ("A", 0.5), ("F", 0.8), ("A", 0.3), ("C5", 0.5), ("A#", 0.3), ("F", 0.5), ("D", 0.5), ("C5", 0.8), ("A#", 0.3), ("F", 0.3), ("C", 0.8)]
        self.musics = [("Never Gonna Give You Up", self.rickroll, "rickroll.pbm"), ("Careless Whisper", self.carelesswhisper, "carelesswhisper.pbm")]

        self.mode = "text"

        self.menuSize = len(self.musics)
        self.menuEntry = 0
        self.oldEntry = -1

        self.playing = False

    def renderUI(self):
        if self.mode == "text":
            badge.display.fill(1)
            badge.display.nice_text("Music Player", 0, 0, 32)
            for music in self.musics:
                badge.display.nice_text(music[0], 0, 32 + 18*(1+self.musics.index(music)))
        elif self.mode == "icon":
            badge.display.fill(1)
            for music in self.musics:
                badge.display.blit(badge.display.import_pbm(f"/apps/transmitter/{music[2]}"), 14+(self.musics.index(music) % 3)*(48+14), 14+(self.musics.index(music) // 3)*(48+14))

    def renderSelection(self):
        if self.mode == "text":
            badge.display.rect(0, 32 + 18*(1+self.oldEntry), 200, 18, 1)
            badge.display.rect(0, 32 + 18*(1+self.menuEntry), 200, 18, 0)
        elif self.mode == "icon":
            badge.display.rect(14+(self.oldEntry % 3)*(48+14), 14+(self.oldEntry // 3)*(48+14), 48, 48, 1)
            badge.display.rect(14+(self.menuEntry % 3)*(48+14), 14+(self.menuEntry // 3)*(48+14), 48, 48, 0)
        badge.display.show()

    def pause(self):
        badge.buzzer.no_tone()

    def play(self):
        self.pause()
        for item in self.musics[self.menuEntry][1]:
            badge.buzzer.tone(self.frequencies[item[0]], item[1])
            if badge.input.get_button(badge.input.Buttons.SW13):
                self.pause
                self.playing = False
                return
        self.playing = False

    def on_open(self):
        self.renderUI()

    def loop(self):
        if badge.input.get_button(badge.input.Buttons.SW7):
            if self.menuEntry == 0:
                self.menuEntry = self.menuSize - 1
            else:
                self.menuEntry -= 1
        if badge.input.get_button(badge.input.Buttons.SW6):
            if self.menuEntry == self.menuSize - 1:
                self.menuEntry = 0
            else:
                self.menuEntry += 1
        if badge.input.get_button(badge.input.Buttons.SW13):
            if self.playing:
                self.pause()
                self.playing = False
            else:
                self.play()
                self.playing = True
        if badge.input.get_button(badge.input.Buttons.SW14):
            if self.mode == "text":
                self.mode = "icon"
                self.renderUI()
                self.renderSelection()
            else:
                self.mode = "text"
                self.renderUI()
                self.renderSelection()

        if self.oldEntry != self.menuEntry:
            self.renderSelection()
        self.oldEntry = self.menuEntry