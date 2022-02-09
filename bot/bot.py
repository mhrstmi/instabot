import os
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list1 = []
dict = {}
list2 = []
tag_check = ['See Post', 'Visit Link',
             'See location', 'See Location', 'See Hashtag']


class Bot(webdriver.Firefox):
    def __init__(self, driver_path=r"C:\geckodriver"):  # setup for selenium
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path

        super(Bot, self).__init__()

        self.maximize_window()

    def open_insta(self):  # opening instagram
        print('opening instagram... \n')
        self.get("https://www.instagram.com/")

    def login(self, username, password):  # insert user and password
        y = True
        while y:

            try:
                print('Clicking on accept button ... \n')
                accept = WebDriverWait(self, 20).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".aOOlW.bIiDR")))  # checking for accept button if u are using vpn
                accept.click()
                print('Waiting for 3 seconds ... \n')
                time.sleep(3)
                y = False
            except:
                print('couldnt find accept button !!!  \n  continuing... \n')
                y = False
                continue
        print('Entering username ... \n')
        username_el = WebDriverWait(self, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "._2hvTZ.pexuQ.zyHYP")))

        username_el.send_keys(username)
        print('Entering password ... \n')
        password_el = WebDriverWait(self, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))

        password_el.send_keys(password)
        print('Clicking on login button ... \n')
        login_el = WebDriverWait(self, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".sqdOP.L3NKy.y3zKF")))

        login_el.click()
        print('Logged in \n')

    def first_search(self, *usernames):  # searching for accounts

        for username in usernames:

            i = 0
            while i < 5:
                if i == 4:
                    # this while loop is for in case internet got disconnected
                    x = input('problem , wanna contiue? y/n: ')
                    if x == 'n':
                        break
                    else:
                        pass
                try:
                    search_el = WebDriverWait(self, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
                    search_el.send_keys(username)
                except:
                    continue

                try:
                    print('Enter TAGs account... \n')
                    acc_el = WebDriverWait(self, 20).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".-qQT3")))
                    if acc_el:

                        acc_el.click()
                        print('Wait for 3 seconds... \n')
                        i = 6
                        i += 1
                        time.sleep(3)
                except:
                    search_el.clear()
                    i += 1
            try:
                story_el = WebDriverWait(self, 20).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@role='button' and @class='RR-M- h5uC0']"))).click()
            except:
                continue

            while True:  # here we find the TAG and save its  info

                try:
                    time.sleep(3)
                    tag_el = WebDriverWait(self, 3).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='zKGE8 wLYRG']"))).click()
                    print('ckick on Tag')
                    tag_save = WebDriverWait(self, 3).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='NPpif']"))).get_attribute('innerHTML')
                    time_story = WebDriverWait(self, 3).until(
                        EC.visibility_of_element_located((By.XPATH, "//time[@class='BPyeS Nzb55']")))
                    date = time_story.get_attribute("title")
                    story_time = time_story.get_attribute("innerHTML")
                    list2.append(str(tag_save))

                    z = True
                    for i in tag_check:  # here we check for some unwanted tags...
                        if tag_save == i:
                            z = False
                            print('already exists')
                            try:
                                next_story = WebDriverWait(self, 3).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@class='FhutL']"))).click()
                                break
                            except:
                                break
                    while z:
                        dict.update(
                            {tag_save: ['', '', '', '', '', '', '', '']})
                        print('new tag found')
                        print(date + '--' + story_time + '--' + tag_save)
                        tag_check.append(str(tag_save))
                        list1.append(str(tag_save))

                        dict[tag_save][2] = str(date)
                        dict[tag_save][3] = str(story_time)

                        try:
                            print('next story')
                            next_story = WebDriverWait(self, 3).until(EC.visibility_of_element_located(
                                (By.XPATH, "//button[@class='FhutL']"))).click()
                            z = False

                        except:
                            break
                    dict[tag_save][0] = username
                    dict[tag_save][4] = story_time
                except:
                    try:
                        print('next story')
                        next_story = WebDriverWait(self, 3).until(EC.visibility_of_element_located(
                            (By.XPATH, "//button[@class='FhutL']"))).click()
                    except:
                        break

    # here we search all the TAGs and save its usernames and flwers number
    def second_search(self):
        self.implicitly_wait(10)
        list3 = list(set(list1) & set(list2))

        for values in list3:

            i = 0
            while i < 5:
                if i == 4:
                    x = input('problem , wanna contiue? y/n: ')
                    if x == 'n':
                        break
                    else:
                        pass
                try:
                    print('finding search element')
                    search_el = WebDriverWait(self, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
                    search_el.send_keys(values)
                except:
                    print('couldnt find search element // con...')
                    continue

                try:
                    print('click on TAG ... \n')
                    acc_el = WebDriverWait(self, 20).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".-qQT3")))
                    if acc_el:

                        acc_el.click()
                        print('Wait for 3 seconds... \n')
                        i = 6
                        i += 1
                        time.sleep(3)
                except:
                    search_el.clear()
                    i += 1

            try:
                try:
                    print('Looking for username section... \n')
                    parent_user_el = WebDriverWait(self, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//div[@class='XBGH5']")))
                    if parent_user_el:
                        print('Saving TAGs username... \n')
                        user = parent_user_el.find_element_by_xpath(
                            ".//h2[@class='_7UhW9       fKFbl yUEEX   KV-D4              fDxYl     ']")
                        tag_username = user.get_attribute("innerHTML")
                        dict[values][1] = str(tag_username)
                        print('saved')

                except:
                    print('Couldnt find accounts username !!! CONTINUING... \n')
                    pass

                try:
                    print('looking for flwers sections... \n')
                    parent_el = WebDriverWait(self, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//a[@class='-nal3 ']")))

                    if parent_el:
                        print('Saving flwers... \n')
                        flwers_num = parent_el.find_element_by_xpath(
                            ".//span[@class='g47SY ']").get_attribute("title")
                        if dict[values][5] == '':
                            dict[values][5] = str(flwers_num)
                            print('saved')
                        else:
                            dict[values][6] = str(flwers_num)
                            print('saved')

                        time.sleep(3)
                except:
                    print('No flwers sections !!! CONTINUING... \n')
                    pass

            except:
                print('no flwers and users \n')
                pass

        list2.clear()
        print(list1)
        print(list2)
        print(dict)

    def excel(self):  # here we insert all the info in a excel file
        print('creating excel file')
        execl_file = openpyxl.load_workbook('flw.xlsx')
        sheet = execl_file.get_sheet_by_name('sheet')
        r = 1
        for key, value in dict.items():
            c = 1
            for values in value:
                sheet.cell(row=r, column=c).value = values
                c += 1
            r += 1

        execl_file.save('final_flwers.xlsx')
        time.sleep(3)
