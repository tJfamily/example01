# -*- coding: utf-8 -*-


from behave import when, then, given
import time


# @when('Open baidu website')
@when(u"打开{text}")
def open_baidu(context, text):
    if text == '百度':
        context.driver.get("http://www.baidu.com")


@then('baidu is open')
def check_baidu_is_open(context):
    assert 'baidu' in context.driver.current_url


@when('search behave')
def search_behave(context):
    context.driver.find_element_by_id('kw').send_keys('behave')
    context.searchItem = 'behave'
    time.sleep(5)


@then('search result gets return')
def check_search_result(context):
    result = context.driver.find_element_by_class_name('result-op')
    assert result
