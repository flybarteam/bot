from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random

driver = webdriver.Safari()



def site_login():
    driver.get('https://www.nordicmafia.org/login.php')
    driver.find_element_by_name('username').send_keys('FlygendeNordmann')
    driver.find_element_by_name('password').send_keys('')
    driver.find_element_by_name('login').click()
    time.sleep(random.uniform(2, 3))

def crime():
    randomNumber = random.randint(1, 5)
    driver.find_element_by_link_text('Kriminalitet').click()
    time.sleep(random.uniform(1, 2))
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
    print('Gjort kriminalitet')
    time.sleep(random.uniform(1, 2))

def blackmail():
    driver.find_element_by_link_text('Utpressing').click()
    time.sleep(random.uniform(1, 2))
    try:
        driver.find_element_by_id('sel_1').click()
        driver.find_element_by_name('submitBlackmail').click()
    except NoSuchElementException:
        None
    print('Gjort utpressing')
    time.sleep(random.uniform(2, 3))


def carTheft():
    randomNumber = random.randint(1, 4)
    driver.find_element_by_link_text('Biltyveri/Garasje').click()
    time.sleep(random.uniform(2, 3))
    try:
        if randomNumber == 1:
            driver.find_element_by_id('rowid_table_select_gtaaction0').click()
        if randomNumber == 2:
            driver.find_element_by_id('rowid_table_select_gtaaction1').click()
        if randomNumber == 3:
            driver.find_element_by_id('rowid_table_select_gtaaction2').click()
        if randomNumber == 4:
            driver.find_element_by_id('rowid_table_select_gtaaction3').click()
    except NoSuchElementException:
        None
    try:
        driver.find_element_by_css_selector('background-color: #ff4c4c;').click()
    except NoSuchElementException:
        None
    try:
        driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/span/span[2]').click()
        print('klikket på teksten')
    except:
        print('Fant ikkje fengselteksten')
    print('Gjort biltyveri')





site_login()
while True:
    crime()
    blackmail()
    carTheft()
    time.sleep(random.uniform(180, 200))
    crime()
    time.sleep(random.uniform(180, 200))
    crime()
    carTheft()
    time.sleep(random.uniform(180, 200))
    crime()
    time.sleep(random.uniform(180, 200))
    crime()
    carTheft()
    time.sleep(random.uniform(180, 200))
    crime()
    time.sleep(random.uniform(180, 200))




