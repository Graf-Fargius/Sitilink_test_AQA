from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_app import Base

class Login_page(Base):

    url="https://www.citilink.ru/"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

        # loacators

    user_name = "//input[@name='login']"
    password = "//input[@name='pass']"
    main_button = "//button[@class='e4uhfkv0 css-1yh1imp e4mggex0']"
    main_word = "//span[@class='en3k2720 e106ikdt0 css-1rzz8dw e1gjr6xo0']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_main_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_button)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_main_word(self):
        self.get_main_word().click()
        print("Click login button")

    def click_main_button(self):
        self.get_main_button().click()
        print("Click login button")

        # Methods

    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_word(self.get_main_word(), 'Войти')
        self.click_main_word()
        self.input_user_name("89656527610")
        self.input_password("Piperoni-1")
        self.click_main_button()










