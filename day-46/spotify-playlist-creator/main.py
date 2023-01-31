
from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Environmental Variables
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
URI = "http://example.com"

# Get song list from Billboard website
date = input("What year would you like to create from?"
             "\nType the date in format YYYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
# print(response.status_code)
top_100_songs = response.text

# scrape song titles into a list
soup = BeautifulSoup(top_100_songs, "html.parser")
song_titles = soup.select(selector="li h3")
all_song_titles = [each.getText().strip("\n, \t") for each in song_titles[:100]]
# print(all_song_titles)

# Spotify Authentication
spotify_auth = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
# User ID from Spotify
user_id = spotify_auth.current_user()["id"]
# print(user_id)

# get Song URIs for each song in song list
song_uris = []
year = date.split("-")[0]

for each in all_song_titles:
    result = spotify_auth.search(q=f"track:{each} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{each} does not exist in Spotify.")

# Create playlist on Spotify
playlist = spotify_auth.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
spotify_auth.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
