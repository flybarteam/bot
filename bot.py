from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import random
import schedule
from pyautogui import press
from datetime import datetime
from tkinter import *

driver = webdriver.Chrome()


def site_login():
    driver.get('https://www.nordicmafia.org/login.php')
    driver.find_element_by_name('username').send_keys(username_entry.get())
    driver.find_element_by_name('password').send_keys(password_entry.get())
    driver.find_element_by_name('login').click()
    LoginWindow.destroy()
    time.sleep(random.uniform(2, 3))


def crime():
    if doCrime.get() == 1:
        randomNumber = random.randint(1, 5)
        #randomNumber = 5
        driver.find_element_by_link_text('Kriminalitet').click()
        time.sleep(random.uniform(1, 2))
        wait = driver.find_element_by_class_name('bheader').text
        if wait == 'MÅ VENTE - KRIMINALITET':
            print('Kan ikkje stjele, må vente')
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
            print('Gjort kriminalitet ' + str(datetime.now().time()))
            time.sleep(random.uniform(1, 2))



def blackmail():
    if doBlackmail.get() == 1:
        driver.find_element_by_link_text('Utpressing').click()
        time.sleep(random.uniform(1, 2))
        wait = driver.find_element_by_class_name('bheader').text
        if wait == 'MÅ VENTE - UTPRESSING':
            print('Kan ikkje utpresse, må vente')
        else:
            try:
                driver.find_element_by_id('sel_1').click()
                driver.find_element_by_name('submitBlackmail').click()
            except NoSuchElementException:
                None
            print('Gjort utpressing '
                  '' + str(datetime.now().time()))
            time.sleep(random.uniform(2, 3))

def carTheft():
    if doCartheft.get() == 1:
        randomNumber = random.randint(1, 4)
        randomNumber = 4
        driver.find_element_by_link_text('Biltyveri/Garasje').click()
        time.sleep(random.uniform(2, 3))
        wait = driver.find_element_by_class_name('bheader').text
        if wait == 'MÅ VENTE - BILTYVERI':
            print('Kan ikkje stjele bil, må vente')
        else:
            if randomNumber == 1:
                driver.find_element_by_id('rowid_table_select_gtaaction0').click()
                print('Gjort biltyveri ' + str(datetime.now().time()))
            if randomNumber == 2:
                driver.find_element_by_id('rowid_table_select_gtaaction1').click()
                print('Gjort biltyveri ' + str(datetime.now().time()))
            if randomNumber == 3:
                driver.find_element_by_id('rowid_table_select_gtaaction2').click()
                print('Gjort biltyveri ' + str(datetime.now().time()))
            if randomNumber == 4:
                driver.find_element_by_id('rowid_table_select_gtaaction3').click()
                print('Gjort biltyveri ' + str(datetime.now().time()))
        try:
            driver.find_element_by_name('sellAllVehicles').click()
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(random.uniform(2, 3))
            print('Har solgt bilene')
        except NoSuchElementException:
            print('Greide ikke selge bilene')
   


totalMoney = 0
def banking():
    if doBanking.get() == 1:
        global totalMoney
        driver.find_element_by_link_text('Bank').click()
        try:
            money = str((driver.find_element_by_id('money_hand').text))
            money = money.replace(' kr', '')
            money = money.replace(',', '')
            totalMoney = int(money) + totalMoney
            print('Har totalt satt i banken: ' + str(totalMoney) + ' kr')
            time.sleep(random.uniform(1, 2))
        except NoSuchElementException:
            None
        try:
            driver.find_element_by_name('depositAll').click()
            time.sleep(random.uniform(1, 2))
        except NoSuchElementException:
            None
    else:
        None


def prison():
    tmpText = (driver.find_element_by_class_name('bheader').text)
    if tmpText == 'MÅ VENTE':
        print('Venter...')
        time.sleep(180)
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



LoginWindow = Tk()

#Username
username_lable = Label(LoginWindow, text="Username")
username_lable.pack()
username_entry = Entry(LoginWindow, bd=5)
username_entry.pack()
#Password
password_lable = Label(LoginWindow, text="Password")
password_lable.pack()
password_entry = Entry(LoginWindow, bd=5, show='*')
password_entry.pack()
#doCrime
doCrime = IntVar()
crime_checkbox = Checkbutton(LoginWindow, text = "Kriminalitet", variable = doCrime,
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20, )
crime_checkbox.pack()
#doBlackmail
doBlackmail = IntVar()
blackmail_checkbox = Checkbutton(LoginWindow, text = "Utpressing", variable = doBlackmail,
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20, )
blackmail_checkbox.pack()
#doCartheft
doCartheft = IntVar()
doCartheft_checkbox = Checkbutton(LoginWindow, text = "Biltyveri", justify = LEFT, variable = doCartheft,
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
doCartheft_checkbox.pack()
#doBanking
doBanking = IntVar()
doBanking_checkbox = Checkbutton(LoginWindow, text = "Sett pengene i banken", variable = doBanking,
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20, )
doBanking_checkbox.pack()
#Login
login = Button(LoginWindow, text='LOG IN', command=site_login)
login.pack()
LoginWindow.mainloop()



banking()
crime()
blackmail()
carTheft()

schedule.every(180).to(200).seconds.do(crime)
schedule.every(900).to(920).seconds.do(blackmail)
schedule.every(360).to(380).seconds.do(carTheft)
schedule.every(900).to(1000).seconds.do(banking)

while True:
    schedule.run_pending()
    time.sleep(1)
