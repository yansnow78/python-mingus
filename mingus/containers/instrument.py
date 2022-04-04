# -*- coding: utf-8 -*-

from __future__ import absolute_import
from enum import Enum, auto

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


class MidiInstr(Enum):
    ACOUSTIC_GRAND_PIANO = 0
    BRIGHT_ACOUSTIC_PIANO = auto()
    ELECTRIC_GRAND_PIANO = auto()
    HONKY_TONK_PIANO = auto()
    ELECTRIC_PIANO_1 = auto()
    ELECTRIC_PIANO_2 = auto()
    HARPSICHORD = auto()
    CLAVI = auto()

    CELESTA = auto()
    GLOCKENSPIEL = auto()
    MUSIC_BOX = auto()
    VIBRAPHONE = auto()
    MARIMBA = auto()
    XYLOPHONE = auto()
    TUBULAR_BELLS = auto()
    DULCIMER = auto()

    DRAWBAR_ORGAN = auto()
    PERCUSSIVE_ORGAN = auto()
    ROCK_ORGAN = auto()
    CHURCH_ORGAN = auto()
    REED_ORGAN = auto()
    ACCORDION = auto()
    HARMONICA = auto()
    TANGO_ACCORDION = auto()

    ACOUSTIC_GUITAR_NYLON = auto()
    ACOUSTIC_GUITAR_STEEL = auto()
    ELECTRIC_GUITAR_JAZZ = auto()
    ELECTRIC_GUITAR_CLEAN = auto()
    ELECTRIC_GUITAR_MUTED = auto()
    OVERDRIVEN_GUITAR = auto()
    DISTORTION_GUITAR = auto()
    GUITAR_HARMONICS = auto()

    ACOUSTIC_BASS = auto()
    ELECTRIC_BASS_FINGER = auto()
    ELECTRIC_BASS_PICK = auto()
    FRETLESS_BASS = auto()
    SLAP_BASS_1 = auto()
    SLAP_BASS_2 = auto()
    SYNTH_BASS_1 = auto()
    SYNTH_BASS_2 = auto()

    VIOLIN = auto()
    VIOLA = auto()
    CELLO = auto()
    CONTRABASS = auto()
    TREMOLO_STRINGS = auto()
    PIZZICATO_STRINGS = auto()
    ORCHESTRAL_HARP = auto()
    TIMPANI = auto()

    STRING_ENSEMBLE_1 = auto()
    STRING_ENSEMBLE_2 = auto()
    SYNTHSTRINGS_1 = auto()
    SYNTHSTRINGS_2 = auto()
    CHOIR_AAHS = auto()
    VOICE_OOHS = auto()
    SYNTH_VOICE = auto()
    ORCHESTRA_HIT = auto()

    TRUMPET = auto()
    TROMBONE = auto()
    TUBA = auto()
    MUTED_TRUMPET = auto()
    FRENCH_HORN = auto()
    BRASS_SECTION = auto()
    SYNTHBRASS_1 = auto()
    SYNTHBRASS_2 = auto()

    SOPRANO_SAX = auto()
    ALTO_SAX = auto()
    TENOR_SAX = auto()
    BARITONE_SAX = auto()
    OBOE = auto()
    ENGLISH_HORN = auto()
    BASSOON = auto()
    CLARINET = auto()

    PICCOLO = auto()
    FLUTE = auto()
    RECORDER = auto()
    PAN_FLUTE = auto()
    BLOWN_BOTTLE = auto()
    SHAKUHACHI = auto()
    WHISTLE = auto()
    OCARINA = auto()

    LEAD_1_SQUARE = auto()
    LEAD_2_SAWTOOTH = auto()
    LEAD_3_CALLIOPE = auto()
    LEAD_4_CHIFF = auto()
    LEAD_5_CHARANG = auto()
    LEAD_6_VOICE = auto()
    LEAD_7_FIFTHS = auto()
    LEAD_8_BASS_LEAD = auto()

    PAD_1_NEW_AGE = auto()
    PAD_2_WARM = auto()
    PAD_3_POLYSYNTH = auto()
    PAD_4_CHOIR = auto()
    PAD_5_BOWED = auto()
    PAD_6_METALLIC = auto()
    PAD_7_HALO = auto()
    PAD_8_SWEEP = auto()

    FX_1_RAIN = auto()
    FX_2_SOUNDTRACK = auto()
    FX_3_CRYSTAL = auto()
    FX_4_ATMOSPHERE = auto()
    FX_5_BRIGHTNESS = auto()
    FX_6_GOBLINS = auto()
    FX_7_ECHOES = auto()
    FX_8_SCI_FI = auto()

    SITAR = auto()
    BANJO = auto()
    SHAMISEN = auto()
    KOTO = auto()
    KALIMBA = auto()
    BAG_PIPE = auto()
    FIDDLE = auto()
    SHANAI = auto()

    TINKLE_BELL = auto()
    AGOGO = auto()
    STEEL_DRUMS = auto()
    WOODBLOCK = auto()
    TAIKO_DRUM = auto()
    MELODIC_TOM = auto()
    SYNTH_DRUM = auto()
    REVERSE_CYMBAL = auto()

    GUITAR_FRET_NOISE = auto()
    BREATH_NOISE = auto()
    SEASHORE = auto()
    BIRD_TWEET = auto()
    TELEPHONE_RING = auto()
    HELICOPTER = auto()
    APPLAUSE = auto()
    GUNSHOT = auto()


class MidiInstrument(Instrument):

    range = (Note("C", 0), Note("B", 8))
    instrument_nr = 1
    name = ""

    def __init__(self, name=""):
        self.name = name


class MidiPercussionInstrument(Instrument):
    def __init__(self):
        super(MidiPercussionInstrument, self).__init__()
        self.name = "Midi Percussion"
        self.mapping = {
            35: "Acoustic Bass Drum",
            36: "Bass Drum 1",
            37: "Side Stick",
            38: "Acoustic Snare",
            39: "Hand Clap",
            40: "Electric Snare",
            41: "Low Floor Tom",
            42: "Closed Hi Hat",
            43: "High Floor Tom",
            44: "Pedal Hi-Hat",
            45: "Low Tom",
            46: "Open Hi-Hat",
            47: "Low-Mid Tom",
            48: "Hi Mid Tom",
            49: "Crash Cymbal 1",
            50: "High Tom",
            51: "Ride Cymbal 1",
            52: "Chinese Cymbal",
            53: "Ride Bell",
            54: "Tambourine",
            55: "Splash Cymbal",
            56: "Cowbell",
            57: "Crash Cymbal 2",
            58: "Vibraslap",
            59: "Ride Cymbal 2",
            60: "Hi Bongo",
            61: "Low Bongo",
            62: "Mute Hi Conga",
            63: "Open Hi Conga",
            64: "Low Conga",
            65: "High Timbale",
            66: "Low Timbale",
            67: "High Agogo",
            68: "Low Agogo",
            69: "Cabasa",
            70: "Maracas",
            71: "Short Whistle",
            72: "Long Whistle",
            73: "Short Guiro",
            74: "Long Guiro",
            75: "Claves",
            76: "Hi Wood Block",
            77: "Low Wood Block",
            78: "Mute Cuica",
            79: "Open Cuica",
            80: "Mute Triangle",
            81: "Open Triangle",
        }

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
