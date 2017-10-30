# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC


css_menu_item = "#u1 > a:nth-child({})"


class BDBase(object):
    def __init__(self, driver):
        self.driver = driver

    def hover_on_more_products(self):
        css_settings_link = css_menu_item.format(8)
        self.driver.find_element_by_css_selector(css_settings_link)
        ac = AC(self.driver)
        ac.move_to_element_with_offset(css_settings_link, 50, 0)
        ac.perform()

    def click_menu_item(self, menu_item):
        self.driver.find_element_by_link_text(menu_item).click()

    def get_current_url(self):
        return self.driver.current_url

    def go_to_bdhomepage(self):
        self.driver.get("http://www.baidu.com")
