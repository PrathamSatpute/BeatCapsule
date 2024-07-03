import spotipy

def fetch_spotify_data(token_info):
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    top_artists = sp.current_user_top_artists(limit=5, time_range='short_term')
    top_tracks = sp.current_user_top_tracks(limit=5, time_range='short_term')
    recent_tracks = sp.current_user_recently_played(limit=50)
    
    return {
        'top_artists': top_artists,
        'top_tracks': top_tracks,
        'recent_tracks': recent_tracks
    }