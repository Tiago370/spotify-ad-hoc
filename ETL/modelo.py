from config import Config

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

    def printAlbum(self):
        print(20* '--')
        print('id: {}\nname: {}\nreleaseDate: {}\ntotalTracks: {}\nimg: {}\nqtdArtistas: {}\nartistas: {}\ntracks: {}'.format(
            self.id, self.nome, self.releaseDate, self.totalTracks, self.img, self.qtdArtistas, self.artistas, self.tracks))
        print(20* '--')

    def setTracks(self, tracks):
        self.tracks = tracks

    def getTracks(self):
        return self.tracks

    def insertAlbum(self):
        # Insere o album no banco
        pass

    def existeAlbum(id):
        string_sql = """SELECT COUNT(albumid) FROM esquema.albums WHERE albumid = %s"""
        registros = Config.consultaBD(Config, string_sql, [id])
        if ((registros[1][0][0]) != 0):
            return True
        else:
            return False