import requests
import json
import tokenMaker as tm
import genre as g
import random
import time
def getRecommendations(token, artist_seed, genre_seed):
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'
    headers = {
        'Authorization': 'Bearer {token}'.format(token=token),
        'Content-Type': 'application/json'
    }
    # pull all artists albums
    r = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params={'seed_artists': artist_seed, 'seed_genres': genre_seed, 'limit': 100})
    d = r.json()
    #print(json.dumps(d, indent=4, sort_keys=True))
    return d
def printJson(d):
    print(json.dumps(d, indent=4, sort_keys=True))
def getRandomArtist(artistsIDs):
    return random.choice(artistsIDs)

def toExtractArtistsIDs(d):
    tracks = d['tracks']
    artists = []
    for track in tracks:
        artists_list = track['artists']
        for artist in artists_list:
            artists.append(artist['id'])
    return list(set(artists))
#printJson(getRecommendations(tm.get_token(), '36QJpDe2go2KgaRleHCDTp', 'samba'))
def getArtistsIDs(token):
    artist_seed = '36QJpDe2go2KgaRleHCDTp'
    genre_seed = g.getRandomGenre()
    artistsIDs = []
    while len(artistsIDs) < 40000:
        batch_artists = toExtractArtistsIDs(getRecommendations(tm.get_token(), artist_seed, genre_seed))
        artistsIDs.extend(batch_artists)
        artistsIDs = list(set(artistsIDs))
        print(len(artistsIDs))
        artist_seed = getRandomArtist(artistsIDs)
        genre_seed = g.getRandomGenre()
        time.sleep(0)
    return artistsIDs
file = open('artistsIDs.txt', 'w')
artistsIDs = getArtistsIDs(tm.get_token())
artistsIDs = sorted(artistsIDs)
for artist in artistsIDs:
    file.write(artist+'\n')
file.close()