# -*- coding: utf-8 -*-

from __future__ import absolute_import, annotations
from enum import IntEnum

#    mingus - Music theory Python package, instrument module.
#    Copyright (C) 2008-2009, Bart Spaans
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from mingus.containers.note import Note
from mingus.containers.mt_exceptions import UnexpectedObjectError
import six


class Instrument(object):

    """An instrument object.

    The Instrument class is pretty self explanatory. Instruments can be used
    with Tracks to define which instrument plays what, with the added bonus
    of checking whether the entered notes are in the range of the
    instrument.

    It's probably easiest to subclass your own Instruments (see Piano and
    Guitar for examples).
    """

    name = "Instrument"
    range = (Note("C", 0), Note("C", 8))
    clef = "bass and treble"
    tuning = None  # optional StringTuning object

    def __init__(self):
        pass

    def set_range(self, range):
        """Set the range of the instrument.

        A range is a tuple of two Notes or note strings.
        """
        if isinstance(range[0], six.string_types):
            range[0] = Note(range[0])
            range[1] = Note(range[1])
        if not hasattr(range[0], "name"):
            raise UnexpectedObjectError(
                "Unexpected object '%s'. " "Expecting a mingus.containers.Note object" % range[
                    0]
            )
        self.range = range

    def note_in_range(self, note):
        """Test whether note is in the range of this Instrument.

        Return True if so, False otherwise.
        """
        if isinstance(note, six.string_types):
            note = Note(note)
        if not hasattr(note, "name"):
            raise UnexpectedObjectError(
                "Unexpected object '%s'. " "Expecting a mingus.containers.Note object" % note
            )
        if note >= self.range[0] and note <= self.range[1]:
            return True
        return False

    def notes_in_range(self, notes):
        """An alias for can_play_notes."""
        return self.can_play_notes(notes)

    def can_play_notes(self, notes):
        """Test if the notes lie within the range of the instrument.

        Return True if so, False otherwise.
        """
        if hasattr(notes, "notes"):
            notes = notes.notes
        if not isinstance(notes, list):
            notes = [notes]
        for n in notes:
            if not self.note_in_range(n):
                return False
        return True

    def __repr__(self):
        """Return a string representing the object."""
        return "%s [%s - %s]" % (self.name, self.range[0], self.range[1])


class Piano(Instrument):

    name = "Piano"
    range = (Note("F", 0), Note("B", 8))

    def __init__(self):
        Instrument.__init__(self)


class Guitar(Instrument):

    name = "Guitar"
    range = (Note("E", 3), Note("E", 7))
    clef = "Treble"

    def __init__(self):
        Instrument.__init__(self)

    def can_play_notes(self, notes):
        if len(notes) > 6:
            return False
        return Instrument.can_play_notes(self, notes)


class MidiInstr(IntEnum):
    ACOUSTIC_GRAND_PIANO = 0
    BRIGHT_ACOUSTIC_PIANO = 1
    ELECTRIC_GRAND_PIANO = 2
    HONKY_TONK_PIANO = 3
    ELECTRIC_PIANO_1 = 4
    ELECTRIC_PIANO_2 = 5
    HARPSICHORD = 6
    CLAVI = 7

    CELESTA = 8
    GLOCKENSPIEL = 9
    MUSIC_BOX = 10
    VIBRAPHONE = 11
    MARIMBA = 12
    XYLOPHONE = 13
    TUBULAR_BELLS = 14
    DULCIMER = 15

    DRAWBAR_ORGAN = 16
    PERCUSSIVE_ORGAN = 17
    ROCK_ORGAN = 18
    CHURCH_ORGAN = 19
    REED_ORGAN = 20
    ACCORDION = 21
    HARMONICA = 22
    TANGO_ACCORDION = 23

    ACOUSTIC_GUITAR_NYLON = 24
    ACOUSTIC_GUITAR_STEEL = 25
    ELECTRIC_GUITAR_JAZZ = 26
    ELECTRIC_GUITAR_CLEAN = 27
    ELECTRIC_GUITAR_MUTED = 28
    OVERDRIVEN_GUITAR = 29
    DISTORTION_GUITAR = 30
    GUITAR_HARMONICS = 31

    ACOUSTIC_BASS = 32
    ELECTRIC_BASS_FINGER = 33
    ELECTRIC_BASS_PICK = 34
    FRETLESS_BASS = 35
    SLAP_BASS_1 = 36
    SLAP_BASS_2 = 37
    SYNTH_BASS_1 = 38
    SYNTH_BASS_2 = 39

    VIOLIN = 40
    VIOLA = 41
    CELLO = 42
    CONTRABASS = 43
    TREMOLO_STRINGS = 44
    PIZZICATO_STRINGS = 45
    ORCHESTRAL_HARP = 46
    TIMPANI = 47

    STRING_ENSEMBLE_1 = 48
    STRING_ENSEMBLE_2 = 49
    SYNTHSTRINGS_1 = 50
    SYNTHSTRINGS_2 = 51
    CHOIR_AAHS = 52
    VOICE_OOHS = 53
    SYNTH_VOICE = 54
    ORCHESTRA_HIT = 55

    TRUMPET = 56
    TROMBONE = 57
    TUBA = 58
    MUTED_TRUMPET = 59
    FRENCH_HORN = 60
    BRASS_SECTION = 61
    SYNTHBRASS_1 = 62
    SYNTHBRASS_2 = 63

    SOPRANO_SAX = 64
    ALTO_SAX = 65
    TENOR_SAX = 66
    BARITONE_SAX = 67
    OBOE = 68
    ENGLISH_HORN = 69
    BASSOON = 70
    CLARINET = 71

    PICCOLO = 72
    FLUTE = 73
    RECORDER = 74
    PAN_FLUTE = 75
    BLOWN_BOTTLE = 76
    SHAKUHACHI = 77
    WHISTLE = 78
    OCARINA = 79

    LEAD_1_SQUARE = 80
    LEAD_2_SAWTOOTH = 81
    LEAD_3_CALLIOPE = 82
    LEAD_4_CHIFF = 83
    LEAD_5_CHARANG = 84
    LEAD_6_VOICE = 85
    LEAD_7_FIFTHS = 86
    LEAD_8_BASS_LEAD = 87

    PAD_1_NEW_AGE = 88
    PAD_2_WARM = 89
    PAD_3_POLYSYNTH = 90
    PAD_4_CHOIR = 91
    PAD_5_BOWED = 92
    PAD_6_METALLIC = 93
    PAD_7_HALO = 94
    PAD_8_SWEEP = 95

    FX_1_RAIN = 96
    FX_2_SOUNDTRACK = 97
    FX_3_CRYSTAL = 98
    FX_4_ATMOSPHERE = 99
    FX_5_BRIGHTNESS = 100
    FX_6_GOBLINS = 101
    FX_7_ECHOES = 102
    FX_8_SCI_FI = 103

    SITAR = 104
    BANJO = 105
    SHAMISEN = 106
    KOTO = 107
    KALIMBA = 108
    BAG_PIPE = 109
    FIDDLE = 110
    SHANAI = 111

    TINKLE_BELL = 112
    AGOGO = 113
    STEEL_DRUMS = 114
    WOODBLOCK = 115
    TAIKO_DRUM = 116
    MELODIC_TOM = 117
    SYNTH_DRUM = 118
    REVERSE_CYMBAL = 119

    GUITAR_FRET_NOISE = 120
    BREATH_NOISE = 121
    SEASHORE = 122
    BIRD_TWEET = 123
    TELEPHONE_RING = 124
    HELICOPTER = 125
    APPLAUSE = 126
    GUNSHOT = 127


class MidiInstrument(Instrument):

    range = (Note("C", 0), Note("B", 8))
    name = ""

    def __init__(self, name: str = "", instrument_nr: int = None):
        self.name = name
        self.instrument_nr = instrument_nr
        
    @property
    def instrument_nr(self):
        if not self._instrument_nr and self._name:
            instr_name = self._name.replace(" ", "_")
            instr_name = instr_name.replace("(", "")
            instr_name = instr_name.replace(")", "")
            instr_name = instr_name.upper()
            try:
                self._instrument_nr = MidiInstr[instr_name].value
            except Exception:
                pass
        if self._instrument_nr:
            return self._instrument_nr
        else:
            return 1
    
    @instrument_nr.setter
    def instrument_nr(self, value: int | MidiInstr):
        self._instrument_nr = value
        if isinstance(value, MidiInstr) and not self._name:
            self._name = value.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def __int__(self):
        return int(self.instrument_nr)


class MidiPercuInstr(IntEnum):
    ACOUSTIC_BASS_DRUM = 35
    BASS_DRUM_1 = 36
    SIDE_STICK = 37
    ACOUSTIC_SNARE = 38
    HAND_CLAP = 39
    ELECTRIC_SNARE = 40
    LOW_FLOOR_TOM = 41
    CLOSED_HI_HAT = 42
    HIGH_FLOOR_TOM = 43
    PEDAL_HI_HAT = 44
    LOW_TOM = 45
    OPEN_HI_HAT = 46
    LOW_MID_TOM = 47
    HI_MID_TOM = 48
    CRASH_CYMBAL_1 = 49
    HIGH_TOM = 50
    RIDE_CYMBAL_1 = 51
    CHINESE_CYMBAL = 52
    RIDE_BELL = 53
    TAMBOURINE = 54
    SPLASH_CYMBAL = 55
    COWBELL = 56
    CRASH_CYMBAL_2 = 57
    VIBRASLAP = 58
    RIDE_CYMBAL_2 = 59
    HI_BONGO = 60
    LOW_BONGO = 61
    MUTE_HI_CONGA = 62
    OPEN_HI_CONGA = 63
    LOW_CONGA = 64
    HIGH_TIMBALE = 65
    LOW_TIMBALE = 66
    HIGH_AGOGO = 67
    LOW_AGOGO = 68
    CABASA = 69
    MARACAS = 70
    SHORT_WHISTLE = 71
    LONG_WHISTLE = 72
    SHORT_GUIRO = 73
    LONG_GUIRO = 74
    CLAVES = 75
    HI_WOOD_BLOCK = 76
    LOW_WOOD_BLOCK = 77
    MUTE_CUICA = 78
    OPEN_CUICA = 79
    MUTE_TRIANGLE = 80
    OPEN_TRIANGLE = 81


class MidiPercussionInstrument(Instrument):
    def __init__(self):
        super(MidiPercussionInstrument, self).__init__()
        self.name = "Midi Percussion"

    def acoustic_bass_drum(self):
        return Note(35 - 12)

    def bass_drum_1(self):
        return Note(36 - 12)

    def side_stick(self):
        return Note(37 - 12)

    def acoustic_snare(self):
        return Note(38 - 12)

    def hand_clap(self):
        return Note(39 - 12)

    def electric_snare(self):
        return Note(40 - 12)

    def low_floor_tom(self):
        return Note(41 - 12)

    def closed_hi_hat(self):
        return Note(42 - 12)

    def high_floor_tom(self):
        return Note(43 - 12)

    def pedal_hi_hat(self):
        return Note(44 - 12)

    def low_tom(self):
        return Note(45 - 12)

    def open_hi_hat(self):
        return Note(46 - 12)

    def low_mid_tom(self):
        return Note(47 - 12)

    def hi_mid_tom(self):
        return Note(48 - 12)

    def crash_cymbal_1(self):
        return Note(49 - 12)

    def high_tom(self):
        return Note(50 - 12)

    def ride_cymbal_1(self):
        return Note(51 - 12)

    def chinese_cymbal(self):
        return Note(52 - 12)

    def ride_bell(self):
        return Note(53 - 12)

    def tambourine(self):
        return Note(54 - 12)

    def splash_cymbal(self):
        return Note(55 - 12)

    def cowbell(self):
        return Note(56 - 12)

    def crash_cymbal_2(self):
        return Note(57 - 12)

    def vibraslap(self):
        return Note(58 - 12)

    def ride_cymbal_2(self):
        return Note(59 - 12)

    def hi_bongo(self):
        return Note(60 - 12)

    def low_bongo(self):
        return Note(61 - 12)

    def mute_hi_conga(self):
        return Note(62 - 12)

    def open_hi_conga(self):
        return Note(63 - 12)

    def low_conga(self):
        return Note(64 - 12)

    def high_timbale(self):
        return Note(65 - 12)

    def low_timbale(self):
        return Note(66 - 12)

    def high_agogo(self):
        return Note(67 - 12)

    def low_agogo(self):
        return Note(68 - 12)

    def cabasa(self):
        return Note(69 - 12)

    def maracas(self):
        return Note(70 - 12)

    def short_whistle(self):
        return Note(71 - 12)

    def long_whistle(self):
        return Note(72 - 12)

    def short_guiro(self):
        return Note(73 - 12)

    def long_guiro(self):
        return Note(74 - 12)

    def claves(self):
        return Note(75 - 12)

    def hi_wood_block(self):
        return Note(76 - 12)

    def low_wood_block(self):
        return Note(77 - 12)

    def mute_cuica(self):
        return Note(78 - 12)

    def open_cuica(self):
        return Note(79 - 12)

    def mute_triangle(self):
        return Note(80 - 12)

    def open_triangle(self):
        return Note(81 - 12)
