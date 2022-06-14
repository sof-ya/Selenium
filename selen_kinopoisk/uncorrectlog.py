from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def uncorrectlog():
    login_path = '//button[text()="Войти"]'
    phone_name = "login"
    out_path = "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[3]"
    browser = webdriver.Chrome(r'chromedriver.exe')
    browser.get('https://www.kinopoisk.ru')
    time.sleep(1)
    login_btn = browser.find_element_by_xpath(login_path)
    login_btn.click()
    time.sleep(1)
    phone_inp = browser.find_element_by_name(phone_name)
    phone_inp.clear()
    phone_inp.send_keys("111")
    phone_inp.send_keys(Keys.RETURN);
    time.sleep(2)
    out = browser.find_element_by_xpath(out_path)
    if out.text == ("Такой логин не подойдет"):
        print("Тест 2 сработал, логин не подходит")


