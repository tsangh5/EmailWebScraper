from EmailWebScraper import results
from selenium import webdriver
import pyautogui
from time import sleep
from openpyxl import Workbook

# email = 'hinben1027'
# password = 'awesomedudes'
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://docs.google.com/spreadsheets/d/1RDv17WXW_3v6pwdvSplQg5QvLEWEY9TkVfxz7ybivAA/edit#gid=0')
# sleep(2)
# pyautogui.click(1986, 46)                                                             # click 'sign in'
# driver.find_element_by_xpath('//input[@name=\"identifier\"]').send_keys(email)          # enter email
# pyautogui.press('enter')                       # click 'next'
# sleep(60) 
# driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)         # enter SMART password
# pyautogui.click(1572, 921)                        # click submit
# pyautogui.click(112, 1394)
# pyautogui.click(158, 529)
# for email in results:
#     pyautogui.write(email)
#     pyautogui.press('down')
wb = Workbook()
ws = wb.active
for i in range(1, len(results)+1):
   try:
      ws[f'A{i}'] = results[i-1]
   except:
      wb.save('emails.xlsx') 
wb.save('emails.xlsx')