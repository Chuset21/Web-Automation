from selenium import webdriver, common
import time


def main():
    chrome = webdriver.Chrome('chromedriver.exe')
    chrome.maximize_window()
    chrome.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

    assert 'Selenium Easy Demo' in chrome.title
    button = chrome.find_element_by_class_name('btn-default')

    time.sleep(1)
    popup = chrome.find_element_by_id('at-cv-lightbox-close')
    try:
        popup.click()
    except (common.exceptions.NoSuchElementException, common.exceptions.StaleElementReferenceException):
        pass

    assert 'Show Message' in chrome.page_source

    user_message = chrome.find_element_by_id('user-message')
    user_message.clear()
    message = 'Silly message'
    user_message.send_keys(message)

    button.click()
    output_message = chrome.find_element_by_id('display')

    assert message in output_message.text

    chrome.quit()


if __name__ == '__main__':
    main()
