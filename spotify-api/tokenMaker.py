import requests as req
import time
import secrets as s
def get_token():
    # formato do arquivo 'secrets.py':
    #CLIENT_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    #CLIENT_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    CLIENT_ID = s.CLIENT_ID
    CLIENT_SECRET = s.CLIENT_SECRET

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # POST
    auth_response = req.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']
    time.sleep(0)
    return access_token
print(get_token())