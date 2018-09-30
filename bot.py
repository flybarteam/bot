from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random

driver = webdriver.Safari()



def site_login():
    driver.get('https://www.nordicmafia.org/login.php')
    driver.find_element_by_name('username').send_keys('FlygendeNordmann')
    driver.find_element_by_name('password').send_keys('Freak123123')
    driver.find_element_by_name('login').click()
    time.sleep(random.uniform(1, 2))

def crime():
    randomNumber = random.randint(1, 5)
    time.sleep(2)
    driver.find_element_by_link_text('Kriminalitet').click()
    time.sleep(2)
    try:
        if randomNumber == 1:
            driver.find_element_by_id('rowid_table_select_krimaction0').click()
        if randomNumber == 2:
            driver.find_element_by_id('rowid_table_select_krimaction1').click()
        if randomNumber == 3:
            driver.find_element_by_id('rowid_table_select_krimaction2').click()
        if randomNumber == 4:
            driver.find_element_by_id('rowid_table_select_krimaction3').click()
        if randomNumber == 5:
            driver.find_element_by_id('rowid_table_select_krimaction4').click()
    except NoSuchElementException:
        None

def blackmail():
    driver.find_element_by_link_text('Utpressing').click()
    time.sleep(2)
    driver.find_element_by_id('sel_1').click()
    driver.find_element_by_name('submitBlackmail').click()


site_login()
blackmail()
crime()

