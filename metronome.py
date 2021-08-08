from PyQt5.QtCore import QObject, QTimer, pyqtSignal

class Metronome(QObject):
    tick = pyqtSignal()
    strong_tick = pyqtSignal()

    def __init__(self, parent=None):
        super(Metronome, self).__init__(parent)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick_cb)

        self.strong_period = 4
        self.current_sub_tick = -1

    def start(self):
        self.timer.start(1000)
        self.tick_cb()

    def tick_cb(self):
        self.tick.emit()

        self.current_sub_tick += 1
        if self.current_sub_tick >= self.strong_period:
            self.current_sub_tick = 0

        if self.current_sub_tick == 0:
            self.strong_tick.emit()
