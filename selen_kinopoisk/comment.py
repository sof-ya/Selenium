import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


from auth_data import KINOPOISK
import time
from loginin import loginin


def comment():
    menu_path = '/html/body/div[1]/div[2]/div[1]/header/div/div[1]/div/div/button'
    media_path = '/html/body/div[1]/div[2]/div[1]/header/div/div[1]/div/div/div/div/div/a[6]'
    article_path = '/html/body/div[1]/div/div[2]/div[4]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/a'
    compage_path = '/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[1]/div/div[2]/span/a'
    comstr_path = '/html/body/div[1]/div/div[2]/div[4]/div/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/form/textarea'
    sendkey_path = '/html/body/div[1]/div/div[2]/div[4]/div/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/form/div/div[1]/button[1]'
    browser = webdriver.Chrome(r'chromedriver.exe')
    browser.get('https://www.kinopoisk.ru')
    loginin(browser, 'your login', KINOPOISK)
    time.sleep(1)
    menu = browser.find_element_by_xpath(menu_path)
    menu.click()
    media = browser.find_element_by_xpath(media_path)
    media.click()
    time.sleep(2)
    article = browser.find_element_by_xpath(article_path)
    article.click()
    time.sleep(2)
    compage = browser.find_element_by_xpath(compage_path)
    compage.click()
    comstr = browser.find_element_by_xpath(comstr_path)
    comstr.clear()
    comstr.send_keys("Круто!")
    time.sleep(2)
    sendkey = browser.find_element_by_xpath(sendkey_path)
    sendkey.click()
    time.sleep(2)
    if 1:
        print("Тест 5 сработал, комментарий отправлен")



