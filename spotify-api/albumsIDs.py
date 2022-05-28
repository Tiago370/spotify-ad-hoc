import requests
import tokenMaker as tm
import json
def getAlbumsByArtist(token, artist_id):
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'
    headers = {
        'Authorization': 'Bearer {token}'.format(token=token),
        'Content-Type': 'application/json'
    }
    # pull all artists albums
    r = requests.get('https://api.spotify.com/v1/artists/{id}/albums'.format(id=artist_id) , headers=headers, params={'limit': 50})
    d = r.json()
    #print(json.dumps(d, indent=4, sort_keys=True))
    return d
def printJson(d):
    print(json.dumps(d, indent=4, sort_keys=True))

def toExtractAlbumsIDs(d):
    items = d['items']
    albuns = []
    for item in items:
        albuns.append(item['id'])
    return albuns

def getAllAlbumsIDs(token, artist_id):
    albumsIDs = []
    current_length = 0
    while True:
        d = getAlbumsByArtist(token, artist_id)
        albumsIDs = list(set(albumsIDs + toExtractAlbumsIDs(d)))
        if current_length == len(albumsIDs):
            print('current_length:', current_length)
            break
        current_length = len(albumsIDs)
    albumsIDs = sorted(albumsIDs)
    return albumsIDs

def printIDs(albumsIDs):
    for albumID in albumsIDs:
        print(albumID)
#obter todos os IDs de todos os albums de todos os artistas
token = tm.get_token()
print('token:', token)
count = 0
with open('IDs/albums/albumIDs.txt', 'a') as f:
    print("arquivo aberto IDS/albums/albumIDs.txt")
    with open('IDs/artists/artistsIDs_30825.txt', 'r') as g:
        print("arquivo aberto IDs/artists/artistsIDs_30825.txt")
        while True:
            artist_id = g.readline()
            artist_id = artist_id.replace('\n', '')
            try:
                albumsIDs = getAllAlbumsIDs(token, artist_id)
                for albumID in albumsIDs:
                    f.write(albumID + '\n')
            except:
                print(artist_id)
                print('erro')
                break
            count += 1
            print('artists:', count)
