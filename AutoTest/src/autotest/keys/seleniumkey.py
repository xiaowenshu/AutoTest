#!/usr/bin/python
# encoding:utf-8


import time
import logging
from selenium import webdriver
from autotest.keys.keyinterface import keyinterface
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common import exceptions
from common.mysql_connect import mysql_connect
from common.logging_config import logging_config
from selenium.webdriver.common.alert import Alert
from test.test_codeccallbacks import NoEndUnicodeDecodeError


class seleniumkey(keyinterface):

    def __init__(self):
        self.handles = dict()
        self.controls = dict()
        self.driver = None
        self.options = None
        self.db = mysql_connect()

    def CreatWebDriver(self, name, args):
        if args[0] == 'Chrome':
            driver_path = ".\tools\chromedriver.exe"
            options = None
            dc = None
            if args[1] != None and args[1] != '':
                downloard_path = args[1]
                #                 prefs={}
                options = webdriver.ChromeOptions()
            #                 options.add_experimental_option('prefs', prefs)
            self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

        elif args[0] == 'Firefox':
            profile = None
            if args[1] != None and args[1] != '':
                downloard_path = args[1]
                profile = webdriver.FirefoxProfile()
                profile.set_preference('browser.download.dir', downloard_path)
            self.driver = webdriver.Firefox(firefox_profile=profile)

        elif args[0] == 'IE':
            driver_path = ".\tools\chromedriver.exe"
            self.driver = webdriver.Ie(executable_path=driver_path)

    def OpenURL(self, name, args):
        if self.driver != None:
            self.driver.get(args[0])
            page = self.driver.current_url.split('/')[-1].split('.')[0]
            self.handles[page] = self.driver.current_window_handle

    def CloseDriver(self, name, args):
        self.driver.quit()

    def Refresh(self, name, args):
        self.driver.refresh()

    def Back(self, name, args):
        self.driver.back()

    def Forward(self, name, args):
        self.driver.forward()

    def Setwindowsize(self, name, args):
        self.driver.set_window_size(args[0], args[1], args[2])

    def GetControls(self, name, args):
        sql = \
        "select name,fram,find_by,find_value,in_pop_window from webcontrols where project ={0} and type='web'".args[0]
        all_controls = self.db.execute_sql(sql)
        for control in all_controls:
            self.controls[control[0]] = control[1:]

    def GetFind_by(self, find_by):
        locator = None
        if find_by == 'id':
            locator = By.ID
        elif find_by == 'name':
            locator = By.NAME
        elif find_by == 'class':
            locator = By.CLASS_NAME
        elif find_by == 'css_selector':
            locator = By.CSS_SELECTOR
        elif find_by == 'link_text':
            locator = By.LINK_TEXT
        elif find_by == 'tag_name':
            locator = By.TAG_NAME
        else:
            locator = By.XPATH
        return locator

    def isElementappear(self, find_by, find_value):
        appear_flag = False
        try:
            if self.driver.find_element(self.GetFind_by(find_by), find_value) != None:
                appear_flag = True
            else:
                appear_flag = False

        except exceptions.NoSuchElementException:
            appear_flag = False
        return appear_flag

    def WaitUntilElementappear(self, find_by, find_value, timeout):
        appear_flag = False
        waittime = 0
        while waittime <= timeout:
            if appear_flag == self.isElementappear(find_by, find_value):
                break
            else:
                time.sleep(1)
                waittime += 1
        if appear_flag == False:
            print('find_by', find_by, 'find_value', find_value, 'is not find in the time', timeout)
            logging.info('find_by', find_by, 'find_value', find_value, 'is not find in the time', timeout)
        return appear_flag

    def WaitElementappear(self, name, args):
        fram = self.controls[args[0]][0]
        find_by = self.controls[args[0]][1]
        find_value = self.controls[args[0]][2]
        in_pop_window = self.controls[args[0]][3]
        timeout = 10
        appear_flag = False

        if fram != None and fram != '':
            control_fram = self.controls['fram']
            if self.WaitUntilElementappear(control_fram[1], control_fram[2], 10) == True:
                elem_frame = self.driver.find_element(self.GetFind_by(control_fram[1]), control_fram[2])
                self.driver.switch_to.frame(elem_frame)
        waittime = 0
        while waittime <= timeout:
            if appear_flag == self.isElementappear(find_by, find_value):
                break
            else:
                time.sleep(1)
                waittime += 1
        if appear_flag == False:
            print('find_by', find_by, 'find_value', find_value, 'is not find in the time', timeout)
            logging.info('find_by', find_by, 'find_value', find_value, 'is not find in the time', timeout)
        return appear_flag

    def FindElement(self, name, args):
        fram = self.controls[args[0]][0]
        find_by = self.controls[args[0]][1]
        find_value = self.controls[args[0]][2]
        in_pop_window = self.controls[args[0]][3]
        element = None
        self.driver.switch_to_default_content()
        if fram != None and fram != '':
            control_fram = self.controls['fram']
            if self.WaitUntilElementappear(control_fram[1], control_fram[2], 10) == True:
                elem_frame = self.driver.find_element(self.GetFind_by(control_fram[1]), control_fram[2])
                self.driver.switch_to.frame(elem_frame)
        if self.WaitUntilElementappear(find_by, find_value, 10) == True:
            element = self.driver.find_element(self.GetFind_by(find_by), find_value)

        return element

    def SendKeys(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            try:
                elem.clear()
            except Exception:
                print('fail to clear')
            elem.send_keys(args[1])

    def Click(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            elem.click()

    def AlertAccept(self, name, args):
        Alert(self.driver).accept()

    def AlertDismiss(self, name, args):
        Alert(self.driver).dismiss()

    def MoveAndClick(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            ActionChains(self.driver).move_to_element(elem).perform()

    def DoubleClick(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            ActionChains(self.driver).double_click(elem).perform()

    def ContextClick(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            ActionChains(self.driver).context_click(elem).perform()

    def SelectByText(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            Select(elem).select_by_visible_text(args[1])

    def SelectByValue(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            Select(elem).select_by_value(args[1])

    def isSelect(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            if elem.is_selected() == True:
                return 'SELECTED'
        return 'UN_SELECTED'

    def isEnabled(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            if elem.is_enabled() == True:
                return 'ENABLED'
        return 'UN_ENABLED'

    def isDisplay(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            if elem.is_displayed() == True:
                return 'DISPLAYED'
        return 'UN_DISPLAYED'

    def ExecScript(self, name, args):
        js = args[3]
        elem = self.FindElement(args)
        if elem != None:
            return str(self.driver.execute_script(js, elem, args[1]))
        else:
            return str(self.driver.execute_script(js, elem))

    def GetCookies(self, name, args):

        return self.driver.get_cookies()

    def AddCookies(self, name, args):
        cookies = args[0]
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    #     def WaitElementNotDisplay(self,args):
    #         elem=self.FindElement(args)

    def GetTitle(self, name, args):
        return self.driver.title()

    def GetText(self, name, args):
        elem = self.FindElement(args)
        if elem != None:
            return elem.text()
        else:
            return None

    def AlertAccpet(self, name, args):
        Alert(self.driver).accept()

    def AlertReject(self, name, args):
        Alert(self.driver).dismiss()











































