from pprint import pprint


class DbBuilder:
    def __init__(self, db):
        self.db = db

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
              'seasons_number integer NOT NULL,' \
              'links text NOT NULL' \
              ');'


        # constuire les relations entre les tables
        sql2 = 'CREATE TABLE IF NOT EXISTS genders (id integer PRIMARY KEY, gender text NOT NULL);'

        sql3 = 'CREATE TABLE IF NOT EXISTS types (id integer PRIMARY KEY, type text NOT NULL);'

        sql4 = 'CREATE TABLE IF NOT EXISTS seasons ( id integer PRIMARY KEY, seasons integer NOT NULL);'

        sql5 = 'CREATE TABLE IF NOT EXISTS studios (id integer PRIMARY KEY, studio text NOT NULL);'

        sql6 = 'CREATE TABLE IF NOT EXISTS authors (id integer PRIMARY KEY, author text NOT NULL);'

        sql7 = 'CREATE TABLE IF NOT EXISTS countrys (id integer PRIMARY KEY, country text NOT NULL);'

        self.db.DB('db/database.db')

        sql_list = [sql, sql2, sql3, sql4, sql5, sql6, sql7]
        for sl in sql_list:
            self.db.create_table(sl)

    def insert_in_db(self, args):
        check_select = 'SELECT title FROM details'  # checker si l'anime existe deja

        if not check_select:
            sql1 = 'INSERT INTO details'  # faire les insert dans les bonnes tables et inserer les id ou c'est necessaires

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
            # insert in db


builder = {
        8: {
            'date': 'sam. 22 août 2020',
            'img': 'https://www.wawacity.vip/img/mangas/e5982e7e23a52d980523c3d286b2f6e0.jpg',
            'link': 'https://www.wawacity.vip/?p=manga&id=1923-the-misfit-of-demon-king-academy-saison1',
            'page': {'desc': 'Basé sur le roman Maou Gakuin no Futekigousha de Shuu.\n'
                             '\n'
                             '\n'
                             '\n'
                             'Après 2000 ans, le seigneur démon, ayant la capacité de '
                             'détruire les humains, les élémentaires et les dieux '
                             "vient d'être réincarné !\n"
                             '\n'
                             '\n'
                             '\n'
                             "Suite à une longue période d'innombrables guerres et de "
                             'conflits, Arnos, le seigneur démon, devint malade et '
                             'fatigué et aspirait à un monde pacifique. Il décida '
                             'donc de se réincarner. Cependant, le monde dans lequel '
                             'il se réincarne est trop habitué à la paix et ses '
                             'habitants sont donc trop faibles.\n'
                             '\n'
                             '\n'
                             '\n'
                             "Arnos décide de s'inscrire à l'Académie Maou, qui est "
                             'un établissement créé pour rechercher tous les '
                             'étudiants susceptibles de représenter la réincarnation '
                             'du seigneur démon. Néanmoins, ses pouvoirs sont trop '
                             "extraordinaires pour que ceux de l'académie puissent le "
                             'juger correctement. Il est donc considéré comme un '
                             '«étudiant inexistant».\n'
                             '\n'
                             '\n'
                             '\n'
                             'Sous-estimé et évité par la plupart des habitants de la '
                             'région, il décide de recruter Misha, une des seules '
                             'personnes gentille avec lui, pour grimper au sommet de '
                             'la hiérarchie des démons et ainsi récupérer son titre '
                             'et statut antérieurs.',
                     'details': {'Année:': '2020',
                                 'Auteur:': 'Shuu',
                                 'Genres:': 'Action, Comédie, Fantasy, Romance, Ecole',
                                 'Nationalité:': 'Japon',
                                 "Nombre d'épisodes:": '13',
                                 'Saison:': '1',
                                 'Studio:': 'SILVER LINK.',
                                 'Titre original:': 'Maou Gakuin no Futekigousha  / '
                                                    'Maou Gakuin no Futekigousha: '
                                                    'Shijou Saikyou no Maou no Shiso, '
                                                    'Tensei Shite Shison-tachi no '
                                                    'Gakkou',
                                 'Types:': 'Shōnen'},
                     'links': ['/download?fn=b2ZmZXI/cHJvZD0zJnJlZj01MTQxOTA2JnM9ZG93bmxvYWQmbG5nPUZS',
                               'https://wlnk.ec/3641d42f?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAxIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/908cec3b?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAxIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/8fbdf42c?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAxIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/ff7ee2a7?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAxIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/cafddd47?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAxIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/3457644c?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAxIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/94bb6f29?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAyIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/bb58db6d?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAyIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/043e8e45?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAyIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/fac2cb70?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAyIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/74c82b02?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAyIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/a879afae?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAyIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/a88eed59?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAzIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/056a389d?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAzIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/14d3c0aa?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAzIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/554ef3a0?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAzIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/5f8d790a?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAzIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/585097be?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSAzIC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/a08b1607?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA0IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/acbad1a3?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA0IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/8814b077?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA0IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/408fefef?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA0IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/29584f81?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA0IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/227dc130?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA0IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/ba78c2be?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA1IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/4ef800ed?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA1IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/0a8d5533?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA1IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/2055975e?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA1IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/5f09b3ce?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA1IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/5a0779c5?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA2IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/537c967c?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA2IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/610b92f8?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA2IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/64689255?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA2IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/d78f367e?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA2IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/91e6d621?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA2IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/901c0bc2?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA3IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/a8562bd5?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA3IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/453a6cfe?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA3IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/b0f5f5fb?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA3IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/f6ab4f53?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA3IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/e3930ea8?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA3IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/64f60dd7?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA4IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/331b956f?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA4IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/d59bda5d?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA4IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/46342de5?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA4IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/44f03c83?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA4IC0gW1ZPU1RGUl0%3D&rl=h2',
                               'https://wlnk.ec/8976500b?fn=VGhlIE1pc2ZpdCBvZiBEZW1vbiBLaW5nIEFjYWRlbXkgLSDDiXBpc29kZSA4IC0gW1ZPU1RGUl0%3D&rl=h2'],
                     'seasons': []},
                'title': 'The Misfit of Demon King Academy - Saison 1 - VOSTFR'},
        9: {
                'date': 'sam. 22 août 2020',
                'img': 'https://www.wawacity.vip/img/mangas/ffd74509020c8a498ae0e223093bdede.jpg',
                'link': 'https://www.wawacity.vip/?p=manga&id=1924-lapis-re-lights-saison1',
                'page': {'desc': 'Projet cross-média de KLabGames et Kadokawa annoncé '
                                 "lors de l'Anime Japan 2018.\n"
                                 '\n'
                                 '\n'
                                 '\n'
                                 "L'histoire tournera autour de 6 groupes d'idoles : "
                                 'LiGHTs, IV KLORE, Konohana wa Otome, Sugar Pockets, '
                                 'Sadistic★Candy et Supernova.\n'
                                 '\n'
                                 '\n'
                                 '\n'
                                 "En plus de chanter, les idoles sont capables d'utiliser "
                                 'la magie.',
                         'details': {'Année:': '2020',
                                     'Auteur:': 'KLab, Kadokawa Corporation',
                                     'Genres:': 'Musical, Fantasy, Magical girl',
                                     'Nationalité:': 'Japon',
                                     "Nombre d'épisodes:": '12',
                                     'Saison:': '1',
                                     'Studio:': 'Yokohama Animation Lab',
                                     'Titre original:': 'Lapis Re :LiGHTs',
                                     'Types:': 'Shōnen'},
                         'links': ['/download?fn=b2ZmZXI/cHJvZD0zJnJlZj01MTQxOTA2JnM9ZG93bmxvYWQmbG5nPUZS',
                                   'https://wlnk.ec/42b860f3?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/0b42b56c?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/e26d4745?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/3f7215e3?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/a2956e3e?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/39bd92b2?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/a56fd09c?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/ad8c31bb?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/59d31087?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/ac7169ff?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/cb43c0c8?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/80e8eedd?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/496e21fe?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/944a44da?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/89a5dbe3?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/2df08355?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/1e38f044?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/4583763a?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgMyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/0b3c3d93?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/1306b83d?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/f5147092?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/fc3c68c4?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/ba9a33b3?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/0d8f6ceb?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/9a3df38a?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/d40ca9ca?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/5d5e6433?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/db673b0e?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/859858a1?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNSAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/6d68be93?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/5dd31e37?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/53cb42b2?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/e96a5c99?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/c1703b91?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/7247b795?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNiAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/1f4434fc?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/bab532c9?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/cbee2dc0?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/1e0032f5?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/d86aeac0?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/8f8770ca?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgNyAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/57c50616?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgOCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/47bac8c3?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgOCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/1d789b9e?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgOCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/b075b61a?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgOCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/a963840a?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgOCAtIFtWT1NURlJd&rl=h2',
                                   'https://wlnk.ec/4de59002?fn=TGFwaXMgUmU6TGlHSFRTIC0gw4lwaXNvZGUgOCAtIFtWT1NURlJd&rl=h2'],
                         'seasons': []},
                'title': 'Lapis Re:LiGHTS - Saison 1 - VOSTFR'
                }
        }


db = DbBuilder('db')
db.insert_in_db(builder)
