from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pro_ui import Ui_Form

class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):

        self.bang = "DOWN"
        self.tm = QTimer()
        self.tm.setInterval(100 - self.slider.value())
        self.tm.timeout.connect(self.run)

    def run(self):
        if self.bang == "DOWN" :
            self.pb.setValue(self.pb.value() + 1)
        else:
            self.pb.setValue(self.pb.value() - 1)

    def up(self):
        self.bang = "UP"
        self.tm.setInterval(100 - self.slider.value())
        self.tm.start()

    def down(self):
        self.bang = "DOWN"
        self.tm.setInterval(100 - self.slider.value())
        self.tm.start()

    def stop(self):
        self.tm.stop()

app = QApplication()
win = MyApp()

win.show()
app.exec()