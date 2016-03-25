#!usr/bin/python

#########################################################################
# references                                                            #
# ==========                                                            #
# virtualenv: https://virtualenv.pypa.io/en/latest/                     #
# os: https://docs.python.org/2/library/os.html                         #
# csv: https://docs.python.org/2/library/csv.html                       #
# time: https://docs.python.org/2/library/time.html                     #
# selenium: http://selenium-python.readthedocs.org/                     #
# beautifulsoup: http://www.crummy.com/software/BeautifulSoup/bs4/doc/  #
#########################################################################


####################
# import libraries #
####################

# from the python standard library
import os
import csv
import time

# from third-party libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



############################
# declare global variables #
############################

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
BASE_URL = "https://www.certificationmatters.org/is-your-doctor-board-certified/search-now.aspx"
LOGIN_USER = os.environ['CERT_SITE_USER']
LOGIN_PW = os.environ['CERT_SITE_PW']


##################
# start scraping #
##################

# create a webdriver
driver = webdriver.Firefox()

# open the web page
driver.get(BASE_URL)

# make sure it's the page we want
assert "Search Now" in driver.title

# to trigger the login page, do a fake search
# first, target the "last name" text input
# ... but wait until the element is present on the page

lname_form = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dnn_ctr865_Search_txtlastName"))
)

# send the letter 'a'
lname_form.send_keys("a")

# click the 'search' button
driver.find_element_by_id("dnn_ctr865_Search_search").click()

# target the email input, once it's visible
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dnn_ctr865_Search_txtEmailAddress"))
)

# target the password input, once it's visible
pw_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dnn_ctr865_Search_txtPassword"))
)

# send email and pw
email_input.send_keys(LOGIN_USER)
pw_input.send_keys(LOGIN_PW)

# submit
driver.find_element_by_id("dnn_ctr865_Search_btnLogin").click()


"""
select = Select(driver.find_element_by_name('name'))
"""

# shut it down
driver.close()

