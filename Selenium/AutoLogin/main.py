from selenium import webdriver
from selenium.webdriver.common.by import By # https://hyunsooworld.tistory.com/entry/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%98%A4%EB%A5%98-AttributeError-WebDriver-object-has-no-attribute-findelementbycssselector-%EC%98%A4%EB%A5%98%ED%95%B4%EA%B2%B0
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from time import sleep
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()        
    
    def initUI(self):
        # Components
        self.textEdit_id = QLineEdit(self)
        # self.textedit1.setPlaceholderText("Id")
        
        self.textEdit_pw = QLineEdit(self)
        self.textEdit_pw.setEchoMode(QLineEdit.Password) # 패스워드 모드로 설정
        # self.textedit2.setPlaceholderText("PW")
        
        ok_btn = QPushButton("OK", self)
        ok_btn.clicked.connect(self.okClicked)
        
        # Layout
        grid = QGridLayout()
        self.setLayout(grid)
        
        grid.addWidget(QLabel('ID'), 0, 0)
        grid.addWidget(self.textEdit_id, 0, 1)
        
        grid.addWidget(QLabel('PW'), 1, 0)
        grid.addWidget(self.textEdit_pw, 1, 1)
        
        grid.addWidget(ok_btn, 2, 1)
        
        self.setWindowTitle("Auto Login")
        self.setGeometry(300, 300, 400, 300)
        self.show()
        
    def okClicked(self):       
        driver = webdriver.Chrome(r'./chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        
        # 1. tcafe (00:00)
        driver.get('https://tcafe2a.com/')
        driver.implicitly_wait(3)

        # 1-1. 로그인 파트
        driver.find_element(By.NAME, 'mb_id').send_keys(self.textEdit_id.text()) # 태그의 name값으로 추출
        driver.find_element(By.NAME, 'mb_password').send_keys(self.textEdit_pw.text())
        driver.find_element(By.XPATH, '//*[@id="ol_before"]/form/fieldset/div[1]/span[2]/button').click()
        
        # 1-2. 출석
        driver.get('https://tcafe2a.com/community/attendance')
        driver.find_element(By.XPATH, '//*[@id="cnftjr"]/div/form/table/tbody/tr/td/img').click()
        sleep(2)

        # 2. netpx (00:00)
        driver.get('https://www.netpx.co.kr/app/member/login?target_url=%2Fapp%2F')
        driver.implicitly_wait(3) # 3초간 로딩을 기다린다

        # 2-1. 로그인 파트
        driver.find_element(By.XPATH, '//*[@id="form"]/div[1]/input').send_keys(self.textEdit_id.text()) # 태그의 name값으로 추출
        driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/input').send_keys(self.textEdit_pw.text()) # 비번 특문제거 
        driver.find_element(By.XPATH, '//*[@id="form"]/div[3]/input').click()

        # 2-2. 출석 파트
        driver.get('https://www.netpx.co.kr/app/event/attend_check/8')
        driver.find_element(By.XPATH, '//*[@id="flashArea"]/form/div[1]/div[2]/a/img').click()
        try :
            alert = driver.switch_to.alert
            alert.accept()
            
        except :
            pass
        sleep(2)

         # 3. 퀘이사존 (09:00)
        driver.get('https://quasarzone.com/login?nextUrl=https://quasarzone.com/')
        driver.implicitly_wait(3) 

        driver.find_element(By.XPATH, '//*[@id="login_id"]').send_keys(self.textEdit_id.text())
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.textEdit_pw.text())
        driver.find_element(By.XPATH, '//*[@id="frm"]/div/div[1]/p/a').click()

        driver.get('https://quasarzone.com/users/attendance')
        driver.implicitly_wait(3)

        driver.find_element(By.CLASS_NAME, 'active2').click()
        driver.implicitly_wait(3)

        try :
            alert = driver.switch_to.alert
            alert.accept()
        except :
            pass
        sleep(2)

        driver.quit()
        
if __name__ == '__main__':       
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec()
