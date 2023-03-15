import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from base.base_app import Base

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #locators

    main_burger_button= "//button[@class='elgik370 e4uhfkv0 css-1q2qhth e4mggex0']"
    first_products_list= "//a[@href='/catalog/smartfony--main-xiaomi/?ref=mainmenu']"
    search_second_products_list= "//input[@placeholder='Поиск по товарам']"
    first_product="//a[@title='Смартфон Xiaomi Poco M5s 4/128Gb,  серый']"
    click_first_product="/html/body/div[6]/div[2]/main/section/div[1]/div[1]/div[3]/div[1]/section/div[4]/div[6]/div[2]/div[1]/div[1]/button"
    cart_busket= "//div[@class='HeaderMenu__buttons  HeaderMenu__buttons_basket']"
    filter_for_second_product="//div[@data-meta-value='Товары со скидкой']"
    check_box_for_second_product="//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[3]/div[6]/div[2]/div/div[1]/div/div/div/div/div/div[9]/div/label/span[2]/span"
    second_product="//*[@id='__next']/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[2]/button"
    cart_main_page= "//a[@href='/order/']"




    #Getters

    def get_main_burger_button(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_burger_button)))

    def get_first_products_list(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_products_list)))

    def get_search_second_products_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_second_products_list)))

    def get_first_product(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_product)))

    def get_click_first_product(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_first_product)))

    def get_cart(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_busket)))


    def get_filter_for_second_product(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_for_second_product)))

    def get_check_box_for_second_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_for_second_product)))

    def get_second_product(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.second_product)))

    def get_cart_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_main_page)))



    # Actions

    def click_main_burger_button(self):
        self.get_main_burger_button().click()
        print("Click main burger button")

    def click_first_products_list(self):
        self.get_first_products_list().click()
        print("Click first products list")

    def click_first_product_button(self):
        action=ActionChains(self.driver)
        gpt=self.driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/main/section/div[1]/div[1]/div[3]/div[1]/section/div[4]/div[5]/div/div/div[1]/p")
        action.move_to_element(gpt).perform()
        self.get_click_first_product().click()
        print("Click first product")


    def click_search_second_products_list(self):
        self.get_search_second_products_list().click()
        self.get_search_second_products_list().send_keys("Ноутбук")
        time.sleep(3)
        self.get_search_second_products_list().send_keys(Keys.ENTER)
        time.sleep(3)
        print("Start searching list of second product")


    def executing_filters(self):
        action = ActionChains(self.driver)
        action.move_to_element((self.driver.find_element(By.XPATH,"//div[@data-meta-value='Товары со скидкой']"))).perform()


    def hold_price_slider(self):
        action = ActionChains(self.driver)
        slider_1=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[2]/div[3]/div/div[4]")
        action.click_and_hold(slider_1).move_by_offset(100,0).release().perform()
        slider_2=self.driver.find_element(By.XPATH,"//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[2]/div[3]/div/div[5]")
        action.click_and_hold(slider_2).move_by_offset(-100, 0).release().perform()
        time.sleep(1)
        print("Hold Slider")

    def scroll_to_check_box_for_second_product(self):
        action = ActionChains(self.driver)
        check_box_for_second_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-meta-value='Ryzen 7']")))
        action.move_to_element(check_box_for_second_product).release().perform()
        print("Scrolling done")

    def click_check_box_for_second_product(self):
        self.get_check_box_for_second_product().click()
        print("Click check box")

    def click_second_product(self):
        action = ActionChains(self.driver)
        product_2 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[2]/button")))
        action.move_to_element(product_2).release().perform()
        self.get_second_product().click()
        print("Choice second product")

    def click_cart(self):
        self.get_cart().click()
        print("Click on Cart")

    def click_cart_2(self):
        self.get_cart_2().click()




        #Methods


    def select_products_1(self):
        self.get_current_url()
        self.get_main_burger_button()
        self.click_main_burger_button()
        self.get_first_products_list()
        self.click_first_products_list()
        self.click_first_product_button()
        self.click_cart()
        self.assert_url("https://www.citilink.ru/order/")
        self.get_screenshot()


    def select_products_2(self):
        self.get_search_second_products_list()
        self.click_search_second_products_list()
        self.get_search_second_products_list()
        self.executing_filters()
        self.hold_price_slider()
        self.scroll_to_check_box_for_second_product()
        self.click_check_box_for_second_product()
        self.click_second_product()
        self.click_cart_2()
        self.get_screenshot()







