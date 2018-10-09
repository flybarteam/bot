from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random
import schedule
from pyautogui import press
from datetime import datetime
from tkinter import *

driver = webdriver.Chrome()


def site_login(username, password):
    driver.get('https://www.nordicmafia.org/login.php')
    time.sleep(1)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('login').click()


def crime(doCrime, randomNumber):
    if doCrime == 1:
        message = ''
        if randomNumber == 0:
            randomNumber = random.randint(1, 5)
        driver.find_element_by_link_text('Kriminalitet').click()
        time.sleep(random.uniform(1, 2))
        wait = driver.find_element_by_class_name('bheader').text
        if wait == 'MÅ VENTE - KRIMINALITET':
            message = 'Kan ikkje stjele, må vente'
        else:
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
            message = 'Gjort kriminalitet ' + str(datetime.now().time())
            return message
            time.sleep(random.uniform(1, 2))


def blackmail(doBlackmail):
    if doBlackmail == 1:
        message = ''
        driver.find_element_by_link_text('Utpressing').click()
        time.sleep(random.uniform(1, 2))
        wait = driver.find_element_by_class_name('bheader').text
        if wait == 'MÅ VENTE - UTPRESSING':
            message = 'Kan ikkje utpresse, må vente'
        else:
            try:
                driver.find_element_by_id('sel_1').click()
                driver.find_element_by_name('submitBlackmail').click()
            except NoSuchElementException:
                None
            message = 'Gjort utpressing ''' + str(datetime.now().time())
            time.sleep(random.uniform(2, 3))
        return message


def carTheft(doCartheft, randomNumber):
    if doCartheft == 1:
        message = ''
        if randomNumber == 0:
            randomNumber = random.randint(1, 4)
        driver.find_element_by_link_text('Biltyveri/Garasje').click()
        time.sleep(random.uniform(2, 3))
        wait = driver.find_element_by_class_name('bheader').text
        if wait == 'MÅ VENTE - BILTYVERI':
            message = 'Kan ikkje stjele bil, må vente'
        else:
            if randomNumber == 1:
                driver.find_element_by_id('rowid_table_select_gtaaction0').click()
                message = 'Gjort biltyveri ' + str(datetime.now().time())
            if randomNumber == 2:
                driver.find_element_by_id('rowid_table_select_gtaaction1').click()
                message = 'Gjort biltyveri ' + str(datetime.now().time())
            if randomNumber == 3:
                driver.find_element_by_id('rowid_table_select_gtaaction2').click()
                message = 'Gjort biltyveri ' + str(datetime.now().time())
            if randomNumber == 4:
                driver.find_element_by_id('rowid_table_select_gtaaction3').click()
                message = 'Gjort biltyveri ' + str(datetime.now().time())
            try:
                driver.find_element_by_name('sellAllVehicles').click()
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(random.uniform(2, 3))
                message = 'Har solgt bilene'
            except NoSuchElementException:
                message = 'Greide ikke selge bilene'
        return message


totalMoney = 0


def banking(doBanking):
    if doBanking == 1:
        message = ''
        global totalMoney
        driver.find_element_by_link_text('Bank').click()
        try:
            money = str((driver.find_element_by_id('money_hand').text))
            money = money.replace(' kr', '')
            money = money.replace(',', '')
            totalMoney = int(money) + totalMoney
            message = ('Har totalt satt i banken: ' + str(format(totalMoney, ',')) + ' kr')
            time.sleep(random.uniform(1, 2))
        except NoSuchElementException:
            None
        try:
            driver.find_element_by_name('depositAll').click()
            time.sleep(random.uniform(1, 2))
        except NoSuchElementException:
            None
        return message
    else:
        None



def prison():
    tmpText = (driver.find_element_by_class_name('bheader').text)
    if tmpText == 'MÅ VENTE':
        message = 'Venter...'
        time.sleep(180)

def fightclub(dofightclub):
    if dofightclub == 1:
        message = ''
        try:
            driver.find_element_by_link_text('Fightclub').click()
            time.sleep(random.uniform(2, 3))
            driver.find_element_by_id('rowid_table_select_fcworkout3').click()
            message = 'Gjort fightclub'
        except NoSuchElementException:
            None
        return message
    else:
        None
def shootTraining():
    if doshootTraining.get() == 1:
        try:
            driver.find_element_by_link_text('Skytetrening').click()
            time.sleep(random.uniform(2, 3))
            driver.find_element_by_name('amount').send_keys('1')
            time.sleep(random.uniform(2, 3))
            driver.find_element_by_name('dotrain').click()
            time.sleep(random.uniform(2, 3))
        except NoSuchElementException:
            None

def stealMerce():
    if dostealMerce.get() == 1 and doCartheft.get() == 0:
        randomNumber = 4
        try:
            driver.find_element_by_link_text('Biltyveri/Garasje').click()
            time.sleep(random.uniform(2, 3))
            wait = driver.find_element_by_class_name('bheader').text
            if wait == 'MÅ VENTE - BILTYVERI':
                message = 'Kan ikkje stjele bil, må vente'
            else:
                if randomNumber == 1:
                    driver.find_element_by_id('rowid_table_select_gtaaction0').click()
                    message = 'Gjort biltyveri ' + str(datetime.now().time())
                if randomNumber == 2:
                    driver.find_element_by_id('rowid_table_select_gtaaction1').click()
                    message = 'Gjort biltyveri ' + str(datetime.now().time())
                if randomNumber == 3:
                    driver.find_element_by_id('rowid_table_select_gtaaction2').click()
                    message = 'Gjort biltyveri ' + str(datetime.now().time())
                if randomNumber == 4:
                    driver.find_element_by_id('rowid_table_select_gtaaction3').click()
                    message = 'Gjort biltyveri ' + str(datetime.now().time())

            try:
                time.sleep(random.uniform(2, 3))
                car = driver.find_element_by_xpath('//*[@id="carSelect_42215"]/td[2]/div').text
                message = car
                if car == 'Mercedes-Benz SL 500':
                    message = 'fant bilen'
                    time.sleep(random.uniform(2, 3))
                    driver.find_element_by_xpath('//*[@id="carSelect_42215"]/td[2]/div').click()
                    time.sleep(random.uniform(2, 3))
                    driver.find_element_by_xpath('//*[@id="transportTable"]/tbody/tr[2]/td[2]/select/option[6]').click()
                    time.sleep(random.uniform(2, 3))
                    driver.find_element_by_xpath('//*[@id="transportTable"]/tbody/tr[3]/td[2]/input').click()
                    time.sleep(random.uniform(2, 3))
                    driver.find_element_by_xpath('//*[@id="transportConfirmers"]/input[4]').click()
                    time.sleep(random.uniform(2, 3))
                else:
                    message = 'fant ikke bilen'
                    None
            except NoSuchElementException:
                None

            try:
                driver.find_element_by_name('sellAllVehicles').click()
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(random.uniform(2, 3))
                print('Har solgt bilene')
            except NoSuchElementException:
                message = 'Greide ikke selge bilene'
        except NoSuchElementException:
            None
    return message

def missionCouch():
    currentLocation = driver.find_element_by_xpath('//*[@id="userInfoNav"]/li[2]/span').text
    if currentLocation == 'Stockholm':
        driver.find_element_by_link_text('Bank').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('withdrawAll').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_link_text('The underground').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('tra_5_b').send_keys('15')
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('dobuysell').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_link_text('Flyplass').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_id('rowid_table_select_destination4').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('doflight').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_link_text('The underground').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('tra_5_s').send_keys('15')
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('dobuysell').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_link_text('Bank').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('depositAll').click()
    elif currentLocation == 'London':
        driver.find_element_by_link_text('Bank').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('withdrawAll').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_link_text('Flyplass').click()
        driver.find_element_by_id('rowid_table_select_destination3').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('doflight').click()
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_link_text('The underground').click()
        driver.find_element_by_name('tra_5_b').send_keys('15')
        time.sleep(random.uniform(1, 4))
        driver.find_element_by_name('dobuysell').click()
        time.sleep(random.uniform(1, 4))
