from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080') 

driver = webdriver.Chrome('chromedriver', options=options) # 크기 설정 매개변수로 주고, 크롬 실행
driver.implicitly_wait(5) # 암시적 대기 5초

driver.get(url='https://www.google.com/') # 구글 접속

search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
#xpath를 이용해 요소 찾기.

search_box.send_keys('Selenium') # 'Selenium'을 검색창에 검색
search_box.send_keys(Keys.RETURN) # 검색 시작

elements = driver.find_elements_by_xpath('//*[@id="rso"]/div[*]/div/div[1]/a/h3/span')

filename = 'selen_test2_output.txt'
file=open(filename, 'w', encoding='utf-8') # 프로그램 시작 시 텍스트 파일을 초기화

for element in elements:
    print(element.text)
    print(element.text, file=open(filename, 'a', encoding='utf-8')) # 출력된 결과를 utf-8 텍스트 파일로 저장

sleep(3)
driver.close()