import selenium
from selenium import webdriver

from selenium.webdriver import ActionChains #?

from selenium.webdriver.common.keys import Keys #?
from selenium.webdriver.common.by import By #?

from selenium.webdriver.support import expected_conditions as EC #?
from selenium.webdriver.support.ui import Select #?
from selenium.webdriver.support.ui import WebDriverWait #?

path = 'G:\Git\Python_Projects\Selenium\chromedriver' # 절대 경로로 지정
URL = 'http://www.google.com' # 접속할 사이트


#창 크기 설정
options = webdriver.ChromeOptions() # 크롬 옵션
options.add_argument('window-size=1920,1080')


driver = webdriver.Chrome(path, options=options)


driver.get(url=URL)



print(driver.current_url) # 현재 url 얻기

'''
driver.close() # 브라우저 닫기
'''

# 로딩 대기
# 찾으려는 element가 로드될 때 까지 지정한 시간만큼 대기한다.

'''
# 암묵적 대기 - 간단히 대기
driver.implicitly_wait(time_to_wait=5) # 5초간 대기 
'''

# 명시적 대기 - 필요한 원소를 콕 찝어 걔가 나올때 까지 대기.
# import By, WebDriverWait, expected_conditions를 이용
try:
    #5초마다 재시도
    element = WebDriverWait(driver, 5).until( 
        EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
        # 요소가 있으면 True를, 없으면 False를 반환한다.
        '''
        요소는 다양하게 설정 가능
        제목이 어떤 문자열인지, 어떤 문자열을 포함하는지, 
        특정/모든 요소가 로드되었거나/볼 수 있거나/볼 수 없거나/클릭 가능하거나 등등의 
        여러 조건이 가능하다.

        혹은 Custom으로 __init__ 함수와 __call__함수를 구현한 class로 조건을 설정하는 것도 가능하다. 
        ''' 
    )

finally:
    driver.quit()