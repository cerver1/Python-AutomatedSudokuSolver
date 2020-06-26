from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def keyboard_usage(driver, value):
    ActionChains(driver).key_down(value).pause(0.5).key_up(value).pause(0.5).perform()

