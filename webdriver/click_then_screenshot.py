# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
1.주소값/id/pass 겟 후 해당주소 접속
2.[id/pass 입력후 로그인 버튼 클릭]
3.결제좌표값 수신
4.해당 좌표 클릭
"""
from selenium import webdriver
import pyautogui

driver = driver = webdriver.Chrome(executable_path=r'C:/Users/jayta/Documents/repo/package/chromedriver.exe')
driver.implicitly_wait(3)
url='https://nid.naver.com/nidlogin.login'
driver.get(url)
driver.maximize_window()

driver.find_element_by_name('id').send_keys('jay_tester')
driver.find_element_by_name('pw').send_keys('dbswodnd')

driver.get_screenshot_as_file('C:/Users/jayta/Documents/repo/screenshot/1.png')
pyautogui.size()
(1366, 768)

pyautogui.click(x=719, y=465, clicks=1, interval=1, button='left')
