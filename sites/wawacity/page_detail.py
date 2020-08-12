# -*- coding: utf-8 -*-


class PageDetail:
    def __init__(self, url, soup):
        self.url = url
        self.soup = soup

    def get_data(self):
        page = self.soup.find('div', {'id': "detail-page"})
        blocs = page.find_all('div', {'class': 'wa-sub-block'})
        anime_title = self.soup.find('h1', {'class': 'wa-block-title'}).getText().strip()
        anime_title = anime_title.replace('Animés » ', '').split(' ')[0]
        result = {}

        bloc_title_list = {
            'Autres': ['seasons', self.get_other_seasons],
            anime_title: ['details', self.get_details],
            'Synopsis': ['desc', self.get_synopsis],
            'Télécharger': ['links', self.get_links]
        }

        for self.bloc in blocs:
            try:
                b_title = self.bloc.find('div', {'class': 'wa-sub-block-title'}).getText().strip()
                current_value = b_title.split(' ')[0]
                if current_value in bloc_title_list:
                    result[bloc_title_list[current_value][0]] = bloc_title_list[current_value][1]()
            except:
                continue

        return result

    def get_other_seasons(self):
        ul = self.bloc.find('ul')
        seasons = []
        try:
            for li in ul.find_all('li'):
                seasons.append(li.text.strip())
        except:
            seasons.append('Aucune autre saisons disponibles pour cette animé.')

        return seasons

    def get_details(self):
        ul = self.bloc.find('ul', {'class': 'detail-list'})

        res = {}
        a_list = ['Genres:', 'Types:']

        for li in ul.find_all('li'):
            tmp = li.text.strip().split('\n')
            if tmp[0] in a_list:
                value = ', '.join([v.contents[0].strip() for v in li.find_all('a')])
            else:
                value = tmp[1].strip()

            res[tmp[0].strip()] = value

        return res

    def get_synopsis(self):
        descs = self.bloc.find_all('p')

        ref_str = 'Le téléchargement du manga'
        result = ''
        for desc in descs:
            synopsis = desc.text
            if synopsis[:len(ref_str)] not in ref_str:
                result += synopsis

        return result

    def get_links(self):
        bloc = self.bloc.find('table', {'class': 'table wa-post-link-list'})
        tr = bloc.find_all('tr', {'class': 'link-row'})

        result = []

        for td in tr:
            t = td.find_all('td')
            link = t[0].find_all("a", href=True)
            result.append(link[0]['href'])

        return result
