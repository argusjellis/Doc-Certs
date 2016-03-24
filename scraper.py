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


############################
# declare global variables #
############################

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
BASE_URL = "http://www.certificationmatters.org"
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
assert "Certification" in driver.title

# ====
# this is where do all the scraping
# ====

# shut it down
driver.close()

