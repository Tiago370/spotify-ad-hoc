
class Album():
    def __init__(self, id, nome, releaseDate, totalTracks, artistas, img, qtdArtistas):
        self.id = id
        self.nome = nome
        self.releaseDate = releaseDate
        self.totalTracks = totalTracks
        self.artistas = artistas
        self.img = img
        self.qtdArtistas = qtdArtistas
        self.tracks = list()

    def printAlbum(self):
        print(20* '--')
        print('id: {}\nname: {}\nreleaseDate: {}\ntotalTracks: {}\nimg: {}\nqtdArtistas: {}\nartistas: {}'.format(
            self.id, self.nome, self.releaseDate, self.totalTracks, self.img, self.qtdArtistas, self.artistas))
        print(20* '--')

    def addTracks(self, track):
        self.tracks.append(track)

    def getTracks(self):
        return self.tracks

    def insertAlbum(self):
        # Insere o album no banco
        pass

    def existeAlbum(self):
        # Confere  no banco se existe o album
        pass