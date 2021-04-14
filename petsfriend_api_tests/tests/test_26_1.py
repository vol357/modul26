# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from pages.auth_page import AuthPage

# to run
# cd C:\skill_factory\26\petsfriend_api_tests\tests
# py -m pytest -v --driver Chrome --driver-path c:/skill_factory/chromedriver test_26_1.py

def test_auth_page(selenium):
   page = AuthPage(selenium)
   page.enter_email("vol1@test.test")
   page.enter_pass("vol1")
   page.btn_click()

   #знак != или == будет зависеть от того, верные или неверные данные мы вводим
   assert page.get_relative_link() != '/all_pets', "login error"

   time.sleep(5) #задержка для учебных целей