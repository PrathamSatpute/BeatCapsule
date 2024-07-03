import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_auth_manager():
    return SpotifyOAuth(
        client_id='14e04f6d28884dcbb4a5a431679516cf',
        client_secret='62ccbe9d8bf54d19ab71dd8451ead4bb',
        redirect_uri='http://localhost:5000/callback',
        scope='user-top-read user-read-recently-played'
    )