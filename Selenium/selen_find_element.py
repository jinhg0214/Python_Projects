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
# send_keys(*value) 함수는 문자열 입력 가능. 
# enter와 같은 특수 키들은 '\ue006'로도 입력 가능하지만, Keys.RETURN/Keys.ENTER 등으로도 입력 가능함
'''
class Keys(object):
    """
    Set of special keys codes.
    """

    NULL = '\ue000'
    CANCEL = '\ue001'  # ^break
    HELP = '\ue002'
    BACKSPACE = '\ue003'
    BACK_SPACE = BACKSPACE
    TAB = '\ue004'
    CLEAR = '\ue005'
    RETURN = '\ue006'
    ENTER = '\ue007'
    SHIFT = '\ue008'
    LEFT_SHIFT = SHIFT
    CONTROL = '\ue009'
    LEFT_CONTROL = CONTROL
    ALT = '\ue00a'
    LEFT_ALT = ALT
    PAUSE = '\ue00b'
    ESCAPE = '\ue00c'
    SPACE = '\ue00d'
    PAGE_UP = '\ue00e'
    PAGE_DOWN = '\ue00f'
    END = '\ue010'
    HOME = '\ue011'
    LEFT = '\ue012'
    ARROW_LEFT = LEFT
    UP = '\ue013'
    ARROW_UP = UP
    RIGHT = '\ue014'
    ARROW_RIGHT = RIGHT
    DOWN = '\ue015'
    ARROW_DOWN = DOWN
    INSERT = '\ue016'
    DELETE = '\ue017'
    SEMICOLON = '\ue018'
    EQUALS = '\ue019'

    NUMPAD0 = '\ue01a'  # number pad keys
    NUMPAD1 = '\ue01b'
    NUMPAD2 = '\ue01c'
    NUMPAD3 = '\ue01d'
    NUMPAD4 = '\ue01e'
    NUMPAD5 = '\ue01f'
    NUMPAD6 = '\ue020'
    NUMPAD7 = '\ue021'
    NUMPAD8 = '\ue022'
    NUMPAD9 = '\ue023'
    MULTIPLY = '\ue024'
    ADD = '\ue025'
    SEPARATOR = '\ue026'
    SUBTRACT = '\ue027'
    DECIMAL = '\ue028'
    DIVIDE = '\ue029'

    F1 = '\ue031'  # function  keys
    F2 = '\ue032'
    F3 = '\ue033'
    F4 = '\ue034'
    F5 = '\ue035'
    F6 = '\ue036'
    F7 = '\ue037'
    F8 = '\ue038'
    F9 = '\ue039'
    F10 = '\ue03a'
    F11 = '\ue03b'
    F12 = '\ue03c'

    META = '\ue03d'
    COMMAND = '\ue03d'
'''

sleep(10)

driver.close()