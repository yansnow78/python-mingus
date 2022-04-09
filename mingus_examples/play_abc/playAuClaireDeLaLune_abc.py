from mingus.containers import Track, Bar
from mingus.containers.instrument import MidiInstr
from mingus.midi import fluidsynth
import mingus.extra.abc as abc

fluidsynth.init("soundfont.sf2")
bpm = 180

t = Track()
t.instrument = MidiInstr.FLUTE
refrein = list[Bar]()
# abc.to_bars("SOL SOL SOL LA | SI2 LA2 | SOL SI LA LA | SOL3 Z", refrein,
#             "fr")
abc.to_bars("GGGA | B2A2 | GBAA | G3Z", refrein)
t += refrein
t += refrein
# abc.to_bars("LA LA LA LA | MI2 MI2 | LA SOL FA# MI | RE3 Z", t, "fr")
abc.to_bars("AAAA | E2E2 | AGF#E | D3Z", t)
t += refrein
fluidsynth.play_Track(t, 1, bpm)

