# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

# to run
# cd C:\skill_factory\26\petsfriend_api_tests\tests
# py -m pytest -v --driver Chrome --driver-path c:/skill_factory/chromedriver test_26.py


from pages.auth_page import AuthPage


def test_auth_page(web_browser):
    """ Make sure main search works fine. """
    url = 'http://petfriends1.herokuapp.com/login'
    page = AuthPage(web_browser,url)

    page.email = 'vol1@test.test'
    page.password = 'vol1'
    page.btn_success.click()

    assert page.get_current_url != url, 'авторизация не удалась'

    time.sleep(15)
