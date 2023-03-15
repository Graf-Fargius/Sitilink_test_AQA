import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.main_page import Main_page
from base.base_app import Base

class Cart_page(Main_page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #locators

    accept_purchase= "//button[@title='Перейти к оформлению']"
    first_product_price="//*[@id='__next']/div/main/div[1]/div[2]/section/div[1]/div/div/div[1]/div[4]/div/div[2]/span/span/span[1]"
    second_product_price="//*[@id='__next']/div/main/div[1]/div[2]/section/div[1]/div/div/div[2]/div[4]/div/div[2]/span/span/span[1]"
    button_clear_cart="//*[@id='__next']/div/main/div[1]/div[2]/section/div[2]/div/div[1]/div[2]/button[2]/span/div[2]/span"



    #Getters

    def get_accept_purchase(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_purchase)))

    def get_first_product_price(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_product_price)))

    def get_second_product_price(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.second_product_price)))

    def get_button_clear_cart(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_clear_cart)))





    # Actions

    def click_accept_purchase(self):
        self.get_accept_purchase().click()
        print("Click accept purchase")

    def check_prices(self):
        action=ActionChains(self.driver)
        get_perfmon_order=WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='css-1xdhyk6 e1hf2t4f0']")))
        action.move_to_element(get_perfmon_order).release().perform()
        print("Scroll itog prices")


    def click_button_clear_cart(self):
        self.get_button_clear_cart().click()
        print("Click button cart")


        #Methods


    def accept_product(self):
        self.get_current_url()
        self.get_accept_purchase()
        self.click_accept_purchase()
        self.check_prices()
        self.test_value('//*[@id="__next"]/div/div[2]/div/div/div/div/div[1]/div[4]/div/div[2]/div/div/div[5]/div/div[1]/div/div/span[2]/span')
        self.get_screenshot()

    def clear_cart_products(self):
        self.click_cart_2()
        self.click_button_clear_cart()
        self.get_screenshot()








