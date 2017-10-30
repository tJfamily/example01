Feature: testing menu links
  Scenario Outline: Open each menu item
    When 打开百度
    Then baidu is open
    When open menu <item_link>
    Then the right menu link  <link_page> is open


    Examples: Menu_Items
        | item_link       |   link_page |
        | 新闻          | 新闻    |
        | hao123        | hao123  |
        | 地图          | 地图    |
        | 视频          | 视频    |
        | 学术          | 学术    |
