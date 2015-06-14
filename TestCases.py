import pytest #Import pytest testing framework
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
Action = webdriver.ActionChains


# URL is a variable because we have 3 different instances to run the tests
URL = "http://cogniance.com"                             # Prodaction server
#URL = "http://ec2-54-157-244-22.compute-1.amazonaws.com" # Staging server
#URL = "http://newsiteqa2.cogniance.com"                   # QA server

class BaseFixture:
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

class Test_Repository:

    def test_favicon(self): #Check if the favicon is present
        favicon = requests.get('%s/wp-content/themes/cgnws/favicon.ico' %URL)
        assert favicon.status_code == 200

    def test_logo(self): #Check if the logo is present
        logo = requests.get('%s/email_signature_logo.png' %URL)
        logo_2 = requests.get('%s/cogniance_email_signature_logo.png' %URL)
        assert logo.status_code == 200
        assert logo_2.status_code == 200

@pytest.mark.skipif("True")
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

    def test_title(self): #Check if the title of website is correct
        assert 'Cogniance ' + u"\u2014 " + 'Your Intelligence. Multiplied.' == browser.title

    def test_description(self): #Check if description of website is correct
        description = browser.find_element_by_xpath("//meta[@name='description']")
        content = description.get_attribute("content")
        assert 'Cogniance is a global organization with roots in Silicon Valley. We exist to help innovators bring software and hardware innovations to market. In essence, we co-create technology products.' == content

    def test_menu_url_1(self): #Check if the URL is correct clicking "Whar We Do" menu item in nav bar
        Button = browser.find_element_by_xpath('html/body/div[1]/div[2]/div[1]/ul/li[1]/a')
        Action(browser).move_to_element(Button).click(Button).perform()
        assert browser.current_url == '%s/#what-we-do' %URL

    def test_menu_url_2(self): #Check if the URL is correct clicking "Our Work" menu item in nav bar
        Button = browser.find_element_by_xpath('html/body/div[1]/div[2]/div[1]/ul/li[2]/a')
        Action(browser).move_to_element(Button).click(Button).perform()
        assert browser.current_url == '%s/#our-work' %URL

    def test_menu_url_3(self): #Check if the URL is correct clicking "Who We Are" menu item in nav bar
        Button = browser.find_element_by_xpath('html/body/div[1]/div[2]/div[1]/ul/li[3]/a')
        Action(browser).move_to_element(Button).click(Button).perform()
        assert browser.current_url == '%s/#who-we-are' %URL

    def test_menu_url_4(self): #Check if the URL is correct clicking "Get In Touch" menu item in nav bar
        Button = browser.find_element_by_xpath('html/body/div[1]/div[2]/div[1]/ul/li[4]/a')
        Action(browser).move_to_element(Button).click(Button).perform()
        assert browser.current_url == '%s/#get-in-touch' %URL

    def test_case_study_hover_1(self): #Check if rollover appears on hover state
        CloudMade = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[1]/a/img")
        Action(browser).move_to_element(CloudMade).perform()
        browser.implicitly_wait(2) # seconds
        rollover = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[1]/a/div")
        assert rollover.is_displayed()

    def test_case_study_hover_2(self): #Check if rollover appears on hover state
        Netpulse = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[2]/a/img")
        Action(browser).move_to_element(Netpulse).perform()
        browser.implicitly_wait(2) # seconds
        rollover = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[2]/a/div")
        assert rollover.is_displayed()

    def test_cloud_made_link(self): # Check if CloudMade pop-up have its own URL
        CloudMade = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[1]/a/img")
        Action(browser).move_to_element(CloudMade).click(CloudMade).perform()
        assert browser.current_url == '%s/#our-work/cloudmade' %URL

    def test_netpulse_link(self): # Check if Netpulse pop-up have its own URL
        Netpulse = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[2]/a/img")
        Action(browser).move_to_element(Netpulse).click(Netpulse).perform()
        assert browser.current_url == '%s/#our-work/netpulse' %URL

    def test_libratone_link(self): # Check if Libratone pop-up have its own URL
        Libratone = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[3]/a/img")
        Action(browser).move_to_element(Libratone).click(Libratone).perform()
        assert browser.current_url == '%s/#our-work/libratone' %URL

    def test_alcohoot_link(self): # Check if Alcohoot pop-up have its own URL
        Alcohoot = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[4]/a/img")
        Action(browser).move_to_element(Alcohoot).click(Alcohoot).perform()
        assert browser.current_url == '%s/#our-work/alcohoot' %URL

    def test_expensify_link(self): # Check if Expensify pop-up have its own URL
        Expensify = browser.find_element_by_xpath(".//*[@id='our-work']/ul/li[5]/a/img")
        Action(browser).move_to_element(Expensify).click(Expensify).perform()
        assert browser.current_url == '%s/#our-work/expensify' %URL

    def test_hover_profile_Juha(self): # Check if Juha profile has blue color on hover on the main page
        Juha_Christensen = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[2]/a/img[1]")
        Action(browser).move_to_element(Juha_Christensen).perform()
        Juha_Christensen_hovered = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[2]/a/img[2]")
        assert Juha_Christensen_hovered.is_displayed()

    def test_hover_profile_Michael(self): # Check if Michael profile has blue color on hover on the main page
        Michael_Shraybman = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[3]/a/img[1]")
        Action(browser).move_to_element(Michael_Shraybman).perform()
        Michael_Shraybman_hovered = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[3]/a/img[2]")
        assert Michael_Shraybman_hovered.is_displayed()

    def test_hover_profile_Sergii(self): # Check if Sergii profile has blue color on hover on the main page
        Sergii_Gorpynich = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[4]/a/img[1]")
        Action(browser).move_to_element(Sergii_Gorpynich).perform()
        Sergii_Gorpynich_hovered = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[4]/a/img[2]")
        assert Sergii_Gorpynich_hovered.is_displayed()

    def test_hover_profile_Kristian(self): # Check if Kristian profile has blue color on hover on the main page
        Kristian_Kroyer = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[5]/a/img[1]")
        Action(browser).move_to_element(Kristian_Kroyer).perform()
        Kristian_Kroyer_hovered = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[5]/a/img[2]")
        assert Kristian_Kroyer_hovered.is_displayed()

    def test_hover_profile_Marty(self): # Check if Marty profile has blue color on hover on the main page
        Marty_McFarland = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[6]/a/img[1]")
        Action(browser).move_to_element(Marty_McFarland).perform()
        Marty_McFarland_hovered = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[6]/a/img[2]")
        assert Marty_McFarland_hovered.is_displayed()

    def test_hover_profile_Carter(self): # Check if Carter profile has blue color on hover on the main page
        Carter_Perez = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[7]/a/img[1]")
        Action(browser).move_to_element(Carter_Perez).perform()
        Carter_Perez_hovered = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[7]/a/img[2]")
        assert Carter_Perez_hovered.is_displayed()

    def test_hover_profile_Steve(self): # Check if Carter profile has blue color on hover on the main page
        Steve_Haney = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[8]/a/img[1]")
        Action(browser).move_to_element(Steve_Haney).perform()
        Steve_Haney_hovered = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[8]/a/img[2]")
        assert Steve_Haney_hovered.is_displayed()

    def test_see_all_size(self): # Check if "See All" text have correct font-size
        Strategize = browser.find_element_by_xpath(".//*[@id='what-we-do']/div[3]/div/div/a[1]/div")
        Action(browser).move_to_element(Strategize).click(Strategize).perform()
        Expertise_Design = browser.find_element_by_xpath(".//*[@id='myModalLabel']/div/nav/ul/li[2]/a")
        Action(browser).move_to_element(Expertise_Design).click(Expertise_Design).perform()
        See_All_button = browser.find_element_by_xpath(".//*[@id='myModalLabel']/div/ul[1]/li[4]/a/p")
        font_size = See_All_button.get_attribute("style")
        assert font_size == "font-size: 21px;"

    def test_adress_Silicon_Valley(self): # Check if the address in rollover is correct
        Silicon_Valley_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[1]/a/strong")
        Action(browser).move_to_element(Silicon_Valley_button).click(Silicon_Valley_button).perform()

        Silicon_Valley_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[1]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='menlo-park']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='menlo-park']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='menlo-park']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='menlo-park']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='menlo-park']/address/a").get_attribute("href")

        assert Silicon_Valley_button_text == 'Silicon Valley'
        assert Rollover_head_text == 'Silicon Valley (HQ)'
        assert Rollover_1_string == '1370 Willow Road'
        assert Rollover_2_string == "Menlo Park, CA 94025\nUSA"
        assert Email_text == 'hellomenlopark@cogniance.com'
        assert Email_adress == 'mailto:hellomenlopark@cogniance.com'

    def test_adress_Los_Angeles(self): # Check if the address in rollover is correct
        Los_Angeles_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[1]/a/strong")
        Action(browser).move_to_element(Los_Angeles_button).click(Los_Angeles_button).perform()

        Los_Angeles_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[1]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='los-angeles']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='los-angeles']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='los-angeles']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='los-angeles']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='los-angeles']/address/a").get_attribute("href")

        assert Los_Angeles_button_text == 'Los Angeles'
        assert Rollover_head_text == 'Los Angeles'
        assert Rollover_1_string == '920 Santa Monica Blvd.'
        assert Rollover_2_string == "Santa Monica, CA 90401\nUSA"
        assert Email_text == 'hellolosangeles@cogniance.com'
        assert Email_adress == 'mailto:hellolosangeles@cogniance.com'

    def test_adress_New_York(self): # Check if the address in rollover is correct
        New_York_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[2]/a/strong")
        Action(browser).move_to_element(New_York_button).click(New_York_button).perform()

        New_York_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[2]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='new-york']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='new-york']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='new-york']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='new-york']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='new-york']/address/a").get_attribute("href")

        assert New_York_button_text == 'New York'
        assert Rollover_head_text == 'New York'
        assert Rollover_1_string == '25 Broadway'
        assert Rollover_2_string == "New York, NY 10004\nUSA"
        assert Email_text == 'hellonewyork@cogniance.com'
        assert Email_adress == 'mailto:hellonewyork@cogniance.com'

    def test_adress_Boston(self): # Check if the address in rollover is correct
        Boston_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[2]/a/strong")
        Action(browser).move_to_element(Boston_button).click(Boston_button).perform()

        Boston_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[2]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='boston']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='boston']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='boston']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='boston']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='boston']/address/a").get_attribute("href")

        assert Boston_button_text == 'Boston'
        assert Rollover_head_text == 'Boston'
        assert Rollover_1_string == '51 Melcher Street'
        assert Rollover_2_string == "Boston, MA 02210\nUSA"
        assert Email_text == 'helloboston@cogniance.com'
        assert Email_adress == 'mailto:helloboston@cogniance.com'

    def test_adress_London(self): # Check if the address in rollover is correct
        London_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[3]/a/strong")
        Action(browser).move_to_element(London_button).click(London_button).perform()

        London_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[3]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='london']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='london']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='london']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='london']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='london']/address/a").get_attribute("href")

        assert London_button_text == 'London'
        assert Rollover_head_text == 'London'
        assert Rollover_1_string == '7 Stratford Place'
        assert Rollover_2_string == "London W1C 1AY\nUK"
        assert Email_text == 'hellolondon@cogniance.com'
        assert Email_adress == 'mailto:hellolondon@cogniance.com'

    def test_adress_Aarhus(self): # Check if the address in rollover is correct
        Aarhus_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[3]/a/strong")
        Action(browser).move_to_element(Aarhus_button).click(Aarhus_button).perform()

        Aarhus_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[3]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='aarhus']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='aarhus']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='aarhus']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='aarhus']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='aarhus']/address/a").get_attribute("href")

        assert Aarhus_button_text == 'Aarhus'
        assert Rollover_head_text == 'Aarhus'
        assert Rollover_1_string == 'Balticagade 12D'
        assert Rollover_2_string == "8000 Aarhus\nDenmark"
        assert Email_text == 'helloaarhus@cogniance.com'
        assert Email_adress == 'mailto:helloaarhus@cogniance.com'

    def test_adress_Copenhagen(self): # Check if the address in rollover is correct
        Copenhagen_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[4]/a/strong")
        Action(browser).move_to_element(Copenhagen_button).click(Copenhagen_button).perform()

        Copenhagen_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[4]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='copenhagen']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='copenhagen']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='copenhagen']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='copenhagen']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='copenhagen']/address/a").get_attribute("href")

        assert Copenhagen_button_text == 'Copenhagen'
        assert Rollover_head_text == 'Copenhagen'
        assert Rollover_1_string == 'Njalsgade 19D, 1.FL'
        assert Rollover_2_string == "2300 Copenhagen\nDenmark"
        assert Email_text == 'hellocopenhagen@cogniance.com'
        assert Email_adress == 'mailto:hellocopenhagen@cogniance.com'

    def test_adress_Munich(self): # Check if the address in rollover is correct
        Munich_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[4]/a/strong")
        Action(browser).move_to_element(Munich_button).click(Munich_button).perform()

        Munich_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[4]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='munich']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='munich']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='munich']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='munich']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='munich']/address/a").get_attribute("href")

        assert Munich_button_text == 'Munich'
        assert Rollover_head_text == 'Munich'
        assert Rollover_1_string == 'Am Glockenbach 7'
        assert Rollover_2_string == "80469 Munich\nGermany"
        assert Email_text == 'hellomunich@cogniance.com'
        assert Email_adress == 'mailto:hellomunich@cogniance.com'

    def test_adress_Wroclaw(self): # Check if the address in rollover is correct
        Wroclaw_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[5]/a/strong")
        Action(browser).move_to_element(Wroclaw_button).click(Wroclaw_button).perform()

        Wroclaw_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[2]/span[5]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='wroclaw']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='wroclaw']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='wroclaw']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='wroclaw']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='wroclaw']/address/a").get_attribute("href")

        assert Wroclaw_button_text == 'Wroclaw'
        assert Rollover_head_text == 'Wroclaw'
        assert Rollover_1_string == 'Ul. Kazimierza Wielkiego 1'
        assert Rollover_2_string == "50-077 Wroclaw\nPoland"
        assert Email_text == 'hellowroclaw@cogniance.com'
        assert Email_adress == 'mailto:hellowroclaw@cogniance.com'

    def test_adress_Kyiv(self): # Check if the address in rollover is correct
        Kyiv_button = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[5]/a/strong")
        Action(browser).move_to_element(Kyiv_button).click(Kyiv_button).perform()

        Kyiv_button_text = browser.find_element_by_xpath(".//*[@id='mapContainer']/div[3]/span[5]/a/strong").text
        Rollover_head_text = browser.find_element_by_xpath(".//*[@id='kyiv']/address/h3/strong").text
        Rollover_1_string = browser.find_element_by_xpath(".//*[@id='kyiv']/address/h4[1]").text
        Rollover_2_string = browser.find_element_by_xpath(".//*[@id='kyiv']/address/h4[2]").text
        Email_text = browser.find_element_by_xpath(".//*[@id='kyiv']/address/a").text
        Email_adress = browser.find_element_by_xpath(".//*[@id='kyiv']/address/a").get_attribute("href")

        assert Kyiv_button_text == 'Kyiv'
        assert Rollover_head_text == 'Kyiv'
        assert Rollover_1_string == 'Malevycha (Bozhenka) 86 O'
        assert Rollover_2_string == "Kyiv 03150\nUkraine"
        assert Email_text == 'hellokyiv@cogniance.com'
        assert Email_adress == 'mailto:hellokyiv@cogniance.com'

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

    def test_About_us_block(self):
        About_us = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[1]/a/img[1]")
        Action(browser).move_to_element(About_us).perform()
        rgba_hovered = browser.find_element_by_xpath(".//*[@id='who-we-are']/div[3]/div[1]/a/img[2]").value_of_css_property("color")

        assert rgba_hovered == '0'

@pytest.mark.skipif("True")
class TestWPAdmin: # Tests for WP-Admin

    @classmethod                                                 #\
    def setup_class(cls):                                        # \
        print('Test suit start execution')                       #  \
                                                                 #   \
    @classmethod                                                 #    \
    def teardown_class(cls):                                     #     \
        browser.quit()                                           #      \
        print('Test suit end execution')                         #       > Functions that return the instance to the default station after execution of every test
                                                                 #      /
    def setup_method(self, method):                              #     /
        browser.maximize_window()                                #    /
        browser.get('http://newsiteqa2.cogniance.com/wp-admin')  #   /
                                                                 #  /
    def teardown_method(self, method):                           # /
        print('end of test case')                                #/

    def test_active_plugins(self): # Check if all the plugins are activated
        username = browser.find_element_by_xpath(".//*[@id='user_login']")
        password = browser.find_element_by_xpath(".//*[@id='user_pass']")
        login = browser.find_element_by_xpath(".//*[@id='wp-submit']")
        Action(browser).move_to_element(login).click(login).perform()
        plugings_button = browser.find_element_by_xpath(".//*[@id='menu-plugins']/a/div[3]")
        Action(browser).move_to_element(plugings_button).click(plugings_button).perform()
        All_plugins = browser.find_element_by_xpath(".//*[@id='wpbody-content']/div[4]/ul/li[1]/a/span")
        Number_of_All_plugins = All_plugins.text
        Activated_plugins = browser.find_element_by_xpath(".//*[@id='wpbody-content']/div[4]/ul/li[2]/a/span")
        Number_of_Activated_plugins = Activated_plugins.text
        assert Number_of_All_plugins == Number_of_Activated_plugins

class TestsByRoman(BaseFixture):

    def test_projectHoverWidth(self):
        project_list = browser.find_elements_by_css_selector('.our-work > .list-projects > li:not(.hide) > a:not([class*="all"])')
        for project in project_list:
            Action(browser).move_to_element(project).perform()
            project_hover = browser.find_element_by_css_selector('.our-work > .list-projects > li:not(.hide) > a:not([class*="all"]) > .hover-dialog')
            assert project_hover.size['height'] == project.size['height']/2

    def test_allProjectHoverWidth(self):
        load_all_button = browser.find_element_by_css_selector('.our-work > .list-projects > li:not(.hide) > a[class*="all"]')
        Action(browser).click(load_all_button).perform()
        project_list = browser.find_elements_by_css_selector('.our-work > .list-projects > li:not(.hide) > a:not([class*="all"])')
        for project in project_list:
            Action(browser).move_to_element(project).perform()
            project_hover = browser.find_element_by_css_selector('.our-work > .list-projects > li:not(.hide) > a:not([class*="all"]) > .hover-dialog')
            assert project_hover.size['height'] == project.size['height']/2

if __name__ == '__main__':
    pytest.main([__file__, '-v',"--capture=sys"])