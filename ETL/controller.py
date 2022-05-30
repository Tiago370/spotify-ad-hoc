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
        resultado =  self.makeRequest('artists/{}'.format(idArtist))
        return resultado
        
    def getAlbums(self, idArtist):
        offset = 0
        completo = False
        items = list()
        while not completo:
            resultado = self.makeRequest('artists/{}/albums?offset={}&limit=20&include_groups=album'.format(idArtist, offset))
            items.extend(resultado['items'])
            if not resultado['next']:
                completo = True
            else:
                offset += 20
        return items

    def getTracks(self, idAlbum):
        offset = 0
        completo = False
        items = list()
        while not completo:
            resultado = self.makeRequest('albums/{}/tracks?limit=20&offset={}'.format(idAlbum, offset))
            items.extend(resultado['items'])
            if not resultado['next']:
                completo = True
            else:
                offset += 20
        return items

if __name__ == "__main__":
    load_dotenv()
    client = os.getenv('CLIENT')
    secret = os.getenv('SECRET')
    sessao = Spotify(client, secret)

    idArtist = '0TnOYISbd1XYRBk9myaseg'
    idAlbum = '4aawyAB9vmqN3uQ7FjRGTy'

    
        
    print(sessao.getArtist(idArtist))
    # print(sessao.getAlbums(idArtist))
    albums = sessao.getAlbums(idArtist)
    tracks = sessao.getTracks(idAlbum)
    
    
    listaTracks = list()
    listaAlbums = list()
    listaArtistas = list()

    listaIdArtista = []
    with open("./IDs/artists/artistsIDs_20047.txt") as file_in:
        for line in file_in:
            listaIdArtista.append(line) 

    # print(listaIdArtista)

    
    for ident in listaIdArtista:
        print("teste: ")
        print(ident)
        artista = sessao.getArtist(ident)
        print("teste: ")
        print(artista)
        teste = 'status'
        if teste in artista:
            pass
        else:
            listaArtistas.append(Artista(artista["id"], artista["name"], artista["followers"], artista["popularity"], artista["images"]))

    for track in tracks:
        listaTracks.append(Tracks(track['id'], track['name'], track['duration_ms'], track['track_number'], track['explicit'], idAlbum))
    
    for track in listaTracks:
        #track.printTracks()
        # track.insertTrack()
        pass
        

   

    for album in albums:
        artistas = list()
        for artista in album['artists']:
            artistas.append(artista['id'])
        listaAlbums.append(Album(album['id'], album['name'], album['release_date'], album['total_tracks'], artistas, album['images'][0]['url'], len(artistas)))

    #print(listaAlbums[0].existeAlbum("6nCJAxRvXmPkPiZo8Vh5ZG"))
    for album in listaAlbums:
        # album.printAlbum()
        album.insertAlbum()
    