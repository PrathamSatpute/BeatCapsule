import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_auth_manager():
    return SpotifyOAuth(
        client_id='your_client_id',
        client_secret='your_client_secret',
        redirect_uri='http://localhost:5000/callback',
        scope='user-top-read user-read-recently-played'
    )