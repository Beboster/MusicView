import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os


CLIENT_ID =  os.environ.get("cID")
CLIENT_SECRET = os.environ.get("cSecret")
REDIRECT_URI = "http://localhost:8080/"
SCOPE = "user-library-read"  # You can adjust this to the permissions you need

# Set up the SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                         redirect_uri=REDIRECT_URI, scope=SCOPE)
def get_top(track_name,artist_name):

# Create a Spotipy object to interact with the API
    sp = spotipy.Spotify(auth_manager=sp_oauth)

    playlists = sp.current_user_playlists()
    # Example: Get the current user's playlists
    # Convert the playlists result to JSON format
    playlists_json = json.dumps(playlists, indent=4)
 
    if artist_name == '':
        query = track_name
    elif track_name == '':
        query = artist_name
    else:    
        query = f"artist:{artist_name} track:{track_name}"
    result = sp.search(q=query, type="track", limit=5)

    artists = json.dumps(result, indent=4)
    artists = result['tracks']['items'][0]['album']['artists']

    track = json.dumps(result, indent=4)
    track = result['tracks']['items'][0]['name']

    artist_names = [artist['name'] for artist in artists]
    # Print the JSON result
    print(track)
    print(artist_names)
