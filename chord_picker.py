#! /usr//bin/env python3
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import QObject, QTimer, pyqtSignal
import random

class ChordPicker(QObject):
    new_chord = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ChordPicker, self).__init__(parent)
        self.fundamental_probability = {
            'A': 1/12,
            'Bb': 1/12,
            'B': 1/12,
            'C': 1/12,
            'C#': 1/12,
            'D': 1/12,
            'Eb': 1/12,
            'E': 1/12,
            'F': 1/12,
            'F#': 1/12,
            'G': 1/12,
            'G#': 1/12 }
        self.chord_type_probability = {
            '7': 1.0,
            'maj7': 0 }

        self.current_chord = '-'

    def generate(self):
        fund = random.choices([*self.fundamental_probability.keys()],
                              weights = [*self.fundamental_probability.values()])
        chord_type = random.choices(
            [*self.chord_type_probability.keys()],
            weights = [*self.chord_type_probability.values()])
        return fund[0] + chord_type[0]

    def update(self):
        c = self.generate()
        while c == self.current_chord:
            c = self.generate()
        self.current_chord = c

        self.new_chord.emit(c)

