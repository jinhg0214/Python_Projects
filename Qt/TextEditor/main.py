from PySide6.QtWidgets import *
from PySide6.QtGui import *

# 2. 종료 이벤트
class MainWindow(QMainWindow)  :
    def closeEvent(self, e):
        if not text.document().isModified(): # 변경된 내용이 없다면 그냥 끔
            return
        answer = QMessageBox.question(
            window, None, "SAVE or NOT",
            QMessageBox.Save |
            QMessageBox.Discard |
            QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
        elif answer & QMessageBox.Cancel:
            e.ignore()

app = QApplication([])
# 프로그램 이름 표시
app.setApplicationName("MEMO")

# 메인 윈도우 위젯
window = MainWindow()
text = QPlainTextEdit()
window.setCentralWidget(text) # 메뉴바와 충돌을 막기 위해 cetral widget 이용
#################################################################################
# 1.메뉴바 관련
# 1.메뉴바 관련 - 1.menu
menu = window.menuBar().addMenu("&File") # 윈도우 메뉴 바에 menu객체 추가.

# 1.메뉴바 관련 - 2.About
help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)

def show_about_dialog():
    text = "<center>" \
           "<h1>Text Editor</h1>" \
           "</center>" \
           "<p>Version 1.2.3<br>" \
           "Copyright Mincoding</p>"
    QMessageBox.about(window, "About", text)
about_action.triggered.connect(show_about_dialog) # 연결
#################################################################################

file_path = None # 초기 경로는 없음

# 1.메뉴바 관련 - 1.menu - 1. Save
save_action = QAction("&Save")
def save():
    if file_path is None: # 저장된 경로가 없다면 경로창 열기
        save_as()
    else:
        with open(file_path, "w") as f: # 이미 경로가 있다면 거기다 저장
            f.write(text.toPlainText()) # 저장은 save에서만 일어나게됨
            text.document().setModified(False)

save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence("Ctrl+S"))
menu.addAction(save_action)

# 1.메뉴바 관련 - 1.menu - 2. Save_As
save_as_action = QAction("Save &As...")
def save_as():
    global file_path # 전역변수 가져오기
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path: 
        file_path = path #전역변수 경로에 저장한 뒤 save 호출
        save()
save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)

# 1.메뉴바 관련 - 1.menu - 3. oepn
open_action = QAction("&Open")
def open_file():
    path = QFileDialog.getOpenFileName(window, "Open File")[0] # 위젯, 창 이름
    if path:
        text.setPlainText(open(path).read()) # 경로의 파일을 읽어 문자열로 가져옴
open_action.triggered.connect(open_file)
open_action.setShortcut(QKeySequence("Ctrl+O")) # 단축키 설정 QtGui의 QKeySequence
menu.addAction(open_action)

# 1.메뉴바 관련 - 1.menu - 4.close
close = QAction("&Close") # 프로그램 종료. QAction은 PySide6부터는 QtGui에서 사용
close.triggered.connect(window.close) # 호출되면 윈도우 종료 함수 호출
menu.addAction(close) # 메뉴에 달기
#################################################################################
window.show()
app.exec()