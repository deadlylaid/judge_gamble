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
from selenium.common.exceptions import TimeoutException
import pyautogui

#def find_id():
#    num=0
#    id = ['userid', 'id', 'name','username']
#    for i in id:
#       driver.find_element_by_xpath('//*[@id='+id[num]+']').send_keys('ID')
#        num=num+1        

#def find_pass():
#    num=0
#    passwd = ['pass','password','pswd','passwd','passwrd']
#    for i in passwd:
#        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('비밀번호')
#        num=num+1
        

driver = webdriver.Chrome(executable_path=r'C:/Users/jayta/Documents/repo/package/chromedriver.exe')
driver.set_page_load_timeout(30)

driver.implicitly_wait(1)
url='http://htht-3.com/main.asp?abc'
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('ID')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('비밀번호'+u'\ue007')

driver.get_screenshot_as_file('C:/Users/jayta/Documents/repo/screenshot/1.png')

pyautogui.size()
(1366, 768)
pyautogui.click(x=719, y=465, clicks=1, interval=1, button='left')


