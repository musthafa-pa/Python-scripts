#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: mustafa
"""
###############script for updating all plugins in wordpress website#############
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import glob
import os

def pluginUpdate():
    chromeOptions = webdriver.ChromeOptions()
    
    ######path to the chrome web driver
    path_to_chromedriver = "/home/user/chromedriver"
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)
    
    #######maximizing the browser window#########
    browser.set_window_size(1024, 600)
    browser.maximize_window()
    
    #########URL of the webpage########
    url = 'https://website.com/wp-admin'
    browser.get(url)
    
    ########Wait for DOM load############
    time.sleep(1)
    
    ####Send username and password keys & login###########
    userName = browser.find_element_by_id('user_login')
    userName.send_keys("username")
    time.sleep(1)
    passWord = browser.find_element_by_id('user_pass')
    passWord.send_keys("password") 
    browser.find_element_by_id("wp-submit").click()
    
    ######find plugin page############
    url = "https://website.com/wp-admin/plugins.php"
    browser.get(url)
    
    #######Select all plugins############
    browser.find_element_by_id('cb-select-all-1').click()
    time.sleep(1)
    ########Select update option from Bulk actions#########
    select = Select(browser.find_element_by_id('bulk-action-selector-top'))
    select.select_by_index(3)
    
    ############Update plugins###########
    browser.find_element_by_id('doaction').click()

pluginUpdate()