import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

import time


def findfilm():
    search_path = '/html/body/div[1]/div[2]/div[1]/header/div/div[2]/div[2]/div/form/div/div/a'
    year_path = "m_act[year]"
    select_country_id = 'country'
    select_ganre_id = "m_act[genre]"
    select_film_path = "m_act[content_find]"
    search_button_path = '/html/body/main/div[4]/div[1]/table/tbody/tr/td[1]/div/table/tbody/tr[3]/td/div/form[1]/input[11]'
    first_film_path = "/html/body/main/div[4]/div[1]/table/tbody/tr/td[1]/div/div[2]/div/div[2]/p/a"
    browser = webdriver.Chrome(r'chromedriver.exe')
    browser.get('https://www.kinopoisk.ru')
    time.sleep(1)
    adv_search = browser.find_element_by_xpath(search_path)
    adv_search.click()
    manifyear = browser.find_element_by_name(year_path)
    manifyear.clear()
    manifyear.send_keys("1994")
    selectcoun = Select(browser.find_element_by_id(select_country_id))
    selectcoun.select_by_visible_text('США')
    selectgan = Select(browser.find_element_by_id(select_ganre_id))
    selectgan.select_by_visible_text('драма')
    selectfilm = Select(browser.find_element_by_name(select_film_path))
    selectfilm.select_by_visible_text('фильм')
    time.sleep(5)
    searchbut = browser.find_element_by_xpath(search_button_path)
    searchbut.click()
    firstfilm = browser.find_element_by_xpath(first_film_path)
    if firstfilm.text == "Побег из Шоушенка":
        print("Тест 3 сработал, вы нашли фильм", firstfilm.text)


