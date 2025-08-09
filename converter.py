import mido

music = mido.MidiFile("midi/carelesswhisper.mid")
output = []
ticksPerBeat = music.ticks_per_beat
tempo = mido.bpm2tempo(120)

NOTE_NAMES_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def noteToName(n: int) -> str:
    return NOTE_NAMES_SHARP[n % 12]

for i, track in enumerate(music.tracks):
    print(f"Track {i}: {track.name}")
    for message in track:
        deltaSeconds = mido.tick2second(message.time, ticksPerBeat, tempo)

        if message.type == "set_tempo":
            tempo = message.tempo

        if message.time != 0 and hasattr(message, "note"):
            output.append((noteToName(message.note), round(deltaSeconds, 2)))

print(output)