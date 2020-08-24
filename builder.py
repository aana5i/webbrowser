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

    def insert_process(self, args):
        result = {}
        for num, dict in args.items():
            for keys, values in dict.items():
                if keys != 'page':
                    result[keys] = values
                else:
                    for key, value in dict['page'].items():
                        if key == 'details':
                            for k, v in value.items():
                                result[k] = v
                        else:
                            result[key] = value
            ''' inset in DB import from create_table'''

'''
a partir d'un fichier text ou de la db, ou du programme, acceder a une liste d'url,
selon l'url, reconnaitre le site et utilise le bon script
rechercher toutes les infos de l'anime.
stocker les resultats dans la db liens dl inclut,
ajouter le lien vers l'emplacement de l'anime sur le DD
selectionner le numeros de l'episodes a par puis le comparer au numeros de lepisode dans le titre sur le DD
ne selectionner que les liens des episodes nno telecharger
'''
url = 'https://www.wawacity.vip/?p=mangas'
b = Builder()
b.get_data(url)
# b.create_tables()
