from dotenv import load_dotenv
import os
from numpy import select
import time
import requests
import json
from modelo import Album, Track, Artist
import logging
import threading

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
            return False
        return json_object

    def getArtist(self, idArtist):
        artista =  self.makeRequest('artists/{}'.format(idArtist))
        imagem = artista['images'][0]['url'] if len(artista['images']) > 0 else ''
        return Artist(artista['id'], artista['name'], artista['followers']['total'], artista['popularity'], imagem, artista['genres'])

    def getAlbums(self, idArtist):
        offset = 0
        completo = False
        items = list()
        listaAlbums = list()
        qtd = 0
        while not completo or qtd > 5:
            resultado = self.makeRequest('artists/{}/albums?offset={}&limit=15&include_groups=album'.format(idArtist, offset))
            if resultado != False:
                items.extend(resultado['items'])
                for album in items:
                    imagem = album['images'][0]['url'] if len(album['images']) > 0 else ''
                    artistas = list()
                    for artista in album['artists']:
                        # Se nao existe o artista ele insere
                        if not Artist.existeArtista(artista['id']):
                            objArtista = self.getArtist(artista['id'])
                            objArtista.insertArtista()
                        artistas.append({
                            'id': artista['id'],
                            'isOwner': True if artista['id'] == idArtist else False
                        })
                    # Caso seja somente ano lancamento somente
                    dataLancamento = album['release_date']+'-01-01' if len(album['release_date']) == 4 else album['release_date']
                    listaAlbums.append(Album(album['id'], album['name'], dataLancamento, album['total_tracks'], artistas, imagem, len(artistas)))
                if not resultado['next']:
                    completo = True
                else:
                    completo = True
                    offset += 20
        return listaAlbums

    def getTracks(self, idAlbum, idArtist):
        offset = 0
        completo = False
        listaTracks = list()
        items = list()
        while not completo:
            resultado = self.makeRequest('albums/{}/tracks?limit=15&offset={}'.format(idAlbum, offset))
            if resultado != False:
                items.extend(resultado['items'])
                for track in items:
                    artistas = list()
                    for artista in track['artists']:
                        # Se nao existe o artista ele insere
                        if not Artist.existeArtista(artista['id']):
                            objArtista = self.getArtist(artista['id'])
                            objArtista.insertArtista()
                        artistas.append({
                            'id': artista['id'],
                            'isOwner': True if artista['id'] == idArtist else False
                        })
                    listaTracks.append(Track(track['id'], track['name'], track['duration_ms'], track['track_number'], track['explicit'], idAlbum, artistas, len(artistas)))
                if not resultado['next']:
                    completo = True
                else:
                    completo = True
                    offset += 20
        return listaTracks

def separa(lista, parts):
    k, m = divmod(len(lista), parts)
    return (lista[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(parts))


def leIdArtistas(arquivo, partes):
    listaIdArtista = list()
    with open(arquivo) as file_in:
        for line in file_in:
            listaIdArtista.append(line.strip())
    return list(separa(listaIdArtista, partes))


def thread_function(num, client, secret, listaIdArtista):
    logging.info("Thread [%d]: Executando", num)
    sessao = Spotify(client, secret)
    for index, idArtista in enumerate(listaIdArtista):
        print('[{}] -- {} --INICIO--'.format(index, idArtista))
        artista = sessao.getArtist(idArtista)
        print('INSERT ARTIST [{}] - '.format(artista.id),artista.insertArtista())
        listaAlbums = sessao.getAlbums(idArtista)
        for album in listaAlbums:
            listaTracks = sessao.getTracks(album.id, idArtista)
            album.setTracks(listaTracks)
            print('\tINSERT ALBUM [{}] - '.format(album.id),album.insertAlbum())
            for track in listaTracks:
                print('\t\tINSERT TRACK [{}] - '.format(track.id),track.insertTrack())
        artista.setAlbums(listaAlbums)
        print('[{}] -- {} --FIM--'.format(index, idArtista))

    logging.info("Thread [%d]: Finalizando", num)

def main():

    load_dotenv()
    client = os.getenv('CLIENT')
    secret = os.getenv('SECRET')
    
    quantidadeThreads = 20

    # Definicoes logging
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    listaIdArtista = leIdArtistas("./ETL/inserir.txt", quantidadeThreads)

    for num, parte in enumerate(listaIdArtista):
        logging.info("Main: thread [%d]: Criada e Iniciada", num)
        x = threading.Thread(target=thread_function, args=(num, client, secret, parte))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main: before joining thread [%d].", index)
        thread.join()
        logging.info("Main: thread [%d] done.", index)


if __name__ == "__main__":
    main()