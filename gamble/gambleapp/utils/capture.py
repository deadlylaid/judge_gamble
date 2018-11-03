
"""
1.주소값/id/pass 겟 후 해당주소 접속
2.[id/pass 입력후 로그인 버튼 클릭]
3.결제좌표값 수신
4.해당 좌표 클릭
"""
from selenium import webdriver
import pyautogui


driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.set_page_load_timeout(30)

driver.implicitly_wait(1)
url = 'http://htht-3.com/main.asp?abc'
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('ID')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('비밀번호' + u'\ue007')

driver.get_screenshot_as_file('C:/Users/jayta/Documents/repo/screenshot/1.png')

pyautogui.size()
(1366, 768)
pyautogui.click(x=719, y=465, clicks=1, interval=1, button='left')