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
import extract_text2



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
url='http://kbest-345.com/Login/Login.aspx'
driver.get(url)
driver.maximize_window()
driver.get_screenshot_as_file('C:/Users/jayta/Documents/repo/screenshot/login.png')
test_instance = extract_text2.ExtractText('C:/Users/jayta/Documents/repo/screenshot/login.png')
password = test_instance.preprocess_image()
#sc코드 삽입
driver.find_element_by_xpath('//*[@id="UserID"]').send_keys('ajtwoddl12')
driver.find_element_by_xpath('//*[@id="UserPass"]').send_keys('ajtwoddl12')
driver.find_element_by_xpath('//*[@id="captchaKey"]').send_keys(password+u'\ue007')
driver.get_screenshot_as_file('C:/Users/jayta/Documents/repo/screenshot/main.png')

#좌표값 찾기


#pyautogui.size()
#(1366, 768)
#pyautogui.click(x=719, y=465, clicks=1, interval=1, button='left')


