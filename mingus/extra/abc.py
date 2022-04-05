# -*- coding: utf-8 -*-

#    mingus - Music theory Python package, fluidsynth module.
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>pygame.examples.mask.main()

from mingus.containers.note import Note
from mingus.containers.bar import Bar
from mingus.containers.track import Track


def to_bars(notes_str: str, container: Track | Bar | list[Bar],
            lang: str = "us"):
    duration_str = ""

    def add_notes(notes, duration):
        bars = None
        last_bar = None
        if isinstance(container, Track):
            bars = container.bars
        elif isinstance(container, list):
            bars = container
        elif isinstance(container, Bar):
            last_bar = container
        if bars is not None:
            if len(bars) == 0:
                bars.append(Bar())
            last_bar = bars[-1]
            if last_bar.is_full():
                bars.append(Bar(last_bar.key, last_bar.meter))
                last_bar = bars[-1]
        if last_bar is not None:
            last_bar.place_notes(notes, calc_duration(duration_str))

    def calc_duration(duration_str):
        str_len = len(duration_str)
        if str_len:
            if duration_str.count('/') == str_len:
                duration = 4/str_len
            else:
                if duration_str[0] == '/':
                    duration_str = '1'+duration_str
                duration = 4/eval(duration_str)
        else:
            duration = 4
        return duration

    if lang == "fr":
        note_map = {"do": "c", "d": "#", "re": "d", "ré": "d",
                    "mi": "e", "fa": "f", "sol": "g", "la": "a", "si": "b"}
        for key, val in note_map.items():
            notes_str = notes_str.replace(key, val)
        for key, val in note_map.items():
            notes_str = notes_str.replace(key.upper(), val.upper())
    note_begin = False
    note = None
    prev_note = None
    for x in notes_str:
        prev_note = note
        note_begin = False
        if 'A' <= x <= 'G':
            note = Note(x)
            note_begin = True
            # note_begin = True
        elif 'a' <= x <= 'g':
            x = x.upper()
            note = Note(x, 5)
            note_begin = True
        elif x in ["#", "b"]:
            note.name += x
        elif x in ["Z", "z"]:
            note = None
            note_begin = True
        elif x == "'":
            note.octave += 1
        elif x == ",":
            note.octave -= 1
        elif x in [" ", ""]== " " or x == "|":
            pass
        elif x.isdigit() or (x == '/'):
            # if duration_str == "":
            #     duration_str += '1'
            duration_str += x
        if note_begin and (prev_note is not None):
            add_notes(prev_note, calc_duration(duration_str))
            duration_str = ""
    add_notes(note, calc_duration(duration_str))
