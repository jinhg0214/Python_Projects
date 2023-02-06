from selenium import webdriver
from selenium.webdriver.common.by import By # https://hyunsooworld.tistory.com/entry/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%98%A4%EB%A5%98-AttributeError-WebDriver-object-has-no-attribute-findelementbycssselector-%EC%98%A4%EB%A5%98%ED%95%B4%EA%B2%B0

driver = webdriver.Chrome(r'./chromedriver.exe')

# ID/PW 정의 부분
tcafe_id = 'test'
tcafe_pw = 'test!'

# 1. tcafe
driver.get('https://tcafe2a.com/')
driver.implicitly_wait(3)

# 1-1. 로그인 파트
driver.find_element(By.NAME, 'mb_id').send_keys(tcafe_id) # 태그의 name값으로 추출
driver.find_element(By.NAME, 'mb_password').send_keys(tcafe_pw) # 
driver.find_element(By.XPATH, '//*[@id="ol_before"]/form/fieldset/div[1]/span[2]/button').click()
 
# 1-2. 출석
tcafe_attendance_url = 'https://tcafe2a.com/community/attendance'
driver.get(tcafe_attendance_url)
driver.find_element(By.XPATH, '//*[@id="cnftjr"]/div/form/table/tbody/tr/td/img').click()

# driver.find_element_by_name('id').send_keys('아이디')
# driver.find_element_by_name('pw').send_keys('비밀번호')
# driver.find_element_by_id('loginBtn').click()
# N. 드라이버 종료
driver.quit()