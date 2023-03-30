from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def auth_yandex_func(login, password):
    url = 'https://passport.yandex.ru/auth/list'
    s = Service(r'path-to-file')
    browser = webdriver.Chrome(service=s)
    browser.get(url=url)
    time.sleep(3)

    try:
        email_input = browser.find_element("id", "passp-field-login")
        email_input.clear()
        email_input.send_keys(login)

        email_button = browser.find_element("id", 'passp:sign-in').click()
        time.sleep(5)
        try:
            error_message = browser.find_element('id', 'field:input-login:hint')
            error_text = error_message.text
            return error_text
        except:
            pass

        pass_input = browser.find_element('id', 'passp-field-passwd')
        pass_input.clear()
        pass_input.send_keys(password)

        pass_button = browser.find_element('id', 'passp:sign-in').click()
        time.sleep(3)
        try:
            error_message = browser.find_element('id', 'field:input-passwd:hint')
            error_text = error_message.text
            return error_text
        except:
            pass


        browser.close()
        browser.quit()
        result = 'Успешная авторизация'
        return result

    except Exception as e:
        print(e)
        browser.close()
        browser.quit()

if __name__ == '__main__':
    login = ''
    password = ''
    error_text = auth_yandex_func(login, password)