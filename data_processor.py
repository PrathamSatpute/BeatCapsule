import pandas as pd

def process_data(raw_data):
    top_artists = pd.DataFrame([(item['name'], item['popularity']) for item in raw_data['top_artists']['items']], 
                               columns=['artist', 'popularity'])
    
    top_tracks = pd.DataFrame([(item['name'], item['artists'][0]['name']) for item in raw_data['top_tracks']['items']], 
                              columns=['track', 'artist'])
    
    recent_tracks = pd.DataFrame([(item['track']['name'], item['played_at']) for item in raw_data['recent_tracks']['items']], 
                                 columns=['track', 'played_at'])
    recent_tracks['played_at'] = pd.to_datetime(recent_tracks['played_at'])
    
    listening_time = len(recent_tracks) * 3  # Assuming average song length of 3 minutes
    
    return {
        'top_artists': top_artists,
        'top_tracks': top_tracks,
        'recent_tracks': recent_tracks,
        'listening_time': listening_time
    }