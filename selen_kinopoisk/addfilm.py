import sys

from auth_data import KINOPOISK
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from loginin import loginin

import time

def addfilm():
    strsearch_name = "kp_query"
    advtime_path = '/html/body/main/div[4]/div[1]/table/tbody/tr/td[1]/div/div[2]/div/div[2]/p/a'
    willwatch_button_path = '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/button'
    myfilms_button_path = '/html/body/div[1]/div[2]/div[1]/header/div/div[3]/div/a'
    myadvtime_path = '/html/body/main/div[4]/div[1]/table/tbody/tr/td/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/div[2]/ul/li/div[4]/a'
    browser = webdriver.Chrome(r'chromedriver.exe')
    browser.get('https://www.kinopoisk.ru')
    time.sleep(1)
    loginin(browser, 'sofja.kulickowa', KINOPOISK)
    searchstr = browser.find_element_by_name(strsearch_name)
    searchstr.clear()
    searchstr.send_keys("Время приключений")
    searchstr.send_keys(Keys.RETURN)
    time.sleep(5)
    advtime = browser.find_element_by_xpath(advtime_path)
    advtime.click()
    time.sleep(2)
    willwatchbut = browser.find_element_by_xpath(willwatch_button_path)
    willwatchbut.click()
    time.sleep(2)
    myfilmsbut = browser.find_element_by_xpath(myfilms_button_path)
    myfilmsbut.click()
    time.sleep(5)
    myadvtime = browser.find_element_by_xpath(myadvtime_path)
    if myadvtime.text == "Время приключений (сериал)":
        print("Тест 4 сработал, фильм ", myadvtime.text, " добавлен")



