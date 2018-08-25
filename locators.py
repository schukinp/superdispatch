from selenium.webdriver.common.by import By

class HomePageLocators(object):
    EMAIL_INPUT = (By.ID, 'userSignInFormEmail')
    PASSWORD_INPUT = (By.ID, 'user_password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[value="Sign in"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'p.flash.error')

class UserPageLocators(object):
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Search books"]')
    SEARCH_RESULTS_BUTTON = (By.XPATH, '//button[contains(@class, "gr-bookSearchResults")]')
    WANT_TO_READ_BUTTON = (By.CSS_SELECTOR, 'button.wtrToRead')
    BOOKS = (By.CSS_SELECTOR, 'tr[itemtype="http://schema.org/Book"]')
    MARK_AS_READ_BUTTON = (By.CSS_SELECTOR, 'button[value="read"]')
    DROPDOWN_SELECT = (By.CSS_SELECTOR, 'button.wtrShelfButton')
    FEEDBACK_TEXTAREA = (By.NAME, 'review[review]')
    RATING = (By.CSS_SELECTOR, 'div.formItem > div > a.star.off')
    READ_TODAY_BUTTON = (By.CSS_SELECTOR, 'div.startedAtSetToday > a.startedAtSetTodayLink.gr-button')
    DAY_SELECTOR = (By.CSS_SELECTOR, 'select.rereadDatePicker.smallPicker.startDay')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'input[value="Save"]')
    PROFILE_IMAGE = (By.CSS_SELECTOR, 'div.dropdown.dropdown--profileMenu')
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, 'a[href="/user/sign_out"]')
