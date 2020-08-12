# -*- coding: utf-8 -*-

from pprint import pprint
from crawler import WebCrawler
from sites.wawacity.page_list import PageList as PL
from sites.wawacity.page_detail import PageDetail as PD


class Builder:
    def __init__(self):
        pass

    def set_crawler(self, url):
        self.crawler = WebCrawler(url)

    def get_data(self, url):
        self.set_crawler(url)
        manga_list = PL(url, self.crawler.get_soup())
        result = manga_list.get_data()

        # _url = 'https://www.wawacity.vip/?p=manga&id=1872-the-millionaire-detective-balance-unlimited-saison1'
        # _url = 'https://www.wawacity.vip/?p=manga&id=1874-food-wars-saison5'
        for k, v in result.items():
            result[k]['page'] = self.get_page_data(result[k]['link'])

        pprint(result)

    def get_page_data(self, _url):
        self.set_crawler(_url)
        manga_page = PD(_url, self.crawler.get_soup())

        return manga_page.get_data()


url = 'https://www.wawacity.vip/?p=mangas'
b = Builder()
b.get_data(url)
