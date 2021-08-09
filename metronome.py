from PyQt5.QtCore import QObject, QTimer, pyqtSignal

class Metronome(QObject):
    tick = pyqtSignal(str)
    strong_tick = pyqtSignal()

    def __init__(self, bpm, strong_period, parent=None):
        super(Metronome, self).__init__(parent)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick_cb)

        self.strong_period = strong_period
        self.current_tick = 0

        self.tick_period_ms = self.bpm_to_period_ms(bpm)

    def start(self):
        self.timer.start(self.tick_period_ms)
        self.tick_cb()

    def tick_cb(self):
        self.current_tick += 1
        if self.current_tick > self.strong_period:
            self.current_tick = 1

        self.tick.emit(str(self.current_tick))

        if self.current_tick == 1:
            self.strong_tick.emit()

    def set_strong_period(self, period):
        self.strong_period = period
        self.current_tick = 0

    def set_tempo(self, bpm):
        self.tick_period_ms = self.bpm_to_period_ms(bpm)
        self.timer.start(self.tick_period_ms)

    def bpm_to_period_ms(self, bpm):
        return 1000 * 60 / bpm
