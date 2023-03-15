import time

import pages.login_page
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from selenium.webdriver.chrome.options import Options

@pytest.mark.run(order=2)
def test_select_product_2(set_up):
    options=Options()
    options.add_experimental_option('excludeSwitches', ['enable-Logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

    print("Start Test 2")


    login = pages.login_page.Login_page(driver)
    login.autorization()



    mp = pages.main_page.Main_page(driver)
    mp.select_products_2()

    cp=pages.cart_page.Cart_page(driver)
    cp.accept_product()
    driver.quit()

