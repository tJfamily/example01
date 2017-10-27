Feature: Script using behave framework
    Scenario: Open Baidu and search behave
        When 打开百度
        Then baidu is open
        When search behave
        Then search result gets return
