class bdmodel(object):
    def __init__(self):
        self.item_link = []
        self.link_page = []

    def add_menu_links(self, item_link, link_page):
        self.item_link.append(item_link)
        self.link_page.append(link_page)
