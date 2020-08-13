# -*- coding: utf-8 -*-

from pprint import pprint
from crawler import WebCrawler
from db_sqlite import DB
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

    def create_tables(self):
        sql = 'CREATE TABLE IF NOT EXISTS details (' \
              'id integer PRIMARY KEY,' \
              'title text NOT NULL,' \
              'original_title text NOT NULL,' \
              'img text NOT NULL,' \
              'site_link text NOT NULL,' \
              'synopsis text NOT NULL,' \
              'date text NOT NULL,' \
              'years text NOT NULL,' \
              'author_id integer NOT NULL,' \
              'gender_id integer NOT NULL,' \
              'country_id integer NOT NULL,' \
              'episode_number integer NOT NULL,' \
              'seasons_id integer NOT NULL,' \
              'studio_id integer NOT NULL,' \
              'types_id integer NOT NULL,' \
              'seasons_id integer NOT NULL,' \
              'links text NOT NULL' \
              ');'

        sql2 = 'CREATE TABLE IF NOT EXISTS genders (id integer PRIMARY KEY, gender text NOT NULL);'

        sql3 = 'CREATE TABLE IF NOT EXISTS types (id integer PRIMARY KEY, type text NOT NULL);'

        sql4 = 'CREATE TABLE IF NOT EXISTS seasons ( id integer PRIMARY KEY, seasons integer NOT NULL);'

        sql5 = 'CREATE TABLE IF NOT EXISTS studios (id integer PRIMARY KEY, studio text NOT NULL);'

        sql6 = 'CREATE TABLE IF NOT EXISTS authors (id integer PRIMARY KEY, author text NOT NULL);'

        sql7 = 'CREATE TABLE IF NOT EXISTS countrys (id integer PRIMARY KEY, country text NOT NULL);'

        db = DB('db/database.db')
        db.create_table(sql)
        db.create_table(sql2)
        db.create_table(sql3)
        db.create_table(sql4)
        db.create_table(sql5)
        db.create_table(sql6)
        db.create_table(sql7)

    def insert_in_db(self):
        pass


url = 'https://www.wawacity.vip/?p=mangas'
b = Builder()
# b.get_data(url)
b.create_tables()
