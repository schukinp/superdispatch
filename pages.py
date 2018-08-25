from locators import *
from elements import *
from random import choice
from string import ascii_letters
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class EmailInput(BaseFormElement):
    locator = HomePageLocators.EMAIL_INPUT

class PasswordInput(BaseFormElement):
    locator = HomePageLocators.PASSWORD_INPUT

class SearchInput(BaseFormElement):
    locator = UserPageLocators.SEARCH_INPUT

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    email_input = EmailInput()
    password_input = PasswordInput()

    def click_sign_in_button(self):
        element = self.driver.find_element(*HomePageLocators.SIGN_IN_BUTTON)
        element.click()

    def get_error(self):
        try:
            element = self.driver.find_element(*HomePageLocators.ERROR_MESSAGE)
            return element.text
        except:
            print('Message not found')

class UserPage(BasePage):
    search_input = SearchInput()

    def wait(self, selenium):
        return WebDriverWait(selenium, 10)

    def click_search_results_button(self):
        element = self.driver.find_element(*UserPageLocators.SEARCH_RESULTS_BUTTON)
        element.click()

    def find_top_3_books(self):
        elements = self.driver.find_elements(*UserPageLocators.BOOKS)[:3]
        return elements

    def mark_want_to_read(self):
        for el in self.find_top_3_books():
           element = el.find_element(*UserPageLocators.WANT_TO_READ_BUTTON)
           element.click()

    def mark_as_read_and_leave_feedback(self, selenium):
        books = self.find_top_3_books()
        for row in books:
            dropdown_selects = row.find_elements(*UserPageLocators.DROPDOWN_SELECT)
            for el in dropdown_selects:
                el.click()
                self.wait(selenium).until(EC.presence_of_element_located(UserPageLocators.MARK_AS_READ_BUTTON))
                element = self.driver.find_element(*UserPageLocators.MARK_AS_READ_BUTTON)
                element.click()
                self.wait(selenium).until(EC.presence_of_element_located(UserPageLocators.SAVE_BUTTON))
                self.set_rating()
                self.leave_feedback()
                self.set_read_date()
                self.click_save()
                sleep(2)

    def leave_feedback(self):
        string = ''.join(choice(ascii_letters) for i in range(10))
        element = self.driver.find_element(*UserPageLocators.FEEDBACK_TEXTAREA)
        element.clear()
        element.send_keys(string)

    def set_rating(self):
        elements = self.driver.find_elements(*UserPageLocators.RATING)
        element = choice(elements)
        element.click()

    def set_read_date(self):
        element = self.driver.find_element(*UserPageLocators.READ_TODAY_BUTTON)
        element.click()
        select = Select(self.driver.find_element(*UserPageLocators.DAY_SELECTOR))
        option = choice(select.options).text
        select.select_by_value(option)

    def click_save(self):
        element = self.driver.find_element(*UserPageLocators.SAVE_BUTTON)
        element.click()

    def click_profile(self):
        element = self.driver.find_element(*UserPageLocators.PROFILE_IMAGE)
        element.click()

    def click_sigin_out(self):
        element = self.driver.find_element(*UserPageLocators.SIGN_OUT_BUTTON)
        element.click()









