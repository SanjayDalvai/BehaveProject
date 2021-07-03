from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome("C:/Users/Sanjay/PycharmProjects/BehaveProject/driver/chromedriver.exe")


@when('open orange hrm homepage')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username {user} and password {pwd}')
def enter_credentials(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('click on the Login Button')
def click_login_button(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('user must successfully login to the Dashboard')
def successful_login(context):
    text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text()
    assert text == "Dashboard"
