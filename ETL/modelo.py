from config import config

class Artista():
    def __init__(self, id, nome, followers, popularity, img, genres):
        self.id = id
        self.nome = nome
        self.followers = followers
        self.popularity = popularity
        self.img = img
        self.genres = genres
        self.albums = list()

    def setAlbums(self, albums):
        self.albums = albums
    
    def printArtista(self):
        print('[ARTIST]-----------\nid:{}\nNome: {}\nSeguidores: {}\nPopularidade: {}\nImagem: {}\nGenres: {}\nAlbums: '.format(
            self.id, self.nome, self.followers, self.popularity, self.img, self.genres
        ))
    
    def insertArtista(self):
        string_sql = 'INSERT INTO public.artist (id, name, followers, popularity, img) VALUES (%s, %s, %s, %s, %s)'
        novo_registro = (self.id, self.nome, self.followers, self.popularity, self.img)
        return config.alteraBD(config, string_sql, novo_registro)


    def existeArtista(self, idArtista):
        string_sql = """SELECT COUNT(id) FROM album WHERE id = '{}'""".format(idArtista)
        registros = self.config.consultaBD(string_sql, [])
        if (registros[1][0][0] > 0):
            return True
        else:
            return False

class Album():
    def __init__(self, id, nome, releaseDate, totalTracks, artistas, img, qtdArtistas):
        self.id = id
        self.nome = nome
        self.releaseDate = releaseDate
        self.totalTracks = totalTracks
        self.img = img
        self.qtdArtistas = qtdArtistas
        self.artistas = artistas
        self.tracks = list()
        # self.config = config.Config()

    def printAlbum(self):
        print('\t[ALBUM]-----------\n\tid: {}\n\tname: {}\n\treleaseDate: {}\n\ttotalTracks: {}\n\timg: {}\n\tqtdArtistas: {}\n\ttracks: '.format(
            self.id, self.nome, self.releaseDate, self.totalTracks, self.img, self.qtdArtistas))

    def setTracks(self, tracks):
        self.tracks = tracks

    def getTracks(self):
        return self.tracks

    def insertAlbum(self):
        #if (self.existeAlbum(self.id)):
        #    return False
        string_sql = "INSERT INTO album(id, name, release_date, qtd_artists, img) VALUES('{}', '{}', '{}', {}, '{}')".format(self.id, self.nome, self.releaseDate, self.qtdArtistas, self.img)
        msg = self.config.alteraBD(string_sql, [])
        if (msg == 'sucesso'):
            return True
        else:
            return False

    def existeAlbum(self, id):
        string_sql = """SELECT COUNT(id) FROM album WHERE id = '{}'""".format(id)
        registros = self.config.consultaBD(string_sql, [])
        if (registros[1][0][0] > 0):
            return True
        else:
            return False

class Tracks():
    def __init__(self, id, nome, duracao, numero, explicito, idAlbum, artistas, qtdArtistas):
        self.id = id
        self.nome = nome
        self.duracao = duracao
        self.numero = numero
        self.explicito = explicito
        self.idAlbum = idAlbum
        self.qtdArtistas = qtdArtistas
        self.artistas = artistas
        # self.config = cfg.Config()

    def printTrack(self):
        print('\t\t[TRACK]-----------\n\t\tid: {}\n\t\tNome: {}\n\t\tDuracao: {}\n\t\tTrackNumber: {}\n\t\tExplicito: {}\n\t\tAlbumID: {}\n\t\tQtdArtistas: {}\n\t\tArtistas: {}\n'.format(
            self.id, self.nome, self.duracao, self.numero, self.explicito, self.idAlbum, self.qtdArtistas, self.artistas))
        
    def insertTrack(self):
        #if (self.existeTracks(self.id)):
        #    return False
        string_sql = "INSERT INTO track(id, name, duration, explicit, track_number, album_id) VALUES('"+self.id+"', '"+self.nome+"', "+str(self.duracao)+', '+str(self.explicito)+', '+str(self.numero)+", '"+self.idAlbum+"');"
        msg = self.config.alteraBD(string_sql, [])
        if (msg == 'sucesso'):
            print('sucesso')
            return True
        else:
            print('deu ruim')
            return False

    def existeTracks(self, id):
        string_sql = """SELECT COUNT(id) FROM tracks WHERE id = '{}'""".format(id)
        registros = self.config.consultaBD(string_sql, [])
        if (registros[1][0][0] > 0):
            return True
        else:
            return False