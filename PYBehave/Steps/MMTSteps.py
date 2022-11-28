import time

from behave import *
from selenium import webdriver
path= r"C:\Users\Vishi\OneDrive\Desktop\sprint-2\chromedriver_win32\chromedriver.exe"


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=path)

@when('open Make My Trip homepage')
def open_homepage(context):
    context.driver.get('https://www.makemytrip.com/')

@then('Click on home stay button')
def click_homestay(context):
    context.driver.find_element('xpath', '//a[@href="https://www.makemytrip.com/homestays/"]').click()
    time.sleep(2)


@then('Select place in location bar')
def select_location_bar(context):
    context.driver.find_element('xpath', '//input[@id="city"]').send_keys('delhi')
    time.sleep(2)
    context.driver.find_element('xpath', '//input[@id="city"]').send_keys('delhi')


@then('Click on selected place on dropdown')
def select_location(context):
    try:
        context.driver.find_element('xpath', '//p[text()="Delhi, India"]').click()

    except:
        context.driver.find_element('xpath', '//p[text()="Delhi"]').click()

@then('select checkin date')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@aria-label="Mon Dec 05 2022"]').click()

@then('Select checkout date')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@aria-label="Wed Dec 07 2022"]').click()

@then('Select number of person')
def step_impl(context):
    context.driver.find_element('xpath', '//li[@data-cy="adults-3"]').click()

@then('click on apply')
def step_impl(context):
    context.driver.find_element('xpath', '//button[text()="APPLY"]').click()

@then('Click on search button')
def step_impl(context):
    context.driver.find_element('xpath', '//button[text()="Search"]').click()
    time.sleep(2)

@then('Select hotel')
def select_hotel(context):
    context.driver.find_element('xpath', '//div[@class="makeFlex flexOne padding20 relative lftCol"]//span[text()="WOOD CASTLE HOTEL"]').click()
    time.sleep(5)

@then('Click on Language option')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@class="whiteText makeFlex perfectCenter langSlct"]').click()

@then('Click on dropdown of country selector')
def step_impl(context):
    context.driver.find_element('xpath', '//p[@class="selectConInput"]').click()

@then(u'select country India')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@class="searchListWrap"]//p[@class="listRow"][1]').click()

@then(u'select languages hindi from radio button')
def step_impl(context):
    context.driver.find_element('xpath', '//label[text()="हिंदी"]').click()

@then(u'Click on apply button')
def step_impl(context):
    context.driver.find_element('xpath', '//button').click()

@then(u'select languages english from radio button')
def step_impl(context):
    context.driver.find_element('xpath', '//label[text()="English"]').click()

@then(u'select languages tamil from radio button')
def step_impl(context):
    context.driver.find_element('xpath', '//label[text()="தமிழ்"]').click()

@then(u'select country uae')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@class="searchListWrap"]//p[@class="listRow"][2]').click()
@then(u'select languages urdu from radio button')
def step_impl(context):
    context.driver.find_element('xpath','//label[text()="العربية"]').click()

@then(u'select country usa')
def step_impl(context):
    context.driver.find_element('xpath', '//div[@class="searchListWrap"]//p[@class="listRow"][3]').click()


