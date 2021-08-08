from PyQt5.QtCore import QObject, QTimer, pyqtSignal

class Metronome(QObject):
    tick = pyqtSignal(str)
    strong_tick = pyqtSignal()

    def __init__(self, parent=None):
        super(Metronome, self).__init__(parent)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick_cb)

        self.strong_period = 4
        self.current_tick = 0

    def start(self):
        self.timer.start(1000)
        self.tick_cb()

    def tick_cb(self):
        self.current_tick += 1
        if self.current_tick > self.strong_period:
            self.current_tick = 1

        self.tick.emit(str(self.current_tick))

        if self.current_tick == 1:
            self.strong_tick.emit()
