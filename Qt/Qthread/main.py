from PySide6.QtWidgets import *
from PySide6.QtCore import *
from time import sleep
from main_ui import Ui_Form

class MyThread(QThread):
    mySignal = Signal(int, int)  # int형 타입을 보내는 Signal 생성
    stop = False
    def __init__(self):
        super().__init__()

    def run(self):  # start하면 run이 실행된다. 약속되어있는 메서드명임!!
        for i in range(5):
            for x in range(101):
                while self.stop:
                    sleep(0.05)

                self.mySignal.emit(i, x)  # int 시그널을 보냄 i번쨰 progressbar를 x로 설정해라!
                sleep(0.05)

class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.th = MyThread()  # 위에서 정의한 MyThread Class 사용
        self.th.mySignal.connect(self.setValue)  # 시그널을 받으면 처리하는 메서드

        self.main()

    def main(self):
        self.pros = [] # 배열 생성
        lay = self.verticalLayout

        for i in range(lay.count()):
            self.pros.append(lay.itemAt(i).widget())  # Vlay의 위젯을 가져와 pros 배열에 넣음
            self.pros[i].setValue(0)

    def setValue(self, i, x):
        self.pros[i].setValue(x)

    def go(self):
        self.th.stop = False
        self.th.start()  # 버튼을 누르면 스레드 시작

    def stop(self):
        self.th.stop = True


app = QApplication([])
win = MyApp()
win.show()
app.exec()