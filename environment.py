from selenium import webdriver


def get_driver(context):
    return webdriver.Chrome()


def before_all(context):
    context.driver = get_driver(context)


def after_all(context):
    context.driver.quit()
