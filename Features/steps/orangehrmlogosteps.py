from behave import *
from selenium import webdriver


@given('launch chrome browser')
def LaunchBrowser(context):
    context.driver=webdriver.Chrome("C:/Users/Sanjay/PycharmProjects/BehaveProject/driver/chromedriver.exe")


@when('open orange hrm homepage')
def OpenHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on page')
def VerifyLogoPresent(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']/img").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()

