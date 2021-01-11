'''
1. Ctrl + Shift + C 로 요소를 찾는다.
2. 해당 요소의 정보에서, Elements 확인
3. Copy Elements 또는 Copy Xpath, class등으로 원하는 요소 복사
    ex) 구글 검색바
    Elements : <input id="input" type="search" autocomplete="off" spellcheck="false" aria-live="polite" placeholder="Google 검색 또는 URL 입력">
    Xpath    : //*[@id="input"]


'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080') 

driver = webdriver.Chrome('chromedriver', options=options) # 크기 설정 매개변수로 주고, 크롬 실행
driver.get(url='https://www.google.com/') # 구글 접속

driver.implicitly_wait(5) # 암시적 대기 5초

search_box = driver.find_element_by_class_name('gLFyf') #class이름이 gLFyf인 요소를 검색하여

search_box.send_keys('Selenium') # 검색창에 'Selenium' 텍스트를 입력


sleep(10)

driver.close()