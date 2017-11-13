# -*- coding: utf-8 -*-

from behave import when, then, given
import time

from codesrepo.dmmodel import bdmodel

menu_links = {
    "新闻": "news",
    "hao123": "hao123",
    "地图": "map",
    "视频": "v",
    "学术": "xueshu"
}


# behave.use_step_matcher('cfparse')


@when('打开{text}')
def open_baidu(context, text):
    if text == "百度":
        context.bd.go_to_bdhomepage()
        #test


@then('baidu is open')
def check_baidu_is_open(context):
    assert 'baidu' in context.bd.get_current_url()


@when('search behave')
def search_behave(context):
    context.bd.driver.find_element_by_id('kw').send_keys('behave')
    context.searchItem = 'behave'
    time.sleep(5)


@then('search result gets return')
def check_search_result(context):
    result = context.bd.driver.find_element_by_class_name('result-op')
    assert result


@when('open menu {menu_item}')
def open_menu(context, menu_item):
    # context.bd.hover_on_more_products()
    context.bd.click_menu_item(menu_item)
    context.current_url = context.bd.get_current_url()
    context.bd.driver.back()
    time.sleep(2)


@then('the right menu link {menu_item} is open')
def check_current_url(context, menu_item):
    # remove the white spaces in the heading and tailing part of the string {menu_item}
    # because the Chinese character will be added a whitespace before passing to the parameter menu_item
    menu_item = menu_item.strip()
    assert menu_links[menu_item] in context.current_url


@when('open baidu')
def open_baidu_using_table(context):
    context.execute_steps('''
        When 打开百度
    ''')

    model = getattr(context, "model", None)
    if not model:
        context.model = bdmodel()
    for row in context.table:
        context.model.add_menu_links(row['item_link'], row['link_page'])


@given('to get a context text')
def get_context_text(context):
    context.stored_text = context.text


@then('the index of {item_link} is {index}')
def check_index_of_link(context, item_link, index):
    real_index = context.model.item_link.index(item_link)
    assert int(index) == real_index + 1


@then('the context text should be right')
def check_context_text(context):
    context.stored_text = context.stored_text.strip()
    assert context.stored_text == 'This is an example to get a text of a step using context.text'
