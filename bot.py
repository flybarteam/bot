from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random
from pyautogui import press
print('Brukernavn')
username = input()
print('Passord')
password = input()
driver = webdriver.Chrome()


def site_login():
    driver.get('https://www.nordicmafia.org/login.php')
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
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
        driver.find_element_by_name('sellAllVehicles').click()
        press('enter')


    except NoSuchElementException:
        None
    print('Gjort biltyveri')

def prison():
    tmpText = (driver.find_element_by_class_name('bheader').text)
    if tmpText == 'MÅ VENTE':
        print('Venter...')
        time.sleep(180)


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

