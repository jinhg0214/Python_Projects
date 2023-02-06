from selenium import webdriver
from selenium.webdriver.common.by import By # https://hyunsooworld.tistory.com/entry/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%98%A4%EB%A5%98-AttributeError-WebDriver-object-has-no-attribute-findelementbycssselector-%EC%98%A4%EB%A5%98%ED%95%B4%EA%B2%B0

# driver = webdriver.Chrome(r'./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# ID/PW 정의 부분
# 일단은 콘솔로 입력받는다
user_id, user_pw = input('Input ID / PW : ').split()

# 1. tcafe
# driver.get('https://tcafe2a.com/')
# driver.implicitly_wait(3)

# # 1-1. 로그인 파트
# driver.find_element(By.NAME, 'mb_id').send_keys(user_id) # 태그의 name값으로 추출
# driver.find_element(By.NAME, 'mb_password').send_keys(user_pw) # 
# driver.find_element(By.XPATH, '//*[@id="ol_before"]/form/fieldset/div[1]/span[2]/button').click()
 
# # 1-2. 출석
# driver.get('https://tcafe2a.com/community/attendance')
# driver.find_element(By.XPATH, '//*[@id="cnftjr"]/div/form/table/tbody/tr/td/img').click()

# 2. netpx
driver.get('https://www.netpx.co.kr/app/member/login?target_url=%2Fapp%2F')
driver.implicitly_wait(3) # 3초간 로딩을 기다린다

# 2-1. 로그인 파트
driver.find_element(By.XPATH, '//*[@id="form"]/div[1]/input').send_keys(user_id) # 태그의 name값으로 추출
driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/input').send_keys(user_pw[:-1]) # 비번 특문제거 
driver.find_element(By.XPATH, '//*[@id="form"]/div[3]/input').click()

# 2-2. 출석 파트
driver.get('https://www.netpx.co.kr/app/event/attend_check/8')
driver.find_element(By.XPATH, '//*[@id="flashArea"]/form/div[1]/div[2]/a/img').click()

# 3. 퀘이사존


# N. 드라이버 종료
driver.quit()