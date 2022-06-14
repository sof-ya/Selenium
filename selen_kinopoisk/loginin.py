from selenium.webdriver.common.keys import Keys

import time

def loginin(browser, login, password):
    login_path = '//button[text()="Войти"]'
    phone_name = "login"
    password_path = "passp-field-passwd"
    avatar_path = "/html/body/div[1]/div[2]/div[1]/header/div/div[3]/div/div[2]/button/div/div/span"

    time.sleep(1)
    login_btn = browser.find_element_by_xpath(login_path)
    login_btn.click()
    time.sleep(1)
    phone_inp = browser.find_element_by_name(phone_name)
    phone_inp.clear()
    phone_inp.send_keys(login)
    phone_inp.send_keys(Keys.RETURN);
    time.sleep(1)
    password_inp = browser.find_element_by_id(password_path)
    password_inp.clear()
    password_inp.send_keys(password)
    password_inp.send_keys(Keys.RETURN);
    time.sleep(3)
    avatar = browser.find_element_by_xpath(avatar_path)
    if avatar.is_displayed():
        print("Регистрация пройдена, тест 1 сработал")