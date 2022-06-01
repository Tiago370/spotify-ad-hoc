from config import config

class Artist():
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
        if not Artist.existeArtista(self.id):
            string_SQL_artista = 'INSERT INTO public.artist (id, name, followers, popularity, img) VALUES (%s, %s, %s, %s, %s)'
            dados_artista = (self.id, self.nome, self.followers, self.popularity, self.img)
            string_SQL_generos = 'INSERT INTO public.artist_genres (id_artist, genre) VALUES (%s, %s)'
            return config.insertArtistaGenres(config, string_SQL_artista, string_SQL_generos, dados_artista, self.genres, self.id)
        else:
            return 'Existe Artista'

    def existeArtista(id):
        string_sql = """SELECT COUNT(id) FROM public.artist WHERE id = %s"""
        registros = config.consultaBD(config, string_sql, [id])
        if ((registros[1][0][0]) != 0):
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

    def insertAlbumOld(self):
        if not Album.existeAlbum(self.id):
            string_sql = 'INSERT INTO public.album (id, name, release_date, qtd_artists, qtd_tracks, img) VALUES (%s, %s, %s, %s, %s, %s)'
            novo_registro = (self.id, self.nome, self.releaseDate, self.qtdArtistas, self.totalTracks, self.img)
            return config.alteraBD(config, string_sql, novo_registro)
        else:
            return 'Existe Album'

    def insertAlbum(self):
        if not Album.existeAlbum(self.id):
            string_SQL_album = 'INSERT INTO public.album (id, name, release_date, qtd_artists, qtd_tracks, img) VALUES (%s, %s, %s, %s, %s, %s)'
            dados_album = (self.id, self.nome, self.releaseDate, self.qtdArtistas, self.totalTracks, self.img)
            string_SQL_artistas = 'INSERT INTO public.artist_album (id_artist, id_album, main_artist) VALUES (%s, %s, %s)'
            return config.insertAlbumsArtists(config, string_SQL_album, string_SQL_artistas, dados_album, self.artistas, self.id)
        else:
            return 'Existe Album'

    def printAlbum(self):
        print('\t[ALBUM]-----------\n\tid: {}\n\tname: {}\n\treleaseDate: {}\n\ttotalTracks: {}\n\timg: {}\n\tArtistas: {}\n\tqtdArtistas: {}\n\ttracks: '.format(
            self.id, self.nome, self.releaseDate, self.totalTracks, self.img, self.artistas, self.qtdArtistas))

    def setTracks(self, tracks):
        self.tracks = tracks

    def getTracks(self):
        return self.tracks

    def existeAlbum(id):
        string_sql = """SELECT COUNT(id) FROM public.album WHERE id = %s"""
        registros = config.consultaBD(config, string_sql, [id])
        if ((registros[1][0][0]) != 0):
            return True
        else:
            return False

class Track():
    def __init__(self, id, nome, duracao, numero, explicito, idAlbum, artistas, qtdArtistas):
        self.id = id
        self.nome = nome
        self.duracao = duracao
        self.numero = numero
        self.explicito = explicito
        self.idAlbum = idAlbum
        self.qtdArtistas = qtdArtistas
        self.artistas = artistas

    def insertTrack(self):
        if not Album.existeAlbum(self.id):
            string_SQL_track = 'INSERT INTO public.track (id, name, duration, explicit, track_number, album_id, qtd_artistas) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            dados_track = (self.id, self.nome, self.duracao, self.explicito, self.numero, self.idAlbum, self.qtdArtistas)
            string_SQL_artistas = 'INSERT INTO public.artist_track (id_artist, id_track, main_artist) VALUES (%s, %s, %s)'
            return config.insertAlbumsArtists(config, string_SQL_track, string_SQL_artistas, dados_track, self.artistas, self.id)
        else:
            return 'Existe Track'

    def printTrack(self):
        print('\t\t[TRACK]-----------\n\t\tid: {}\n\t\tNome: {}\n\t\tDuracao: {}\n\t\tTrackNumber: {}\n\t\tExplicito: {}\n\t\tAlbumID: {}\n\t\tQtdArtistas: {}\n\t\tArtistas: {}\n'.format(
            self.id, self.nome, self.duracao, self.numero, self.explicito, self.idAlbum, self.qtdArtistas, self.artistas))

    def existeTrack(id):
        string_sql = """SELECT COUNT(id) FROM public.track WHERE id = %s"""
        registros = config.consultaBD(config, string_sql, [id])
        if ((registros[1][0][0]) != 0):
            return True
        else:
            return False