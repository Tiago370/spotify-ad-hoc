import config as cfg

class Album():
    def __init__(self, id, nome, releaseDate, totalTracks, artistas, img, qtdArtistas):
        self.id = id
        self.nome = nome
        self.releaseDate = releaseDate
        self.totalTracks = totalTracks
        imgs = img.split('/')
        self.img = imgs[len(imgs)-1]
        self.qtdArtistas = qtdArtistas
        self.artistas = artistas
        self.tracks = list()
        self.config = cfg.Config()

    def printAlbum(self):
        print(20* '--')
        print('id: {}\nname: {}\nreleaseDate: {}\ntotalTracks: {}\nimg: {}\nqtdArtistas: {}\n\ntracks: {}'.format(
            self.id, self.nome, self.releaseDate, self.totalTracks, self.img, self.qtdArtistas, self.tracks))
        print('artistas:')
        for artista in self.artistas:
            print(artista)
        print(20* '--')

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
    def __init__(self, id, nome, duracao, numero, explicito):
        self.id = id
        self.nome = nome
        self.duracao = duracao
        self.numero = numero
        self.explicito = explicito
        

    def printTracks(self, idAlbum):
        print(20* '--')
        print('id: {}\nNome: {}\nDuracao: {}\nTrackNumber: {}\nExplicito: {}\nAlbumID: {}'.format(
            self.id, self.nome, self.duracao, self.numero, self.explicito, idAlbum))
        
    def insertTracks(self, idAlbum):
        #if (self.existeTracks(self.id)):
        #    return False
        string_sql = "INSERT INTO tracks(id, name, duration_ms, track_number, explicit, albumID) VALUES('{}', '{}', '{}', {}, '{}')".format(self.id, self.nome, self.duracao, self.numero, self.explicito, idAlbum)
        msg = self.config.alteraBD(string_sql, [])
        if (msg == 'sucesso'):
            return True
        else:
            return False

    def existeTracks(self, id):
        string_sql = """SELECT COUNT(id) FROM tracks WHERE id = '{}'""".format(id)
        registros = self.config.consultaBD(string_sql, [])
        if (registros[1][0][0] > 0):
            return True
        else:
            return False