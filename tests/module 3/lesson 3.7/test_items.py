from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def check_exists_by_css_selector(browser ,selector):
    try:
        browser.find_element(By.CSS_SELECTOR, selector)
    except NoSuchElementException:
        return False
    return True


def test_user_should_see_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button_presence = check_exists_by_css_selector(browser, 'button.btn-add-to-basket')
    assert button_presence is True, 'Button is not present in DOM'
