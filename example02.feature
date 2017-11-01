Feature: Testing Baidu
  @test
    Scenario: Check each menu link
    Given to get a context text
      """
      This is an example to get a text of a step using context.text
     """
    Then the context text should be right
    When open baidu
        | item_link    | link_page |
        | 新闻          | 新闻    |
        | hao123        | hao123  |
        | 地图          | 地图    |
        | 视频          | 视频    |
        | 学术          | 学术    |
    And open menu 学术
    Then the right menu link  学术 is open
    And the index of 学术 is 5