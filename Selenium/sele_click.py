from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('chromedriver')

driver.get(url='https://www.naver.com/') 

driver.implicitly_wait(5)

search_box = driver.find_element_by_xpath('//*[@id="query"]')

search_box.send_keys('Selenium')
search_box.send_keys(Keys.ENTER)

# 첫번째 검색 결과를 클릭해서 접속해보기
posting = driver.find_element_by_xpath('//*[@id="web_1"]/div/div[1]/div[2]/a')
posting.click() # 클릭

sleep(5)

driver.close()