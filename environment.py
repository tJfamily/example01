from selenium import webdriver
from codesrepo.base import BDBase


def get_driver(context):
    return webdriver.Chrome()


def before_all(context):
    context.driver = get_driver(context)
    context.bd = BDBase(context.driver)


def after_all(context):
    context.driver.quit()
