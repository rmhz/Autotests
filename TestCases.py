import pytest #Import pytest testing framework
from selenium import webdriver
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
Action = webdriver.ActionChains


# URL is a variable because we have 3 different instances to run the tests
URL = "http://cogniance.com"                             # Prodaction server
#URL = "http://ec2-54-157-244-22.compute-1.amazonaws.com" # Staging server
#URL = "http://newsiteqa2.cogniance.com"                   # QA server


class Test_Repository:

    def test_favicon(self): #Check if the favicon is present
        favicon = requests.get('%s/wp-content/themes/cgnws/favicon.ico' %URL)
        assert favicon.status_code == 200

    def test_logo(self): #Check if the logo is present
        logo = requests.get('%s/email_signature_logo.png' %URL)
        logo_2 = requests.get('%s/cogniance_email_signature_logo.png' %URL)
        assert logo.status_code == 200
        assert logo_2.status_code == 200


class TestWebSite: # Tests for wevsite

    @classmethod                             #\
    def setup_class(cls):                    # \
        print('Test suit start execution')   #  \
                                             #   \
    @classmethod                             #    \
    def teardown_class(cls):                 #     \
        browser.quit()                       #      \
        print('Test suit end execution')     #       > Functions that return the instance to the default station after execution of every test
                                             #      /
    def setup_method(self, method):          #     /
        browser.maximize_window()            #    /
        browser.get(URL)                     #   /
                                             #  /
    def teardown_method(self, method):       # /
        print('end of test case')            #/


    def test_LinkedIn_icon(self):
        browser.find_element_by_xpath(".//*[@id='get-in-touch']/div[2]/a[1]").click()
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        assert browser.current_url == 'https://www.linkedin.com/company/cogniance'

    def test_Twitter_icon(self):
        browser.find_element_by_xpath(".//*[@id='get-in-touch']/div[2]/a[2]").click()
        window_after = browser.window_handles[2]
        browser.switch_to.window(window_after)
        assert browser.current_url == 'https://twitter.com/Cogniance'

    def test_Facebook_icon(self):
        browser.find_element_by_xpath(".//*[@id='get-in-touch']/div[2]/a[3]").click()
        window_after = browser.window_handles[3]
        browser.switch_to.window(window_after)
        assert browser.current_url == 'https://www.facebook.com/cogniance'







