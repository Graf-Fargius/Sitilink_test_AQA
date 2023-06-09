import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver

class Base():
    def __init__(self, driver):
        self.driver=driver

        """Method Get current url"""

    def get_current_url(self):
        get_url=self.driver.current_url
        print("current url " + get_url)

        """Method assert word"""

    def assert_word(self,word,result):
        value_word=word.text
        assert value_word==result
        print("Good value word")


        """Method read text"""

    def product_value(self, word):
        price_product_value = self.driver.find_element(By.XPATH, word)
        price_product_value_1=price_product_value.text
        print(price_product_value_1)



        """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screeenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('.\\screen\\' + name_screeenshot)
        print("Screenshot is done")

        """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url==result
        print("Good value url")

