# -*- coding: utf-8 -*-

from __future__ import absolute_import

#    mingus - Music theory Python package, note module.
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

from mingus.containers.instrument import MidiPercuInstr
from mingus.containers.note import Note
import six
from mingus.containers.mt_exceptions import NoteFormatError


class PercussionNote(Note):
    """Percusion notes do not have a name of the staff (e.g. C or F#)"""

    # noinspection PyMissingConstructor
    def __init__(self, instr, velocity=64, channel=None, duration=None):
        """
        Set duration in milliseconds if you want to stop the instrument before it stops itself.
        For example, a player might manual stop a triangle after 1 second.
        """    
        if isinstance(instr, six.string_types):
            instr = MidiPercuInstr[instr]
        elif isinstance(instr, int):
            instr = MidiPercuInstr(instr)
        if isinstance(instr, MidiPercuInstr):
            self.name = instr.name
            self.key_number = instr.value
            assert 0 <= velocity < 128, 'Velocity must be between 0 and 127'
            if velocity is not None:
                self.velocity = velocity
            if channel is not None:
                self.channel = channel
            self.duration = duration
        else:
            raise NoteFormatError(
                "Don't know what to do with instr object: %r" % instr)
        return

    def __int__(self):
        return self.key_number

    def __repr__(self):
        return self.name
