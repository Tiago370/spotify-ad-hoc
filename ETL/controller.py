from dotenv import load_dotenv
import os
from numpy import select
import time
import requests
import json
from modelo import Album, Tracks, Artista


class Spotify():
    def __init__(self, client, secret):
        self.client = client
        self.secret = secret
        self.tokenTime = 0
        self.token = ''

    def getToken(self):
        atual = int(time.time())
        if atual - self.tokenTime > 3000:
            try:
                auth_response = requests.post('https://accounts.spotify.com/api/token', {
                'grant_type': 'client_credentials',
                'client_id': self.client,
                'client_secret': self.secret,
                })
                auth_response_data = auth_response.json()
                self.token = auth_response_data['access_token']
                self.tokenTime = atual
            except requests.exceptions.RequestException as error:
                print("Error: ", error)
                exit(1)
        return self.token

    def makeRequest(self, endpoint):
        baseUrl = 'https://api.spotify.com/v1/'
        headers = {
            'Authorization': 'Bearer {}'.format(self.getToken())
        }
        try:
            json_data = requests.get(baseUrl + endpoint, headers=headers).text
            json_object = json.loads(json_data)
        except requests.exceptions.RequestException as error:
                print("Error: ", error)
                exit(1)
        return json_object

    def getArtist(self, idArtist):
        artista =  self.makeRequest('artists/{}'.format(idArtist))
        imagens = list()
        for image in artista['images']:
            imagens.append(image['url'])
        return Artista(artista['id'], artista['name'], artista['followers']['total'], artista['popularity'], imagens, artista['genres'])

    def getAlbums(self, idArtist):
        offset = 0
        completo = False
        items = list()
        listaAlbums = list()
        while not completo:
            resultado = self.makeRequest('artists/{}/albums?offset={}&limit=20&include_groups=album'.format(idArtist, offset))
            items.extend(resultado['items'])
            for album in items:
                imagens = list()
                for image in album['images']:
                    imagens.append(image['url'])
                artistas = list()
                for artista in album['artists']:
                    artistas.append(artista['id'])
                listaAlbums.append(Album(album['id'], album['name'], album['release_date'], album['total_tracks'], artistas, imagens, len(artistas)))

            if not resultado['next']:
                completo = True
            else:
                offset += 20
        
        return listaAlbums

    def getTracks(self, idAlbum):
        offset = 0
        completo = False
        listaTracks = list()
        items = list()
        while not completo:
            resultado = self.makeRequest('albums/{}/tracks?limit=20&offset={}'.format(idAlbum, offset))
            items.extend(resultado['items'])
            for track in items:
                artistas = list()
                for artista in track['artists']:
                    artistas.append(artista['id'])
                listaTracks.append(Tracks(track['id'], track['name'], track['duration_ms'], track['track_number'], track['explicit'], idAlbum, artistas, len(artistas)))
            if not resultado['next']:
                completo = True
            else:
                offset += 20
        return listaTracks

if __name__ == "__main__":
    load_dotenv()
    client = os.getenv('CLIENT')
    secret = os.getenv('SECRET')
    sessao = Spotify(client, secret)

    idArtist = '0TnOYISbd1XYRBk9myaseg'
    idAlbum = '4aawyAB9vmqN3uQ7FjRGTy'

    tracks = sessao.getTracks(idAlbum)

    listaArtistas = list()

    listaIdArtista = list()
    with open("./IDs/artists/teste.txt") as file_in:
        for line in file_in:
            listaIdArtista.append(line.strip())

    for index, idArtista in enumerate(listaIdArtista):
        print('[{}] -- {} --INICIO--'.format(index, idArtist))
        listaAlbums = list()
        artista = sessao.getArtist(idArtista)
        listaArtistas.append(artista)
        albums = sessao.getAlbums(idArtista)
        listaAlbums = sessao.getAlbums(idArtista)
        for album in listaAlbums:
            album.setTracks(sessao.getTracks(album.id))
        artista.setAlbums(listaAlbums)
        print('[{}] -- {} --FIM--'.format(index, idArtist))

    # for artista in listaArtistas:
    #     artista.printArtista()
    #     for album in artista.albums:
    #         album.printAlbum()
    #         for track in album.tracks:
    #             track.printTrack()
